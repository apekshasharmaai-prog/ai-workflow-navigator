from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

KNOWLEDGE_PATH = DATA_DIR / "knowledge"

VECTOR_STORE_DIR = DATA_DIR / "vector_store"

INDEX_PATH = VECTOR_STORE_DIR / "index.faiss"

CHUNKS_PATH = VECTOR_STORE_DIR / "chunks.json"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

VECTOR_DIMENSION = 384

TOP_K = 3

OLLAMA_MODEL = "llama3.2:3b"
print(BASE_DIR)