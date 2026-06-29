from app.config import (
    EMBEDDING_MODEL,
    INDEX_PATH,
    CHUNKS_PATH,
    OLLAMA_MODEL
)

from app.platform.embeddings import EmbeddingModel
from app.platform.retriever import Retriever
from app.platform.llm import LocalLLM

from app.workflow.service import WorkflowService


def create_workflow_service():

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

    return WorkflowService(

        retriever,

        llm

    )