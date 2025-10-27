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

| Component | Technology | Role in Project |
| :--- | :--- | :--- |
| **LLM (Generator)** | **Llama 3** (via Ollama) | The main model that generates text responses. |
| **Embeddings** | **Nomic Embed** (via Ollama) | Creates the vector representation (the "meaning") of the code for search. |
| **RAG Framework** | **LangChain** | Orchestrates the entire pipeline: loading, splitting, retrieval, and LLM calling. |
| **Vector Store** | **ChromaDB** | Persistent and efficient storage of the code index. |
| **Local Engine** | **Ollama** | Responsible for running the LLM and Embedding models locally. |

---

## Setup and Usage

Follow these steps to get the assistant running.

### Prerequisites

1.  **Python 3.10+**
2.  **Ollama** (Installed and running)
3.  **Download Models** (Execute in the terminal after installing Ollama):
    ```bash
    ollama pull llama3
    ollama pull nomic-embed-text
    ```

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/caiobvg/llama3-local-rag
    cd llama3-local-rag
    ```

2.  **Set up Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python Dependencies:**
    ```bash
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

## Project Structure

| File/Folder | Description |
| :--- | :--- |
| `main.py` | Contains the core RAG pipeline code, including indexing logic and the chat loop. |
| `calculations.py` | The example code file used as the data source (Knowledge Base). |
| `venv/` | Python virtual environment (ignored by Git). |
| `chroma_db/` | Vector database cache (the code index, ignored by Git). |
| `.gitignore` | File that prevents large cache and dependency folders from being uploaded. |
