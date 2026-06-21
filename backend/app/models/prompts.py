from pydantic import BaseModel


class PromptInfo(BaseModel):
    name: str
    path: str
    description: str


class PromptListResponse(BaseModel):
    prompts: list[PromptInfo]
