from pydantic import BaseModel, Field


class WorkflowRequest(BaseModel):
    """
    Request received from Appian.
    """

    question: str = Field(
        ...,
        min_length=3,
        description="Business user's workflow question"
    )