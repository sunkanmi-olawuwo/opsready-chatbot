from fastapi.testclient import TestClient

from app.main import app


def test_chat_endpoint_returns_answer_with_metadata() -> None:
    client = TestClient(app)
    response = client.post(
        "/api/chat",
        json={
            "question": "What is the role of Microsoft Foundry Agents?",
            "prompt_version": "support_answer_v1",
            "top_k": 3,
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["answer"]
    assert body["citations"]
    assert body["metadata"]["agent_provider"] == "local"
