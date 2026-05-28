# Patch + MVP + PRD + SDD + DDD Quick Reference

## 1. Quick Triage

Use `patch` when:
- the change is local
- no capability decomposition is needed
- no multi-iteration planning is needed

Use `MVP evolution` when:
- the request validates or expands the core idea
- new or reordered capabilities are involved
- module boundaries, interfaces, data flow, state flow, or evolution direction may change
- the work will span multiple chats or iterations

## 2. Escalation Rules

Stay in PRD-only or lightweight `PRD -> SDD` when:
- the work is mainly product-rule clarification
- the change is about wording, protocol semantics, copy, or acceptance criteria
- no boundary, interface, data-flow, state-flow, or iteration-order impact exists

Escalate to full architecture flow when PRD changes affect:
- module boundaries
- interfaces
- data flow
- state flow
- iteration ordering
- performance or evolvability constraints

Enter DDD when:
- rule ownership is unclear
- bounded-context separation matters
- aggregates or anti-corruption boundaries affect replaceability

## 3. Required Flow

### MVP evolution
1. `Requirement Intake & Triage`
2. `MVP / Idea Baseline`
3. `PRD Baseline`
4. `Global Architecture Charter / SDD`
5. `Capability Roadmap`
6. `Iteration Plan`
7. `Current Capability Design Packet`
8. `Current Iteration Contract`
9. `ADR`
10. `Iteration Freeze & Resume Note`

### Patch / simple task
1. `Requirement Intake & Triage`
2. PRD check
3. lightweight SDD
4. DDD only when needed
5. implementation mapping

## 4. Node Rules

### Stable Node
- clear enough to continue development
- assumptions are stable enough
- valid as the preferred next start point

### Temporary Node
- temporarily accepted to move the current iteration forward
- not considered solved
- must be assigned to a later recovery iteration

## 5. Minimal Fields

### Requirement Intake & Triage
- request summary
- patch or MVP evolution
- judgment rationale

### MVP / Idea Baseline
- core idea
- value being validated
- MVP success criteria
- MVP scope / non-scope

### PRD Baseline
- target capability
- user/business rules
- inputs/outputs
- acceptance criteria
- final wording if prior PRD conflicted

### Global Architecture Charter / SDD
- system goal under MVP constraints
- capability map
- module boundaries
- main call chain or data flow

### Capability Roadmap
- capability name
- idea being validated
- MVP required or not
- dependencies
- recommended order
- DDD needed or not
- temporary-node risk

### Iteration Plan
- overall MVP goal
- first 2-3 iterations in detail
- later iterations in coarse form
- for each iteration:
  - goal
  - included capabilities
  - dependencies
  - expected increment
  - entry / exit condition
  - stable nodes
  - temporary nodes
  - recovery items
  - whether DDD happens here

### Current Capability Design Packet
- `MVP Alignment`
- `PRD Baseline for Capability`
- `SDD for Capability`
- `DDD Decision / Content`
- `Implementation Readiness`

### Current Iteration Contract
- iteration goal
- included MVP capabilities
- excluded work
- expected increment
- definition of done

### ADR
- decision topic
- chosen option
- rejected option
- why it fits the current MVP

### Iteration Freeze & Resume Note
- completed MVP capabilities
- frozen boundaries
- stable nodes ready to continue
- temporary nodes added
- recovery iteration for each temporary node
- recommended next capability

## 6. Execution Markers

When the skill triggers, always expose:
- skill marker: `using architecture-design`
- current step
- visible checkpoint before coding
- resume marker when continuing from an existing freeze point

## 7. Anti-Patterns

- skipping patch/MVP triage
- roadmap without iteration plan
- coding MVP evolution work without a current capability packet
- accepting temporary nodes without recovery planning
- treating PRD, SDD, and DDD as unrelated parallel documents
