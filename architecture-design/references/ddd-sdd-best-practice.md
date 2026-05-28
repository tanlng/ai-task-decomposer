# Patch + MVP + PRD + SDD + DDD Iterative Architecture Best Practice

## Core Positioning

- Start by triaging the request: patch or MVP evolution.
- Refine the idea and the MVP before refining the full future architecture.
- Let PRD define what must happen.
- Let SDD define how the system collaborates to make it happen.
- Let DDD define where stable business rules and ownership belong.
- Keep SDD as the first half of `architecture-design`; do not split it into a parallel skill.
- Keep `Iteration Plan` as a separate layer between roadmap and current-iteration execution.

## Intake and Triage Rule

Classify the request first.

Treat it as a `patch` when:
- the change is local and bounded
- no MVP-capability decomposition is needed
- no multi-iteration architecture plan is required

Treat it as `MVP evolution` when:
- the change validates or expands the core idea
- new capabilities or reordered capabilities are involved
- responsibilities, interfaces, data flow, state flow, or evolution direction may change
- the work will span multiple chats or iterations

Default handling:
- patch -> PRD if needed, lightweight SDD, DDD only when required, then implementation mapping
- MVP evolution -> full iterative architecture chain

## Decision Rule

Use only PRD when:
- the change is purely about user-visible rules or copy
- no module responsibility, interface, or data-flow changes exist

Use PRD + lightweight SDD when:
- one module changes but interface, state flow, or non-functional constraints matter
- API shape, storage schema, async flow, or error path needs design

Use PRD + SDD + DDD when:
- multiple modules collaborate
- business rules need clear ownership
- bounded contexts or aggregates may change
- external systems need anti-corruption boundaries
- the solution must stay replaceable or evolvable

Treat the task as a large scheme when:
- multiple modules or services are involved
- the work will span multiple chats or iterations
- ordering affects boundaries, interfaces, or state flow
- jumping into implementation would likely create a "make it run first, redesign later" path

## MVP Gating Rule

Before detailed architecture design for MVP evolution:
- freeze the MVP goal
- define the idea being validated
- mark MVP scope and non-scope
- reject non-MVP capability expansion from the current iteration

If a capability does not pass MVP Alignment:
- keep it on the roadmap
- do not expand it into PRD/SDD/DDD for the current iteration

## Recommended Workflow for MVP Evolution

1. Produce `Requirement Intake & Triage`.
2. Freeze the `MVP / Idea Baseline`.
3. Produce the global `PRD Baseline`.
4. Produce the `Global Architecture Charter / SDD`.
5. Build the `Capability Roadmap`.
6. Produce the `Iteration Plan`.
7. Select the current iteration capability set.
8. Produce the `Current Capability Design Packet`:
   - MVP Alignment
   - PRD Baseline for Capability
   - SDD for Capability
   - DDD Decision / Content
   - Implementation Readiness
9. Produce the `Current Iteration Contract`.
10. Record ADRs for important trade-offs.
11. Close the iteration with `Iteration Freeze & Resume Note`.

## Node Status Model

### Stable Node

Use when:
- the boundary is clear enough to continue development
- inputs and assumptions are sufficiently stable
- the work can be resumed directly in a later chat

Must mean:
- safe to continue
- preferred next start point for "begin work" style requests

### Temporary Node

Use when:
- the current iteration must move forward before the area is fully settled
- the issue is accepted temporarily for MVP progress
- later cleanup or completion is required

Must mean:
- not solved yet
- must be scheduled in a later iteration
- must not be forgotten after the current chat

## Global Document Checklist

### Requirement Intake & Triage

- request summary
- patch or MVP evolution
- judgment rationale
- whether to enter the full iterative architecture chain

### MVP / Idea Baseline

- core idea
- value being validated now
- MVP success criteria
- MVP scope
- non-MVP scope
- what is explicitly deferred

### PRD Baseline

