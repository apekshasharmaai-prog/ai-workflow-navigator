from utils.embeddings import generate_embeddings
from utils.vector_store import (
    load_index,
    load_chunks,
    search
)

def retrieve(question, top_k=3):
    """
    Retrieves the most relevant chunks
    for a user question.
    """

    # Load vector database
    index = load_index()

    # Load chunk objects
    chunks = load_chunks()

    # Generate embedding for question
    query_embedding = generate_embeddings([question])[0]

    # Search FAISS
    indices = search(
        index,
        query_embedding,
        top_k
    )

    # Retrieve matching chunks
    results = []

    for chunk_index in indices:

        results.append(chunks[chunk_index])

    return results

question = "Why is Cargo Request failing with HTTP 401?"

results = retrieve(question)

for i, chunk in enumerate(results, start=1):
    print("=" * 80)
    print(f"Result {i}")
    print(f"ID    : {chunk['id']}")
    print(f"Type  : {chunk['type']}")
    print(f"Title : {chunk['title']}")
    print()
    print(chunk["text"])