from fastapi import APIRouter, Depends

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService, get_chat_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, service: ChatService = Depends(get_chat_service)) -> ChatResponse:
    return await service.answer(request)
