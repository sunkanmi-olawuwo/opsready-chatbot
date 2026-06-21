from pydantic import BaseModel


class TelemetrySummary(BaseModel):
    request_count: int
    average_latency_ms: int
    average_agent_latency_ms: int
    average_knowledge_latency_ms: int
    total_input_tokens: int
    total_output_tokens: int
    error_count: int
    provider: str


class TraceStep(BaseModel):
    name: str
    duration_ms: int
    status: str


class TraceListResponse(BaseModel):
    traces: list[dict[str, object]]
