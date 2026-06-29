from app.platform.document_loader import DocumentLoader
loader = DocumentLoader(
    "data/knowledge"
)

documents = loader.load_documents()

print()

print("=" * 50)

print(f"Loaded {len(documents)} documents")

print("=" * 50)

for doc in documents:

    print(doc["source"])

print()