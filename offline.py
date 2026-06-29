from app.config import (
    KNOWLEDGE_PATH,
    EMBEDDING_MODEL,
    INDEX_PATH,
    CHUNKS_PATH
)

from app.platform.document_loader import DocumentLoader
from app.platform.chunk_builder import ChunkBuilder
from app.platform.embeddings import EmbeddingModel
from app.platform.vector_store import VectorStore


def main():

    print("=" * 60)
    print("Enterprise AI Knowledge Index Builder")
    print("=" * 60)

    # --------------------------------------------------
    # Load Documents
    # --------------------------------------------------

    print("\nLoading documents...")

    loader = DocumentLoader(
        KNOWLEDGE_PATH
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} document(s).")

    # --------------------------------------------------
    # Build Chunks
    # --------------------------------------------------

    print("\nBuilding chunks...")

    chunk_builder = ChunkBuilder()

    chunks = chunk_builder.build(
        documents
    )

    print(f"Created {len(chunks)} chunk(s).")

    # --------------------------------------------------
    # Generate Embeddings
    # --------------------------------------------------

    print("\nGenerating embeddings...")

    embedding_model = EmbeddingModel(
        EMBEDDING_MODEL
    )

    embeddings = []

    for i, chunk in enumerate(chunks, start=1):

        print(
            f"Embedding {i}/{len(chunks)}",
            end="\r"
        )

        embeddings.append(

            embedding_model.embed(

                chunk["text"]

            )

        )

    print(f"\nGenerated {len(embeddings)} embedding(s).")

    # --------------------------------------------------
    # Save Vector Store
    # --------------------------------------------------

    print("\nSaving vector store...")

    VectorStore.save(

        embeddings=embeddings,

        chunks=chunks,

        index_path=INDEX_PATH,

        chunks_path=CHUNKS_PATH

    )

    print("\nVector store created successfully.")

    print("=" * 60)
    print("Offline indexing completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()