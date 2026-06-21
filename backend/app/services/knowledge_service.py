from pathlib import Path
from time import perf_counter

from fastapi import Depends

from app.core.config import Settings, get_settings
from app.models.knowledge import KnowledgeChunk, KnowledgeSource


class KnowledgeService:
    """Local development adapter for the target Foundry knowledge base/file search layer."""

    def __init__(self, docs_directory: Path, provider: str) -> None:
        self.docs_directory = docs_directory
        self.provider = provider

    def search(self, question: str, top_k: int) -> tuple[list[KnowledgeChunk], int]:
        started = perf_counter()
        chunks = self._load_chunks()
        query_terms = {term.lower().strip(".,?:;()[]") for term in question.split() if len(term) > 2}

        scored: list[KnowledgeChunk] = []
        for chunk in chunks:
            content_terms = chunk.content.lower()
            matches = sum(1 for term in query_terms if term in content_terms)
            if matches:
                scored.append(chunk.model_copy(update={"score": round(matches / max(len(query_terms), 1), 3)}))

        if not scored:
            scored = [chunk.model_copy(update={"score": 0.1}) for chunk in chunks[:top_k]]

        scored.sort(key=lambda item: item.score, reverse=True)
        elapsed_ms = int((perf_counter() - started) * 1000)
        return scored[:top_k], elapsed_ms

    def list_sources(self) -> list[KnowledgeSource]:
        sources: list[KnowledgeSource] = []
        for path in sorted(self.docs_directory.glob("*.md")):
            content = path.read_text(encoding="utf-8")
            sources.append(
                KnowledgeSource(
                    title=self._title_from(content, path),
                    source=path.name,
                    provider=self.provider,
                    chunk_count=len(self._split_content(content)),
                    status="local-development-source",
                    target="Foundry knowledge base / file search backed by Azure Blob Storage and Azure AI Search",
                )
            )
        return sources

    def _load_chunks(self) -> list[KnowledgeChunk]:
        chunks: list[KnowledgeChunk] = []
        for path in sorted(self.docs_directory.glob("*.md")):
            content = path.read_text(encoding="utf-8")
            title = self._title_from(content, path)
            for index, chunk_text in enumerate(self._split_content(content), start=1):
                chunks.append(
                    KnowledgeChunk(
                        title=title,
                        source=path.name,
                        chunk_id=f"{path.stem}-{index:03d}",
                        content=chunk_text,
                        score=0.0,
                    )
                )
        return chunks

    @staticmethod
    def _title_from(content: str, path: Path) -> str:
        for line in content.splitlines():
            if line.startswith("# "):
                return line.removeprefix("# ").strip()
        return path.stem.replace("-", " ").title()

    @staticmethod
    def _split_content(content: str) -> list[str]:
        paragraphs = [paragraph.strip() for paragraph in content.split("\n\n") if paragraph.strip()]
        return paragraphs or [content.strip()]


def get_knowledge_service(settings: Settings = Depends(get_settings)) -> KnowledgeService:
    return KnowledgeService(settings.sample_docs_directory, settings.knowledge_provider)
