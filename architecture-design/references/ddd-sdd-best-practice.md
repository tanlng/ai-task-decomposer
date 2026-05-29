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

## 3. Required Flow and Gates

### MVP evolution

#### Step 1. Baseline
- `Requirement Intake & Triage`
- `MVP / Idea Baseline`
- `PRD Baseline`
- Gate: do not enter planning or coding before these exist

#### Step 2. Planning
- `Global Architecture Charter / SDD`
- `Capability Roadmap`
- `Iteration Plan`
- Gate: do not enter capability implementation before roadmap and iteration plan exist

#### Step 3. Current Iteration
- `Current Capability Design Packet`
- `Current Iteration Contract`
- `ADR` when needed
- Gate: do not code before current capability packet and current iteration contract exist

#### Step 4. Implementation & Freeze
- code implementation
- `Iteration Freeze & Resume Note`
- Gate: do not claim the iteration is complete until freeze note is updated

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

## 6. Persistence Rule

For `MVP evolution`, do not leave the artifacts only in chat.

Prefer existing project documentation conventions first.
If none exist, write to:
- `docs/architecture/mvp-baseline.md`
- `docs/architecture/iteration-plan.md`
- `docs/architecture/capabilities/<capability-slug>.md`
- `docs/architecture/freeze-notes.md`
- `docs/architecture/adr/<adr-slug>.md`

For a single capability implementation round, at minimum update:
- MVP baseline
- iteration plan
- current capability document
- freeze notes

## 7. Execution Markers

When the skill triggers, always expose:
- skill marker: `using architecture-design`
- current step
- visible checkpoint before coding
- written document paths
- resume marker when continuing from an existing freeze point

If the user asks where the split-work documents are and `Capability Roadmap` or `Iteration Plan` is missing:
- state that Step 2 is incomplete
- do not present the work as a valid MVP-implementation pass
- return to planning artifacts first

## 8. Anti-Patterns

- skipping patch/MVP triage
- roadmap without iteration plan
- coding MVP evolution work without a current capability packet
- accepting temporary nodes without recovery planning
- treating PRD, SDD, and DDD as unrelated parallel documents
- keeping architecture artifacts only in chat without writing project documents
- explaining missing planning artifacts as “this round forgot them” after coding already happened
