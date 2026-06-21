# Data And Retrieval

The target data path is:

1. curated documentation lives in Azure Blob Storage
2. Foundry knowledge base / file search is configured over those documents
3. Azure AI Search supports retrieval behind the knowledge experience
4. Foundry Agents use retrieved content to answer questions with citations

The local path uses markdown files in `data/sample-docs` to keep development fast and testable.
