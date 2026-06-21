from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    settings = get_settings()
    return {
        "status": "ok",
        "service": "genaiops-support-copilot",
        "environment": settings.app_env,
        "agent_provider": settings.agent_provider,
        "knowledge_provider": settings.knowledge_provider,
    }
