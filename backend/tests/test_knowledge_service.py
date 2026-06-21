from pathlib import Path

from app.services.knowledge_service import KnowledgeService


def test_knowledge_service_finds_sources() -> None:
    service = KnowledgeService(Path("../data/sample-docs"), "local")
    sources = service.list_sources()
    assert sources
    assert sources[0].target.startswith("Foundry knowledge base")


def test_knowledge_service_searches_chunks() -> None:
    service = KnowledgeService(Path("../data/sample-docs"), "local")
    chunks, latency = service.search("Foundry Agents tools", 3)
    assert chunks
    assert latency >= 0
