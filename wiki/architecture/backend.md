# Backend Architecture

The backend is a FastAPI orchestration layer.

Primary responsibilities:

- expose stable API contracts
- call agent providers
- expose knowledge source metadata
- load prompt versions
- provide evaluation, telemetry, and trace endpoints
- isolate local development adapters from Azure providers

Provider interfaces are expected for agent execution, knowledge grounding, evaluation, and telemetry.
