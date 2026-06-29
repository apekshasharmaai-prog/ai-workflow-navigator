from app.platform.document_loader import DocumentLoader
from app.platform.chunk_builder import ChunkBuilder


loader = DocumentLoader(
    "data/knowledge"
)

documents = loader.load_documents()

builder = ChunkBuilder()

chunks = builder.build_chunks(
    documents
)

print()

print("=" * 50)

print(f"Chunks: {len(chunks)}")

print("=" * 50)

print(chunks[0]["text"])