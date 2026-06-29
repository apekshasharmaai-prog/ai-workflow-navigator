import json
from pathlib import Path

from app.platform.document_formatter import DocumentFormatter


class DocumentLoader:
    """
    Loads workflow documents from disk.

    Returns:
    - id
    - source
    - raw document
    - formatted text
    """

    def __init__(self, documents_path):

        self.documents_path = Path(documents_path)

    def load(self):

        documents = []

        for file in self.documents_path.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:
                raw = json.load(f)

            documents.append(
                {
                    "id": raw.get("id", file.stem),
                    "source": file.name,
                    "raw": raw,
                    "text": DocumentFormatter.format(raw)
                }
            )

        return documents