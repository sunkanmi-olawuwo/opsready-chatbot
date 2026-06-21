from time import perf_counter

from app.models.knowledge import KnowledgeChunk
from app.services.agent_client import AgentResult


class LocalAgentClient:
    """Deterministic local stand-in for Microsoft Foundry Agents."""

    async def answer(self, *, question: str, prompt: str, chunks: list[KnowledgeChunk]) -> AgentResult:
        started = perf_counter()
        if not chunks:
            answer = "I do not have enough information in the configured knowledge sources to answer that."
        else:
            source_names = ", ".join(dict.fromkeys(chunk.source for chunk in chunks))
            summary = chunks[0].content.replace("\n", " ")
            answer = (
                f"Based on the configured knowledge sources, {summary} "
                f"Relevant sources: {source_names}."
            )

        elapsed_ms = int((perf_counter() - started) * 1000)
        return AgentResult(
            answer=answer,
            model="local-foundry-agent-mock",
            input_tokens=len(prompt.split()),
            output_tokens=len(answer.split()),
            agent_latency_ms=elapsed_ms,
        )
