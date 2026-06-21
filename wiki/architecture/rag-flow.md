# Grounding Flow

This project intentionally describes grounding as a Foundry Agent knowledge base / file search flow, not a custom index-first RAG implementation.

## Flow

```text
Question
  -> Agent instructions
  -> Knowledge base / file search
  -> Retrieved source content
  -> Agent response
  -> Citations and metadata
```

Azure AI Search remains important, but it is treated as backing infrastructure for the Foundry knowledge experience.
