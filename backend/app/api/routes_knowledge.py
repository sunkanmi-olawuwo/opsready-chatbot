from fastapi import APIRouter, Depends

from app.models.knowledge import KnowledgeSourcesResponse
from app.services.knowledge_service import KnowledgeService, get_knowledge_service

router = APIRouter()


@router.get("/knowledge/sources", response_model=KnowledgeSourcesResponse)
async def knowledge_sources(service: KnowledgeService = Depends(get_knowledge_service)) -> KnowledgeSourcesResponse:
    return KnowledgeSourcesResponse(sources=service.list_sources())