- target capability
- user/business rules
- inputs/outputs
- acceptance criteria
- boundary conditions
- relationship to the existing PRD

### Global Architecture Charter / SDD

- system goal under MVP constraints
- capability map
- module boundaries
- main call chain or data flow
- architecture spine that must not drift
- minimal extensibility reserved for later evolution
- intentionally deferred design areas

### Capability Roadmap

For each capability:
- capability name
- idea being validated
- MVP required or not
- dependencies
- affected boundaries
- recommended iteration order
- validation outcome after completion
- whether DDD is required
- whether temporary-node risk exists

### Iteration Plan

Must cover the whole MVP period while keeping different precision levels:
- overall MVP goal
- iteration overview
- first 2-3 iterations with precise planning
- later iterations with coarse planning and explicit note that further decomposition is needed

For each iteration include:
- iteration number
- iteration goal
- included capabilities
- dependencies
- expected increment
- entry condition
- exit condition
- stable nodes
- temporary nodes
- follow-up recovery items
- whether DDD is expected in this iteration

## Current Iteration Artifacts Checklist

### Current Capability Design Packet

#### MVP Alignment

- idea being validated
- why it is MVP-critical
- impact if delayed
- related extensions excluded from this iteration

#### PRD Baseline for Capability

- module goal
- user/business rules
- inputs/outputs
- acceptance criteria
- boundary conditions

#### SDD for Capability

- responsibilities
- collaborating modules
- call chain / sequence
- data flow / state transitions
- interfaces / protocol contracts
- failure path and fallback
- observability and non-functional constraints

#### DDD Decision / Content

- whether DDD is required
- if yes: contexts, aggregates/entities, domain services, invariants, events, anti-corruption boundaries
- if no: why ownership and rule placement remain simple enough without DDD expansion

#### Implementation Readiness

- code/module landing points
- owner
- extension points
- tests
- release impact
- open questions

### Current Iteration Contract

- iteration goal
- MVP capabilities included
- non-MVP work excluded
- inputs
- expected increment
- definition of done
- validation method

### ADR

- decision topic
- alternatives considered
- chosen option
- why it fits current MVP
- deferred option
- upgrade/reopen condition

### Iteration Freeze & Resume Note

- MVP capabilities completed
- boundaries frozen this round
- ideas validated / unvalidated
- stable nodes ready to continue
- temporary nodes added this round
- iteration in which each temporary node must be recovered
- impact if recovery is skipped
- recommended next capability
- assumptions to recheck before resuming
- conditions that require reopening the MVP baseline or global charter

## DDD Timing Rule

Do not assume DDD must be completed globally upfront.

Prefer:
- global PRD and SDD first
- DDD during the first architecture-heavy iteration or the first core capability iteration
- explicit marking in `Iteration Plan` of which iteration will complete DDD

Escalate to DDD when:
- rule ownership is unclear
- bounded-context separation matters
- aggregates or anti-corruption boundaries affect replaceability

## Output Template

1. Conclusion
2. Requirement Intake & Triage
3. MVP / Idea Baseline
4. PRD Baseline
5. Global Architecture Charter / SDD
6. Capability Roadmap
7. Iteration Plan
8. Current Capability Design Packet
9. Current Iteration Contract
10. ADRs
11. Iteration Freeze & Resume Note
12. Risks and next iteration advice

Inside `Current Capability Design Packet`, always keep:
1. MVP Alignment
2. PRD Baseline
3. SDD
4. DDD Decision / Content
5. Implementation Readiness

## Anti-Patterns

- skipping patch/MVP triage and jumping straight into design
- designing the full future system before freezing the MVP
- having a roadmap without a separate iteration plan
- expanding non-MVP capabilities inside the current iteration
- accepting temporary nodes without scheduling recovery iterations
- doing DDD before SDD makes collaboration clear
- using DDD terms to hide missing interface or data-flow design
- writing PRD, SDD, and DDD as unrelated parallel documents
- documenting decisions only in chat without iteration and resume artifacts
