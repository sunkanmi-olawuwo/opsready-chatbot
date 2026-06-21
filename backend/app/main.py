from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
    routes_chat,
    routes_evaluations,
    routes_health,
    routes_knowledge,
    routes_prompts,
    routes_telemetry,
)
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="GenAIOps Support Copilot API",
    description="FastAPI backend for a Microsoft Foundry Agents GenAIOps portfolio project.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_health.router, prefix="/api", tags=["health"])
app.include_router(routes_chat.router, prefix="/api", tags=["chat"])
app.include_router(routes_prompts.router, prefix="/api", tags=["prompts"])
app.include_router(routes_knowledge.router, prefix="/api", tags=["knowledge"])
app.include_router(routes_evaluations.router, prefix="/api", tags=["evaluations"])
app.include_router(routes_telemetry.router, prefix="/api", tags=["telemetry"])
