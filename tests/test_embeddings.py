from app.platform.document_loader import DocumentLoader
from app.platform.chunk_builder import ChunkBuilder
from app.platform.embeddings import EmbeddingModel

loader = DocumentLoader(
    "data/knowledge"
)

documents = loader.load_documents()

builder = ChunkBuilder()

chunks = builder.build_chunks(documents)

embedding_model = EmbeddingModel(
    "all-MiniLM-L6-v2"
)

vectors = embedding_model.embed_documents(
    chunks
)

print(vectors.shape)