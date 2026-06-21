from fastapi.testclient import TestClient

from app.main import app


def test_prompts_endpoint_lists_prompt_versions() -> None:
    client = TestClient(app)
    response = client.get("/api/prompts")

    assert response.status_code == 200
    prompts = response.json()["prompts"]
    assert any(prompt["name"] == "support_answer_v1" for prompt in prompts)


def test_knowledge_sources_endpoint_lists_local_sources() -> None:
    client = TestClient(app)
    response = client.get("/api/knowledge/sources")

    assert response.status_code == 200
    sources = response.json()["sources"]
    assert sources
    assert sources[0]["target"].startswith("Foundry knowledge base")
