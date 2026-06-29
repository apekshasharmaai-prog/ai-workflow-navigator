from app.common.models import (
    WorkflowResponse,
    WorkflowMetadata
)
from app.platform.workflow_context_builder import MetadataExtractor
from app.platform.prompts import PromptBuilder
from app.platform.retriever import Retriever
from app.platform.llm import LocalLLM


class WorkflowService:
    """
    Orchestrates the Workflow AI pipeline.

    Responsibilities
    ----------------
    1. Retrieve relevant workflow documents.
    2. Extract deterministic metadata.
    3. Build the LLM prompt.
    4. Generate a business-friendly explanation.
    5. Return the final response.
    """

    def __init__(
        self,
        retriever: Retriever,
        llm: LocalLLM
    ):
        self.retriever = retriever
        self.llm = llm

    def ask(
        self,
        question: str
    ) -> WorkflowResponse:

        # ----------------------------------------
        # Retrieve Relevant Documents
        # ----------------------------------------

        chunks = self.retriever.retrieve(question)

        if not chunks:
            raise ValueError(
                "No relevant workflow documentation found."
            )

        # ----------------------------------------
        # Extract Metadata
        # ----------------------------------------

        metadata = None

        for chunk in chunks:

            if "metadata" in chunk.raw:

                metadata = MetadataExtractor.extract(
                chunk.raw
            )

                break

        if metadata is None:

            metadata = WorkflowMetadata()

        # ----------------------------------------
        # Build Prompt
        # ----------------------------------------

        prompt = PromptBuilder.build(
            question=question,
            metadata=metadata,
            chunks=chunks
        )

        # ----------------------------------------
        # Generate Summary
        # ----------------------------------------

        summary = self.llm.generate(
            prompt
        ).strip()

        # ----------------------------------------
        # Calculate Confidence
        # ----------------------------------------

        confidence = round(
            max(chunk.score for chunk in chunks) * 100,
            1
        )

        # ----------------------------------------
        # Build Response
        # ----------------------------------------

        return WorkflowResponse(
            summary=summary,
            metadata=metadata,
            confidence=confidence,
            sources=sorted(
                {
                    chunk.source
                    for chunk in chunks
                }
            )
        )