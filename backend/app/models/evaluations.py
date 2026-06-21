from pydantic import BaseModel


class EvaluationSummary(BaseModel):
    run_id: str
    status: str
    dataset: str
    overall_score: float
    groundedness_score: float
    citation_score: float
    notes: str


class EvaluationSummaryResponse(BaseModel):
    summary: EvaluationSummary
