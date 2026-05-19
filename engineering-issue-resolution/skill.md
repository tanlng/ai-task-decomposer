---
name: engineering-issue-resolution
description: Orchestrates structured debugging, architecture-safe fixing, and verification workflows for complex engineering issues.
---

# Engineering Issue Resolution

## When To Use

Use when:
- root cause is unclear
- the system is complex
- lifecycle/dataflow consistency matters
- multiple subsystems interact
- regressions are expensive
- observability is required

Examples:
- WebRTC packetsLost
- rendering anomalies
- async deadlocks
- cache inconsistencies
- lifecycle desynchronization
- performance regressions
- distributed/network/storage anomalies

---

# Workflow

## Phase 1 — Structured Debugging

If:
- root cause is unclear
- symptoms are inconsistent
- multiple hypotheses exist
- observability is insufficient

Then:
-> load structured-debugging

Output:
- root-cause-report.md

---

## Phase 2 — Architecture-Disciplined Fix

If:
- root cause is sufficiently validated
- affected systems are identified

Then:
-> load architecture-disciplined-fix

Output:
- fix-plan.md

---

## Phase 3 — Verification & Regression

If:
- modification completed
- regression/performance/stability validation required

Then:
-> load verification-regression

Output:
- verification-report.md

---

# Global Principles

- Never patch blindly
- One hypothesis at a time
- Evidence over intuition
- Preserve observability
- Prefer systemic understanding
- Maintain elimination chains
- Respect lifecycle and dataflow boundaries
