# DDD + SDD Integration Best Practice

## Core Positioning

- PRD defines what the product must do.
- SDD defines how the system collaborates to realize that behavior.
- DDD defines where stable business rules and ownership belong.
- SDD is not a parallel skill. It is the first half of architecture-design.

## Decision Rule

Use only PRD when:
- the change is purely about user-visible rules or copy
- no module responsibility, interface, or data flow changes

Use PRD + lightweight SDD when:
- one module changes but interface, state flow, or non-functional constraints matter
- external API shape, storage schema, async flow, or error path needs design

Use PRD + SDD + DDD when:
- multiple modules collaborate
- business rules need clear ownership
- bounded contexts or aggregates may change
- external systems need anti-corruption boundaries
- the solution must stay replaceable or evolvable

## Recommended Workflow

1. Freeze the requirement baseline in PRD.
2. Produce SDD first.
3. Produce DDD only after SDD makes the system collaboration clear.
4. Map the design to concrete code owners, module paths, and tests.
5. Sync knowledge artifacts after implementation.

## SDD Minimum Checklist

- system goal and scope
- constraints and assumptions
- module responsibilities
- key call chain or sequence
- data flow and state transitions
- interface / protocol contracts
- failure path and fallback strategy
- observability and non-functional constraints

## DDD Minimum Checklist

- bounded contexts
- aggregate / entity ownership
- domain services and invariants
- domain events if needed
- anti-corruption boundaries
- which logic must not stay in UI / controller / infrastructure

## Output Template

1. Conclusion
2. Requirement and constraint summary
3. SDD
4. DDD
5. Implementation mapping
6. Risks and trade-offs

## Anti-Patterns

- jumping from PRD directly to code
- doing DDD before system responsibilities are clear
- using DDD terms to hide missing interface or data-flow design
- adding a separate SDD skill that duplicates architecture ownership
- documenting decisions only in chat without persistent knowledge artifacts
