# lama3-local-rag

A 100% local and private AI assistant for code, built with the RAG (Retrieval-Augmented Generation) architecture.

This project demonstrates how to use open-source Large Language Models (LLMs) like Llama 3 to converse about complex codebases, without sending any files to cloud services like OpenAI or GitHub Copilot.

---

## Features

* **Private Code Analysis:** All processing (embeddings and generation) is executed locally via **Ollama**.
* **RAG Core:** Implements the RAG pipeline to ensure LLM responses are based **only** on your source code, preventing "hallucinations."
* **Project Support:** Configured to analyze Python files and easily adaptable to TypeScript, HTML, etc.
* **Persistent Index:** Uses **ChromaDB** to save the code's "knowledge," allowing the script to be restarted without re-indexing the entire project.

---

## Technologies Used

| Component | Technology |
| :--- | :--- |
| **LLM (Generator)** | **Llama 3** (via Ollama) |
| **Embeddings** | **Nomic Embed** (via Ollama) |
| **RAG Framework** | **LangChain** | 
| **Vector Store** | **ChromaDB** | 
| **Local Engine** | **Ollama** | 

---

## Setup and Usage

### Prerequisites

1.  **Python 3.10+**
2.  **Ollama** (Installed and running)
3.  **Download Models** (Execute in the terminal after installing Ollama):
    ```bash
    ollama pull llama3
    ollama pull nomic-embed-text
    ```

### Installation

    ```bash
    git clone https://github.com/caiobvg/llama3-local-rag
    cd llama3-local-rag
    python3 -m venv venv
    source venv/bin/activate
    pip install langchain-community langchain-core langchain-text-splitters langchain-ollama chromadb
    ```

### Usage

The project is configured to read the example file `calculations.py`.

1.  **Run the Script:**
    ```bash
    python main.py
    ```

2.  **First Run (Indexing):**
    The script will execute the `index_project()` function. It will read `calculations.py`, create the embeddings (the most time-consuming step), and save the index to the `chroma_db/` folder.

3.  **Chat:**
    After indexing, the chat will start. Ask questions about the code in `calculations.py`:

    ```
    Your question: What is the purpose of the GeometryCalculator class?
    Thinking...
    ```

---
