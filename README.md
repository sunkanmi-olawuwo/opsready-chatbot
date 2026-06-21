# GenAIOps Support Copilot

A portfolio-grade GenAIOps platform for building, evaluating, monitoring, and tracing a Microsoft Foundry Agents application grounded in Azure AI Search documentation.

> Screenshot placeholder: add the running dashboard screenshot after the first UI pass.

## What This Demonstrates

- Microsoft Foundry Agents with knowledge base / file search grounding
- Azure Blob Storage as the source document store
- Azure AI Search-backed retrieval through Foundry knowledge tooling
- Prompt and agent instruction versioning with GitHub
- Structured and automated evaluations
- Monitoring, cost awareness, and distributed tracing
- A production-style React + FastAPI engineering dashboard

## Architecture

```text
React dashboard
  -> FastAPI orchestration API
  -> Agent provider
      -> Local mock agent for development
      -> Microsoft Foundry Agent for Azure-backed execution
          -> Knowledge base / file search
          -> Azure Blob Storage source content
          -> Azure AI Search-backed retrieval
  -> Evaluations, telemetry, traces, and documentation
```

The local scaffold works without cloud credentials, but the target architecture follows the Microsoft Learn GenAIOps path and the newer Microsoft Foundry Agents model.

## Tech Stack

- Frontend: React, TypeScript, Vite, Tailwind-style CSS, TanStack Query-ready service layer
- Backend: Python, FastAPI, Pydantic, pytest, Ruff, structured service layers
- AI platform target: Microsoft Foundry Agents, knowledge base / file search, Azure Blob Storage, Azure AI Search
- Ops: GitHub Actions, evaluation scripts, telemetry/tracing abstractions, wiki-first documentation

## Quick Start

```bash
cd backend
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Use Python 3.11-3.13 for the backend. Python 3.14 is ahead of some pinned package wheels at the moment.

```bash
cd frontend
pnpm install
pnpm run dev
```

Frontend package management uses `pnpm`, not npm.

## Documentation

The root README is intentionally short. The main project memory lives in [wiki/README.md](wiki/README.md).

Start with:

- [Project onboarding](wiki/getting-started/project-onboarding.md)
- [Learning path sync](wiki/learning-path/README.md)
- [Architecture overview](wiki/architecture/overview.md)
- [Roadmap](wiki/evolution/roadmap.md)

## Status

Foundation scaffold in progress. The project starts with local development adapters and evolves toward Microsoft Foundry Agents, Azure Blob Storage, Azure AI Search-backed knowledge grounding, Foundry evaluations, monitoring, and tracing.
