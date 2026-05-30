# Promotion Criteria

Use this checklist when deciding whether a skill should move into the configured shared skill repository.

## Score First

Before promotion, score the skill across five dimensions. Use `0-5` for each:

- `0`: missing or actively harmful
- `1`: very weak
- `2`: incomplete
- `3`: acceptable
- `4`: strong
- `5`: clear and reusable by default

Dimensions:

- Entry problem clarity
- Trigger uniqueness
- Reuse and sanitization readiness
- Packaging and installation readiness
- Context efficiency

Threshold guidance:

- `22-25`: promote-ready if no hidden private constraints remain
- `17-21`: reusable but needs refinement before promotion
- `12-16`: split or keep local first
- `0-11`: do not promote; merge, narrow, or redesign

For a more detailed rubric, read `skill-scorecard.md`.

## Promote

Promote a skill when most of these are true and the score is usually `22+`:

- It solves a recurring class of tasks, not one project issue.
- It can be explained without private project context.
- It has stable trigger wording a future agent can recognize.
- It improves correctness, repeatability, architecture discipline, or delivery workflow.
- It can be reused by Codex, Claude Code, or other AI tools.
- Its examples can be sanitized or generalized.
- Its bundled scripts or references are safe to publish to the target Git repository.

## Keep Project-Local

Keep a skill local when any of these dominate or the score stays around `12-16`:

- It depends on one repository's private architecture, secrets, customer data, or undocumented deployment environment.
- It contains machine-specific paths that are not part of the intended workflow.
- It is a temporary workaround.
- It mainly captures product decisions for one project.
- It would confuse agents outside the original project.

## Split

Split the skill when the score is dragged down by mixed concerns, especially weak trigger uniqueness or reuse readiness:

- The workflow is generic but examples are private.
- The trigger is generic but the scripts are project-specific.
- The skill mixes governance policy with one repo's implementation details.

Recommended split:

```text
shared skill repo:
  generic workflow
  reusable scripts
  sanitized examples

project repo:
  project-specific docs
  private paths
  local commands
  sensitive context
```

## Required Cleanup Before Promotion

- Remove full API keys, tokens, private URLs, and personal account details.
- Replace sensitive paths with placeholders unless the path is intentionally part of a local workflow.
- Convert project-specific nouns into role-based nouns when possible.
- Put trigger scenarios in `description`.
- Keep `SKILL.md` short enough to load cheaply.
- Move long details into one-level `references/` files.
- Re-score after cleanup to confirm the skill actually improved rather than only moved files around.
