from pathlib import Path

from fastapi import Depends

from app.core.config import Settings, get_settings
from app.models.prompts import PromptInfo


class PromptLoader:
    def __init__(self, prompt_directory: Path) -> None:
        self.prompt_directory = prompt_directory

    def list_prompts(self) -> list[PromptInfo]:
        prompts: list[PromptInfo] = []
        for path in sorted(self.prompt_directory.glob("*.md")):
            prompts.append(
                PromptInfo(
                    name=path.stem,
                    path=str(path),
                    description=self._description_for(path.stem),
                )
            )
        return prompts

    def load(self, prompt_version: str) -> str:
        path = self.prompt_directory / f"{prompt_version}.md"
        if not path.exists():
            raise FileNotFoundError(f"Prompt version not found: {prompt_version}")
        return path.read_text(encoding="utf-8")

    @staticmethod
    def render(template: str, *, question: str, context: str) -> str:
        return template.replace("{{question}}", question).replace("{{context}}", context)

    @staticmethod
    def _description_for(name: str) -> str:
        descriptions = {
            "support_answer_v1": "Baseline grounded support prompt for Foundry agent instructions.",
            "support_answer_v2": "More structured support prompt for comparison and evaluation.",
        }
        return descriptions.get(name, "Prompt instruction asset.")


def get_prompt_loader(settings: Settings = Depends(get_settings)) -> PromptLoader:
    return PromptLoader(settings.prompt_directory)
