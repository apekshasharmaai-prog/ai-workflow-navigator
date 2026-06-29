from dataclasses import dataclass, asdict
from typing import List


@dataclass
class WorkflowResponse:

    summary: str

    current_stage: str

    current_approver: str

    reason: str

    next_step: str

    sla: str

    sources: List[str]

    confidence: float

    def to_dict(self):

        return asdict(self)