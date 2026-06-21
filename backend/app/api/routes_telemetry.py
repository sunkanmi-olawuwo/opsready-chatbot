from fastapi import APIRouter

from app.models.telemetry import TelemetrySummary, TraceListResponse, TraceStep

router = APIRouter()


@router.get("/telemetry/summary", response_model=TelemetrySummary)
async def telemetry_summary() -> TelemetrySummary:
    return TelemetrySummary(
        request_count=0,
        average_latency_ms=0,
        average_agent_latency_ms=0,
        average_knowledge_latency_ms=0,
        total_input_tokens=0,
        total_output_tokens=0,
        error_count=0,
        provider="local",
    )


@router.get("/traces/recent", response_model=TraceListResponse)
async def recent_traces() -> TraceListResponse:
    return TraceListResponse(
        traces=[
            {
                "trace_id": "local-trace-placeholder",
                "question": "What is hybrid search?",
                "status": "sample",
                "duration_ms": 0,
                "steps": [
                    TraceStep(name="receive_request", duration_ms=0, status="sample"),
                    TraceStep(name="knowledge_search", duration_ms=0, status="sample"),
                    TraceStep(name="agent_response", duration_ms=0, status="sample"),
                ],
            }
        ]
    )
