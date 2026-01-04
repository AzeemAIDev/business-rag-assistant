import json
import os 
from dotenv import load_dotenv
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from operator import itemgetter
from qdrant_client import QdrantClient

# Load configuration values from JSON file
try:
     with open("config.json" , "r") as f:
        config = json.load(f)
except Exception as e:
    print("File could not loaded" , e)

# Extract configuration parameters
qdrant_url = config["qdrant_url"]
qdrant_api_key = config["qdrant_key"]
embed_model = config["embedding_model_name"]
num_chunks = config["num_chunks"]
collection_name = config["collection_name"]
prompt_str = config["prompt_template"]

# Initialize HuggingFace embedding model
embed_model = HuggingFaceEmbeddings(model_name=embed_model)

# Initialize Qdrant client for vector database connection
client = QdrantClient(
    api_key=qdrant_api_key,
    url=qdrant_url
)

# Connect LangChain vector store with Qdrant
qdrant = QdrantVectorStore(
    embedding=embed_model,
    collection_name=collection_name,
    client=client
)

# Create retriever for similarity search
retriever = qdrant.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": num_chunks}
)

# Load environment variables from .env file
load_dotenv()

# Initialize LLM for response generation
chat_llm = ChatOpenAI(
    model_name="tngtech/deepseek-r1t2-chimera:free",
    openai_api_key=os.getenv("openai_api_key"),
    openai_api_base=os.getenv("openai_api_base"),
    temperature=0
)

# Extract user question from request
query_fetcher = itemgetter("question")

# Format retrieved documents into a single context string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Define RAG pipeline components
_setup = {
    "question": query_fetcher,
    "context": query_fetcher | retriever | format_docs
}

# Create prompt template
_prompt = PromptTemplate.from_template(prompt_str)

# Build full RAG chain
_chain = (_setup | _prompt | chat_llm)

# Allowed origins for local development
origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000"
]

# Initialize FastAPI application
app = FastAPI(
    title="RAG",
    description="RAG system for Business",
    version="1.0.0.0"
)

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request body schema
class Query_Model(BaseModel):
    question: str

# Health check endpoint
@app.get("/")
def get_rot():
    return {"return": "welcome"}

# Endpoint to handle user queries
@app.post("/ask")
def ask_ques(query: Query_Model):
    try:
        response = _chain.invoke({"question": query.question})
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
