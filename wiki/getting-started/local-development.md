# Local Development

The local environment runs without Azure credentials.

## Backend

```bash
cd backend
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Use Python 3.11-3.13 for now. The default `python3` on this machine may point at Python 3.14, which is newer than some pinned backend package wheels.

## Frontend

```bash
cd frontend
pnpm install
pnpm run dev
```

## Local Providers

- `AGENT_PROVIDER=local`
- `KNOWLEDGE_PROVIDER=local`

The local providers are development adapters for the target Microsoft Foundry Agent and knowledge base implementation.

## Tests

```bash
cd backend
.venv/bin/python -m pytest
```

```bash
cd frontend
pnpm run test
```
