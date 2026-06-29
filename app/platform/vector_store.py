import faiss
import json
import numpy as np
from pathlib import Path


class VectorStore:

    def __init__(
        self,
        dimension,
        index_path,
        chunks_path
    ):

        self.dimension = dimension

        self.index_path = Path(index_path)

        self.chunks_path = Path(chunks_path)

        self.index = faiss.IndexFlatIP(
            dimension
        )

    def add_embeddings(
        self,
        embeddings
    ):

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        self.index.add(
            embeddings
        )

    def save_index(self):

        self.index_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            str(self.index_path)
        )

    def save_chunks(
        self,
        chunks
    ):

        self.chunks_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.chunks_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                chunks,
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def load_index(index_path):

        return faiss.read_index(
            str(index_path)
        )

    @staticmethod
    def load_chunks(chunks_path):

        with open(
            chunks_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)
    @classmethod
    def save(
    cls,
    embeddings,
    chunks,
    index_path,
    chunks_path
    ):
        """
        Creates and saves a FAISS index along with
        the corresponding chunks.
        """

        if not embeddings:
            raise ValueError("No embeddings to save.")

        dimension = len(embeddings[0])

        vector_store = cls(
            dimension,
            index_path,
            chunks_path
        )

        vector_store.add_embeddings(
            embeddings
        )

        vector_store.save_index()

        vector_store.save_chunks(
            chunks
        )