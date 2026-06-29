from typing import List


class ChunkBuilder:
    """
    Splits formatted documents into semantic chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 200
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def build(
        self,
        documents: List[dict]
    ) -> List[dict]:

        chunks = []

        for document in documents:
            chunks.extend(
                self._split_document(document)
            )

        return chunks

    def _split_document(
        self,
        document: dict
    ) -> List[dict]:

        text = document["text"]
        source = document["source"]
        document_id = document["id"]

        chunks = []

        start = 0
        chunk_number = 1

        while start < len(text):

            end = min(
                start + self.chunk_size,
                len(text)
            )

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append(
                    {
                        "id": f"{document_id}-{chunk_number}",
                        "document_id": document_id,
                        "chunk_number": chunk_number,
                        "source": source,
                        "text": chunk_text,
                        "raw": document["raw"]
                    }
                )

            if end == len(text):
                break

            start = end - self.overlap
            chunk_number += 1

        return chunks