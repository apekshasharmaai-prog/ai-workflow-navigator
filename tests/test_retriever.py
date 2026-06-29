from app.config import (
    EMBEDDING_MODEL,
    INDEX_PATH,
    CHUNKS_PATH
)

from app.platform.retriever import Retriever


retriever = Retriever(

    EMBEDDING_MODEL,

    INDEX_PATH,

    CHUNKS_PATH

)

results = retriever.retrieve(

    "Why is my purchase request pending?"

)

print()

print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"Result {i}")

    print(result["source"])

    print()