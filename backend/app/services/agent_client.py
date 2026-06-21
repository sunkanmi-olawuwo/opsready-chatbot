from typing import Protocol

from app.models.knowledge import KnowledgeChunk


class AgentResult:
    def __init__(self, answer: str, model: str, input_tokens: int, output_tokens: int, agent_latency_ms: int) -> None:
        self.answer = answer
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.agent_latency_ms = agent_latency_ms


class AgentClient(Protocol):
    async def answer(self, *, question: str, prompt: str, chunks: list[KnowledgeChunk]) -> AgentResult:
        """Return a grounded answer from an agent provider."""
