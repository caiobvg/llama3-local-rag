import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaEmbeddings, ChatOllama

PROJECT_PATH = "./test" 
EMBED_MODEL = "nomic-embed-text" 
LLM_MODEL = "llama3" 
DB_DIR = "./chroma_db" 

def index_project():
    print(f"Starting indexing...")

    loader = DirectoryLoader(
        PROJECT_PATH,
        glob="**/calculations.py", 
        loader_cls=TextLoader,
        use_multithreading=True,
        show_progress=True
    )
    
    documents = loader.load()

    if not documents:
        print("No documents found. Make sure 'calculations.py' exists.")
        return

    print(f"\nTotal files loaded: {len(documents)}")

    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language="python",
        chunk_size=2000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    
    print(f"Documents split into {len(chunks)} chunks.")

    embeddings = OllamaEmbeddings(model=EMBED_MODEL)

    print("Creating vector database...")
    db = Chroma.from_documents(
        chunks, 
        embeddings, 
        persist_directory=DB_DIR
    )
    
    print(f"Database created and saved to {DB_DIR}")

def start_chat():
    print("Starting RAG chat...")

    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 8}
    )

    llm = ChatOllama(model=LLM_MODEL)

    template = """
    You are an expert programming assistant.
    Answer the user's question based **only** on the following code context.
    If the answer is not in the context, say "I could not find that information in the code."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    print("Chat is ready. Ask questions about your code (type 'exit' to quit).")
    while True:
        try:
            question = input("\nYour question: ")
            if question.lower() == 'exit':
                break
            
            print("Thinking...")
            for response_chunk in chain.stream(question):
                print(response_chunk, end="", flush=True)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    if not os.path.exists(DB_DIR):
        index_project()
    
    start_chat()