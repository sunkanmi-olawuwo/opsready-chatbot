# ADR-0003: Foundry Knowledge Base Grounding

## Status

Accepted

## Context

The application should follow newer Microsoft Foundry Agents patterns instead of classic custom assistant or index-first RAG patterns.

## Decision

Use Microsoft Foundry Agents with knowledge base / file search grounding as the target architecture. Azure Blob Storage stores source documents, and Azure AI Search supports retrieval through the Foundry knowledge experience.

## Consequences

The project demonstrates modern Foundry agent operations. Backend abstractions should be named around agents and knowledge, not custom indexes.
