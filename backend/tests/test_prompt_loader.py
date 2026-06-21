from pathlib import Path

from app.prompts.prompt_loader import PromptLoader


def test_prompt_loader_lists_prompts() -> None:
    loader = PromptLoader(Path("../prompts"))
    prompts = loader.list_prompts()
    assert any(prompt.name == "support_answer_v1" for prompt in prompts)


def test_prompt_loader_renders_template() -> None:
    rendered = PromptLoader.render("Q={{question}} C={{context}}", question="What?", context="Docs")
    assert rendered == "Q=What? C=Docs"
