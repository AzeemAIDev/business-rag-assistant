<h1>Business RAG Assistant</h1>

<h2>Overview</h2>
<p>
Business RAG Assistant is an AI-powered application designed for companies to provide accurate internal information based on user queries.
The system uses <strong>Retrieval-Augmented Generation (RAG)</strong> to retrieve relevant company data from a vector database and generate intelligent responses using an LLM.
</p>

<p>This project is useful for answering questions like:</p>
<ul>
  <li>Company details</li>
  <li>Management information (CEO, Manager, etc.)</li>
  <li>Salary structure</li>
  <li>Internal policies and general company knowledge</li>
</ul>

<h2>How It Works</h2>
<ol>
  <li>Company data is stored in <strong>Qdrant vector store</strong>.</li>
  <li>When a user asks a question, relevant data is retrieved from Qdrant.</li>
  <li>The retrieved data is analyzed using <strong>DeepSeek LLM API</strong>.</li>
  <li>A clear and accurate response is generated for the user.</li>
</ol>

<h2>Privacy &amp; Security</h2>
<p>To maintain privacy and security:</p>
<ul>
  <li><strong>API keys and URLs are NOT exposed</strong> in the codebase.</li>
  <li>Sensitive information is managed using environment variables and configuration files.</li>
</ul>

<h2>Environment Variables (.env)</h2>
<p>Create a <code>.env</code> file in the root directory and add your LLM API keys there.</p>

<pre>
DEEPSEEK_API_KEY=your_api_key_here
</pre>

<h2>Configuration (config.json)</h2>
<p>The <code>config.json</code> file is used to store:</p>
<ul>
  <li>Qdrant API key</li>
  <li>Qdrant URL</li>
</ul>
<p>This file allows easy configuration without modifying core code.</p>

<h2>Vector Store Setup</h2>
<ul>
  <li>The notebook <code>vector_store_setup.ipynb</code> is provided.</li>
  <li>Use it to:</li>
  <ul>
    <li>Upload your data to Qdrant</li>
    <li>Create embeddings</li>
    <li>Store and retrieve vectors efficiently</li>
  </ul>
</ul>

<h2>Project Structure</h2>
<pre>
business-rag-assistant/
│
├── Images/
│   ├── Screenshot 2026-01-03 211644.png
│   ├── Screenshot 2026-01-03 214912.png
│   └── Screenshot 2026-01-03 215256.png
│
├── Code/
│   └── vector_store_setup.ipynb
├── README.md
├── app.py
├── config.json
├── index.html
├── requirements.txt

</pre>

<h2>Installation &amp; Setup</h2>

<h3>1. Clone the Repository</h3>
<pre>
git clone https://github.com/AzeemAIDev/business-rag-assistant.git
cd business-rag-assistant
</pre>

<h3>2. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Run Backend Server</h3>
<pre>
uvicorn app:app --port 8000
</pre>

<h3>4. Run Frontend</h3>
<ul>
  <li>Right-click on <code>index.html</code></li>
  <li>Select <strong>Open with Live Server</strong></li>
</ul>

<h2>Technologies Used</h2>
<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>Qdrant Vector Database</li>
  <li>DeepSeek LLM API</li>
  <li>Retrieval-Augmented Generation (RAG)</li>
</ul>

<h2>Author</h2>
<p>
<strong>Azeem</strong><br>
ML Engineer &amp; AI Learner<br>
<a href="https://github.com/AzeemAIDev" target="_blank">
https://github.com/AzeemAIDev
</a>
</p>
