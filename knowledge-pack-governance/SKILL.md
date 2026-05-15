---
name: knowledge-pack-governance
description: Generate maintainable system knowledge after implementation, debugging, refactor, or architecture changes. Produces PRD delta, architecture call chains, runtime cases, and ADR records.
tools:
  - read_file
  - search_code
  - grep
  - run_terminal_cmd
---

# Purpose

Convert implementation results into traceable engineering knowledge.

This skill complements:
- architecture-design
- prd-driven-development
- debugging
- refactor

It does NOT replace them.

---

# When To Use

Use AFTER:
- feature implementation
- bug fixing
- refactor
- architecture adjustment
- important runtime issue resolution

Use ONLY for:
- core business flows
- async/concurrency logic
- cache/storage/protocol flows
- risky or complex systems

Do NOT use for:
- trivial CRUD
- simple text changes
- framework boilerplate

---

# Required Outputs

## 1. PRD Delta

Describe:
- feature goal
- user-visible behavior
- inputs/outputs
- boundary conditions
- PRD deviations

Focus:
WHAT changed.

---

## 2. Architecture Call Chain

Document:
- entry points
- main call chain
- async/event flow
- cache/storage interaction
- state transitions
- lock/concurrency behavior

Must reach:
Class.Method

Example:

```text
UploadController.Upload
 -> UploadService.Process
 -> ObjectStorageClient.PutObject