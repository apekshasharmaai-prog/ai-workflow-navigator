from fastapi import APIRouter, HTTPException

from app.api.schemas import WorkflowRequest
from app.workflow.factory import create_workflow_service

router = APIRouter()

service = create_workflow_service()


@router.post("/workflow/explain")
def explain_workflow(request: WorkflowRequest):

    try:

        print("\n" + "=" * 80)
        print("API REQUEST")
        print("=" * 80)
        print("Question:", request.question)

        response = service.ask(
            request.question
        )

        print("\n" + "=" * 80)
        print("WORKFLOW RESPONSE OBJECT")
        print("=" * 80)
        print(response)

        print("\n" + "=" * 80)
        print("WORKFLOW RESPONSE JSON")
        print("=" * 80)
        print(response.to_dict())

        print("\n" + "=" * 80)
        print("METADATA")
        print("=" * 80)
        print("Current Stage    :", response.metadata.current_stage)
        print("Current Approver :", response.metadata.current_approver)
        print("Next Step        :", response.metadata.next_step)
        print("SLA              :", response.metadata.sla)

        print("\n" + "=" * 80)
        print("END API REQUEST")
        print("=" * 80)

        return response.to_dict()

    except Exception as ex:

        print("\n" + "=" * 80)
        print("API ERROR")
        print("=" * 80)
        print(ex)

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )