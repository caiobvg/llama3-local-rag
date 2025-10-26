# lama3-local-rag

Um assistente de IA para código, 100% local e privado, construído com a arquitetura RAG (Geração Aumentada por Recuperação).

Este projeto demonstra como usar Large Language Models (LLMs) de código aberto (Llama 3) para conversar sobre bases de código complexas, sem enviar nenhum arquivo para serviços de nuvem como OpenAI ou GitHub Copilot.

---

## Funcionalidades

* **Análise de Código Privada:** Todo o processamento (embeddings e geração) é executado localmente via **Ollama**.
* **RAG Core:** Implementa o pipeline RAG para garantir que as respostas do LLM sejam baseadas *apenas* no seu código-fonte, evitando alucinações.
* **Suporte a Projetos:** Configurado para analisar arquivos Python e facilmente adaptável para TypeScript, HTML, etc.
* **Índice Persistente:** Usa **ChromaDB** para salvar o "conhecimento" do código, permitindo que o script seja reiniciado sem reindexar o projeto inteiro.

---

## Tecnologias Utilizadas

| Componente | Tecnologia | Função no Projeto |
| :--- | :--- | :--- |
| **LLM (Gerador)** | **Llama 3** (via Ollama) | O modelo principal que gera as respostas em texto. |
| **Embeddings** | **Nomic Embed** (via Ollama) | Cria a representação vetorial (o "significado") do código para busca. |
| **Framework RAG** | **LangChain** | Orquestra todo o pipeline: carregamento, divisão, busca e chamada do LLM. |
| **Banco Vetorial** | **ChromaDB** | Armazenamento persistente e eficiente do índice de código. |
| **Motor Local** | **Ollama** | Responsável por rodar os modelos LLM e de Embeddings na máquina local. |

---

## Como Configurar e Rodar

Siga estes passos para colocar o assistente em funcionamento.

### Pré-requisitos

1.  **Python 3.10+**
2.  **Ollama** (Instalado e rodando)
3.  **Modelos Baixados** (Execute no terminal após instalar o Ollama):
    ```bash
    ollama pull llama3
    ollama pull nomic-embed-text
    ```

### Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/caiobvg/lama3-local-rag.git](https://github.com/caiobvg/lama3-local-rag.git)
    cd lama3-local-rag
    ```

2.  **Configure o Ambiente Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências Python:**
    ```bash
    pip install langchain-community langchain-core langchain-text-splitters langchain-ollama chromadb
    ```

### Uso

O projeto está configurado para ler o arquivo `calculations.py`.

1.  **Execute o Script:**
    ```bash
    python main.py
    ```

2.  **Primeira Execução (Indexação):**
    O script irá rodar a função `indexar_projeto()`. Ele lerá o `calculations.py`, criará os embeddings (o processo mais demorado) e salvará o índice na pasta `chroma_db/`.

3.  **Conversa:**
    Após a indexação, o chat será iniciado. Faça perguntas sobre o código do `calculations.py`:

    ```
    Your question: What is the purpose of the GeometryCalculator class?
    Thinking...
    ```

---

## Estrutura do Projeto

| Arquivo/Pasta | Descrição |
| :--- | :--- |
| `main.py` | Contém o código principal do pipeline RAG, incluindo a lógica de indexação e o loop de chat. |
| `calculations.py` | O arquivo de código de exemplo usado como fonte de dados (Base de Conhecimento). |
| `venv/` | Ambiente virtual Python (ignorado pelo Git). |
| `chroma_db/` | Banco de dados vetorial (o índice do código, ignorado pelo Git). |
| `.gitignore` | Arquivo que impede o envio de pastas grandes e de cache. |
