from app.config import (
    EMBEDDING_MODEL,
    INDEX_PATH,
    CHUNKS_PATH,
    OLLAMA_MODEL
)

from app.platform.embeddings import EmbeddingModel
from app.platform.retriever import Retriever
from app.platform.llm import LocalLLM
from app.platform.workflow_context_builder import MetadataExtractor
from app.workflow.service import WorkflowService


embedding_model = EmbeddingModel(
    EMBEDDING_MODEL
)

retriever = Retriever(
    embedding_model=embedding_model,
    index_path=INDEX_PATH,
    chunks_path=CHUNKS_PATH
)

llm = LocalLLM(
    OLLAMA_MODEL
)

service = WorkflowService(
    retriever,
    llm
)


question = "Why is my purchase request pending?"


print("=" * 80)
print("QUESTION")
print("=" * 80)
print(question)

print("\n")

# ------------------------------------------------------
# Debug Retrieval
# ------------------------------------------------------

chunks = retriever.retrieve(question)

print("=" * 80)
print("RETRIEVED CHUNKS")
print("=" * 80)

for i, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {i}")

    print(f"Source        : {chunk.source}")

    print(f"Document ID   : {chunk.document_id}")

    print(f"Score         : {chunk.score}")

    print(f"Has Metadata  : {'metadata' in chunk.raw}")

    print("-" * 60)

# ------------------------------------------------------
# Debug Metadata
# ------------------------------------------------------

metadata_document = next(
    (
        chunk.raw
        for chunk in chunks
        if "metadata" in chunk.raw
    ),
    {}
)

metadata = MetadataExtractor.extract(
    metadata_document
)

print("\n")
print("=" * 80)
print("EXTRACTED METADATA")
print("=" * 80)

print(metadata)

print("\n")

# ------------------------------------------------------
# Service
# ------------------------------------------------------

response = service.ask(
    question
)

print("=" * 80)
print("FINAL RESPONSE")
print("=" * 80)

print(response)

print("\n")
print("=" * 80)
print("JSON RESPONSE")
print("=" * 80)

print(response.to_dict())