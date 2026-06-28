from pathlib import Path
from utils.document_loader import load_document
from utils.chunking import split_into_chunks
from utils.embeddings import generate_embeddings
from utils.vector_store import (
    create_index,
    add_embeddings,
    save_index,
    save_chunks
)


KNOWLEDGE_BASE = Path("data/knowledge_base")


def build_knowledge_base():

    index = create_index()

    all_chunks = []

    json_files = KNOWLEDGE_BASE.rglob("*.json")

    for file in json_files:

        # Load document
        document = load_document(file)

        # Chunk document
        chunks = split_into_chunks(document)

        # Extract text for embeddings
        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        # Generate embeddings
        embeddings = generate_embeddings(texts)

        # Store vectors
        add_embeddings(index, embeddings)

        # Store chunk metadata
        all_chunks.extend(chunks)

    save_index(index)

    save_chunks(all_chunks)

    print("Knowledge Base Created Successfully.")


if __name__ == "__main__":

    build_knowledge_base()
    