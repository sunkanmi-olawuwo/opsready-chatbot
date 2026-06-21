# Understanding GenAIOps Support Copilot

GenAIOps Support Copilot is a portfolio-grade application for learning and demonstrating the full lifecycle of a generative AI support system. It answers developer questions about Azure AI Search and Microsoft Foundry by using an agent grounded in a knowledge base.

## Why It Exists

Many AI demos stop after calling a model. This project is designed to show the operational layers around the model: planning, prompt versioning, knowledge grounding, evaluation, monitoring, tracing, and continuous improvement.

## Main Flow

```text
User question
  -> React dashboard
  -> FastAPI orchestration API
  -> Microsoft Foundry Agent provider
  -> Knowledge base / file search tool
  -> Azure Blob Storage source documents
  -> Azure AI Search-backed retrieval
  -> Grounded answer with citations, metadata, and trace context
```

## Current Implementation

The repository starts with local adapters:

- local mock agent
- local markdown knowledge source
- prompt file loader
- deterministic evaluation dataset
- frontend dashboard shell
- FastAPI API contract

These adapters make the app runnable before Azure credentials are configured. They are not the final architecture.

## Target Implementation

The Azure-backed version will use:

- Microsoft Foundry Agents
- Foundry knowledge base / file search grounding
- Azure Blob Storage for source documentation
- Azure AI Search-backed retrieval through Foundry tooling
- Foundry evaluations and GitHub Actions
- Foundry/Application Insights/OpenTelemetry monitoring and tracing

## Certification Preparation

The project supports Microsoft AI certification preparation by creating practical evidence for agent design, RAG-style grounding, Azure AI Search, prompt management, evaluation, monitoring, tracing, responsible AI, and CI/CD.

## When Returning Later

Read these files first:

1. `wiki/evolution/implementation-log.md`
2. `wiki/features/feature-coverage.md`
3. `wiki/evolution/roadmap.md`
4. `wiki/learning-path/README.md`
5. `README.md`
