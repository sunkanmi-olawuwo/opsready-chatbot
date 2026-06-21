from fastapi import APIRouter, Depends

from app.models.prompts import PromptListResponse
from app.prompts.prompt_loader import PromptLoader, get_prompt_loader

router = APIRouter()


@router.get("/prompts", response_model=PromptListResponse)
async def list_prompts(loader: PromptLoader = Depends(get_prompt_loader)) -> PromptListResponse:
    return PromptListResponse(prompts=loader.list_prompts())
