from time import perf_counter
from uuid import uuid4

from fastapi import Depends

from app.core.config import Settings, get_settings
from app.models.chat import ChatMetadata, ChatRequest, ChatResponse, Citation
from app.prompts.prompt_loader import PromptLoader, get_prompt_loader
from app.services.agent_client import AgentClient
from app.services.foundry_agent_client import FoundryAgentClient
from app.services.knowledge_service import KnowledgeService, get_knowledge_service
from app.services.local_agent_client import LocalAgentClient


class ChatService:
    def __init__(
        self,
        settings: Settings,
        prompt_loader: PromptLoader,
        knowledge_service: KnowledgeService,
        agent_client: AgentClient,
    ) -> None:
        self.settings = settings
        self.prompt_loader = prompt_loader
        self.knowledge_service = knowledge_service
        self.agent_client = agent_client

    async def answer(self, request: ChatRequest) -> ChatResponse:
        started = perf_counter()
        chunks, knowledge_latency_ms = self.knowledge_service.search(request.question, request.top_k)
        context = "\n\n".join(f"[{chunk.chunk_id}] {chunk.title}\n{chunk.content}" for chunk in chunks)
        prompt_template = self.prompt_loader.load(request.prompt_version)
        prompt = self.prompt_loader.render(prompt_template, question=request.question, context=context)
        agent_result = await self.agent_client.answer(question=request.question, prompt=prompt, chunks=chunks)
        latency_ms = int((perf_counter() - started) * 1000)

        return ChatResponse(
            answer=agent_result.answer,
            citations=[
                Citation(
                    title=chunk.title,
                    source=chunk.source,
                    chunk_id=chunk.chunk_id,
                    score=chunk.score,
                    provider=self.settings.knowledge_provider,
                )
                for chunk in chunks
            ],
            metadata=ChatMetadata(
                model=agent_result.model,
                prompt_version=request.prompt_version,
                agent_provider=self.settings.agent_provider,
                knowledge_provider=self.settings.knowledge_provider,
                latency_ms=latency_ms,
                knowledge_latency_ms=knowledge_latency_ms,
                agent_latency_ms=agent_result.agent_latency_ms,
                input_tokens=agent_result.input_tokens,
                output_tokens=agent_result.output_tokens,
                trace_id=f"local-{uuid4()}",
            ),
        )


def get_agent_client(settings: Settings = Depends(get_settings)) -> AgentClient:
    if settings.agent_provider == "foundry":
        return FoundryAgentClient()
    return LocalAgentClient()


def get_chat_service(
    settings: Settings = Depends(get_settings),
    prompt_loader: PromptLoader = Depends(get_prompt_loader),
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
    agent_client: AgentClient = Depends(get_agent_client),
) -> ChatService:
    return ChatService(settings, prompt_loader, knowledge_service, agent_client)
