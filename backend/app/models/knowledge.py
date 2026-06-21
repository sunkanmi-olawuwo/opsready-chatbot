from pydantic import BaseModel


class KnowledgeChunk(BaseModel):
    title: str
    source: str
    chunk_id: str
    content: str
    score: float


class KnowledgeSource(BaseModel):
    title: str
    source: str
    provider: str
    chunk_count: int
    status: str
    target: str


class KnowledgeSourcesResponse(BaseModel):
    sources: list[KnowledgeSource]
