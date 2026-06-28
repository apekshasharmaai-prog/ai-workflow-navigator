from pathlib import Path

# -----------------------------
# Base Paths
# -----------------------------

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

KNOWLEDGE_BASE_DIR = DATA_DIR / "knowledge_base"

VECTOR_STORE_DIR = DATA_DIR / "vector_store"


# -----------------------------
# Embedding Model
# -----------------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# -----------------------------
# Chunking
# -----------------------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


# -----------------------------
# Retrieval
# -----------------------------

TOP_K = 3


# -----------------------------
# Vector Store
# -----------------------------

VECTOR_DIMENSION = 384

INDEX_PATH = VECTOR_STORE_DIR / "index.faiss"

CHUNKS_PATH = VECTOR_STORE_DIR / "chunks.json"