from app.common.models import WorkflowMetadata


class MetadataExtractor:
    """
    Extracts workflow metadata from the original
    workflow document.

    No LLM.
    No regex.
    Deterministic extraction.
    """

    @staticmethod
    def extract(
        document: dict
    ) -> WorkflowMetadata:

        metadata = document.get(
            "metadata",
            {}
        )

        return WorkflowMetadata(

            current_stage=metadata.get(
                "current_stage",
                "Not Available"
            ),

            current_approver=metadata.get(
                "current_approver",
                "Not Available"
            ),

            next_step=metadata.get(
                "next_step",
                "Not Available"
            ),

            sla=metadata.get(
                "sla",
                "Not Available"
            )

        )