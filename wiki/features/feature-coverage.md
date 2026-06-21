# Feature Coverage

| Feature | Status | Evidence |
| --- | --- | --- |
| FastAPI backend scaffold | Implemented | `backend/app/main.py` |
| React dashboard scaffold | Implemented | `frontend/src/App.tsx` |
| Local agent adapter | Implemented | `backend/app/services/local_agent_client.py` |
| Foundry Agent provider boundary | Planned | `backend/app/services/foundry_agent_client.py` |
| Local knowledge source | Implemented | `data/sample-docs` |
| Foundry knowledge base / file search | Planned | `wiki/plans/003-azure-knowledge-base-integration-plan.md` |
| Azure Blob Storage source documents | Planned | `.env.example` |
| Azure AI Search-backed retrieval | Planned | `wiki/architecture/data-and-retrieval.md` |
| Prompt versioning | In Progress | `prompts/` |
| Evaluation dataset | Implemented | `evals/datasets/support_questions.jsonl` |
| Foundry evaluations | Planned | `wiki/plans/005-evaluation-automation-plan.md` |
| Monitoring dashboard | In Progress | `frontend/src/pages/MonitoringPage.tsx` |
| Tracing dashboard | In Progress | `frontend/src/pages/TracesPage.tsx` |
| Learning path mapping | Implemented | `wiki/learning-path/README.md` |
