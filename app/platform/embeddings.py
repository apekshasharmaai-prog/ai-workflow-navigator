from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Enterprise embedding model.
    Responsible for converting text into vectors.
    """

    def __init__(self, model_name):

        self.model = SentenceTransformer(model_name)

    def embed(self, text):

        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def embed_documents(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        return self.model.encode(
            texts,
            normalize_embeddings=True
        )