# Backend

FastAPI backend for the GenAIOps Support Copilot.

The backend starts with local adapters for:

- agent execution
- knowledge search
- prompt loading
- telemetry placeholders

The target provider path is Microsoft Foundry Agents with knowledge base / file search grounding backed by Azure Blob Storage and Azure AI Search.

## Run

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Use Python 3.11-3.13. CI currently targets Python 3.11.

## Test

```bash
pytest
```
