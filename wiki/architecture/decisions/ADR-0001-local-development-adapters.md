# ADR-0001: Local Development Adapters

## Status

Accepted

## Context

The portfolio target depends on Azure resources, but development should not block on cloud setup.

## Decision

Use local adapters for agent responses and knowledge search while preserving the same API shape expected from the Foundry-backed implementation.

## Consequences

The app can run and test locally. The code must keep provider boundaries clear so local behavior does not become the final architecture by accident.
