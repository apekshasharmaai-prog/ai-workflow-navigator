import numpy as np

from app.common.models import RetrievedChunk
from app.platform.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant document chunks using
    semantic similarity search.
    """

    def __init__(
        self,
        embedding_model,
        index_path,
        chunks_path
    ):

        self.embedding_model = embedding_model

        self.index = VectorStore.load_index(
            index_path
        )

        self.chunks = VectorStore.load_chunks(
            chunks_path
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 3
    ) -> list[RetrievedChunk]:

        query_embedding = self.embedding_model.embed(
            question
        )

        query_embedding = np.asarray(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:
                continue

            chunk = self.chunks[index]

            results.append(

                RetrievedChunk(

                    id=chunk["id"],

                    document_id=chunk["document_id"],

                    text=chunk["text"],

                    source=chunk["source"],

                    raw=chunk["raw"],

                    score=round(float(distance), 4)

                )

            )

        return results