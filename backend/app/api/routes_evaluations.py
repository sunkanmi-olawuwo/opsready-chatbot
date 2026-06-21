from fastapi import APIRouter

from app.models.evaluations import EvaluationSummary, EvaluationSummaryResponse

router = APIRouter()


@router.get("/evaluations/latest", response_model=EvaluationSummaryResponse)
async def latest_evaluation() -> EvaluationSummaryResponse:
    return EvaluationSummaryResponse(
        summary=EvaluationSummary(
            run_id="local-placeholder",
            status="planned",
            dataset="support_questions.jsonl",
            overall_score=0.0,
            groundedness_score=0.0,
            citation_score=0.0,
            notes="Evaluation workflow scaffolded; Foundry evaluators are planned for the Azure phase.",
        )
    )
