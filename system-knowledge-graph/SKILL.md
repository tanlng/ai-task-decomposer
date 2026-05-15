---
name: system-knowledge-graph
description: Maintain cross-document consistency, lifecycle knowledge, runtime flow relationships, and architecture dependency updates when system behavior changes.
tools:
  - read_file
  - search_code
  - grep
  - run_terminal_cmd
---

# Purpose

Maintain consistency between architecture knowledge documents.

This skill tracks:
- lifecycle documents
- runtime flows
- call chains
- event propagation
- state transitions
- cross-document dependencies

Goal:
Prevent architecture knowledge drift.

---

# When To Use

Use when:
- modifying existing call chains
- changing lifecycle stages
- changing event flow
- changing async behavior
- modifying state transitions
- changing cache/storage behavior
- modifying rendering/input/loading flows

Typical examples:
- mouse selection flow
- loading lifecycle
- render lifecycle
- async task scheduling
- event propagation
- connection lifecycle

---

# Core Responsibilities

## 1. Dependency Detection

Identify related documents affected by code changes.

Examples:

Mouse selection flow change
may impact:
- loading lifecycle
- selection lifecycle
- render lifecycle
- runtime cases
- ADR documents

---

## 2. Lifecycle Maintenance

Maintain lifecycle-level documentation.

Examples:
- loading stages
- render stages
- selection stages
- async stages
- cache lifecycle

For each lifecycle:
- stage order
- trigger conditions
- state changes
- side effects
- async boundaries
- cleanup logic

must remain synchronized.

---

## 3. Cross-Document Synchronization

When behavior changes:
- update related call chain docs
- update lifecycle docs
- update runtime cases
- update ADR if architectural intent changed

Prevent:
- outdated flow docs
- inconsistent lifecycle descriptions
- broken architecture references

---

## 4. Runtime Relationship Tracking

Track:
- event propagation
- state dependencies
- async chains
- cache invalidation
- rendering dependencies
- object activation flow

Focus on:
actual runtime relationships.

---

# Quality Rules

FORBIDDEN:
- isolated document updates
- partial lifecycle updates
- fake dependency assumptions

REQUIRED:
- trace actual relationships
- update impacted documents together
- preserve lifecycle consistency

If uncertain:
output:
UNKNOWN
or:
TO_BE_CONFIRMED

Never fabricate dependencies.

---

# Completion Rule

A change is NOT fully documented unless:
- impacted lifecycle docs are updated
- affected call chains are synchronized
- runtime behavior remains traceable
- cross-document consistency is preserved

Missing synchronization =
Knowledge Drift