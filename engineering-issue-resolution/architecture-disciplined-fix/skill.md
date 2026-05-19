---
name: architecture-disciplined-fix
description: Architecture-safe fixing workflow after root cause confirmation.
---

# Architecture-Disciplined Fix

## Goal

Implement fixes safely and consistently with system architecture.

Focus:
- correct modification boundary
- lifecycle consistency
- dataflow integrity
- avoiding local patches

---

# Required Inputs

Prefer:
- root-cause-report
- instrumentation data
- lifecycle understanding
- affected modules

If root cause is unclear:
return to structured-debugging.

---

# Rules

## Fix The Source

Prefer:
- correcting ownership
- stabilizing state flow
- fixing lifecycle ordering

Avoid:
- scattered conditionals
- duplicated state
- hidden synchronization hacks

---

## Respect Boundaries

Evaluate:
- ownership
- lifecycle impact
- async ordering
- cache assumptions
- state consistency

---

## Prefer Simplification

If architecture itself causes instability:
- refactor may be preferable to patching

---

# Lifecycle Awareness

Maintain:

Lifecycle Impact

Document:
- where behavior begins
- propagation path
- synchronization points
- cleanup points

---

# Output

Produce:

fix-plan.md

Including:
- modification location
- lifecycle impact
- architecture reasoning
- risk analysis
- rejected alternatives
