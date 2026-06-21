from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=3, max_length=4000)
    prompt_version: str = "support_answer_v1"
    top_k: int = Field(default=5, ge=1, le=10)


class Citation(BaseModel):
    title: str
    source: str
    chunk_id: str
    score: float
    provider: str = "local"


class ChatMetadata(BaseModel):
    model: str
    prompt_version: str
    agent_provider: str
    knowledge_provider: str
    latency_ms: int
    knowledge_latency_ms: int
    agent_latency_ms: int
    input_tokens: int
    output_tokens: int
    trace_id: str


class ChatResponse(BaseModel):
    answer: str
    citations: list[Citation]
    metadata: ChatMetadata
