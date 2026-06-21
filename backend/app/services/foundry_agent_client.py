from app.models.knowledge import KnowledgeChunk
from app.services.agent_client import AgentResult


class FoundryAgentClient:
    """Placeholder for the production Microsoft Foundry Agent integration."""

    async def answer(self, *, question: str, prompt: str, chunks: list[KnowledgeChunk]) -> AgentResult:
        raise NotImplementedError(
            "Foundry Agent integration is planned for the Azure phase. "
            "Use AGENT_PROVIDER=local until Foundry credentials and agent resources are configured."
        )
