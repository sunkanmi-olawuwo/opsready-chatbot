# 001 Foundry Agents Knowledge Base Foundation

## Goal

Build the app around Microsoft Foundry Agents and knowledge base / file search grounding.

## Scope

- Agent provider abstraction
- Local mock agent
- Future Foundry Agent client
- Knowledge provider abstraction
- Local markdown knowledge source
- Future Azure Blob Storage + Foundry knowledge base path
- Citation and operational metadata contract

## Acceptance Criteria

- `/api/chat` returns answer, citations, metadata, and trace ID
- `/api/knowledge/sources` lists local source documents
- Documentation names knowledge base/file search as the target grounding model
