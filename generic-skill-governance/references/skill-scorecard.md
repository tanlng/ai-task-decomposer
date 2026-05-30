# Skill Scorecard

Use this rubric when deciding whether a skill should stay independent, merge, split, stay local, or be promoted to a shared repository.

Score each dimension from `0` to `5`.

## 1. Entry Problem Clarity

- `5`: one clear entry problem; future agents can tell in one sentence when to use it
- `4`: mostly clear; minor ambiguity remains
- `3`: understandable, but examples or wording are still broader than ideal
- `2`: multiple problems are mixed together
- `1`: the skill mostly describes output style, not an entry problem
- `0`: no stable ownership boundary

## 2. Trigger Uniqueness

- `5`: trigger wording is concrete and does not compete with nearby skills
- `4`: rare overlap, easy to resolve
- `3`: some overlap, but acceptable with a short "not this skill" rule
- `2`: frequent overlap with another skill
- `1`: trigger is broad and selection is unreliable
- `0`: the same user request could reasonably trigger several skills every time

## 3. Reuse And Sanitization Readiness

- `5`: reusable across projects with no private context
- `4`: reusable after light noun cleanup
- `3`: reusable, but still carries some local assumptions
- `2`: several private examples or repo-only assumptions remain
- `1`: mostly project-specific
- `0`: cannot be shared safely

## 4. Packaging And Installation Readiness

- `5`: folder structure, naming, references, and UI metadata are ready
- `4`: small cleanup remains
- `3`: usable, but missing one supporting piece such as references or agent metadata
- `2`: structure is inconsistent or unclear
- `1`: the skill is still an ad-hoc draft
- `0`: not packageable yet

## 5. Context Efficiency

- `5`: concise, easy to load, and only expands when needed
- `4`: slightly verbose but still efficient
- `3`: acceptable, though the main file could be leaner
- `2`: too much policy or background lives in the main file
- `1`: expensive to load and hard to scan
- `0`: unusable within normal context budgets

## Decision Bands

- `22-25`: keep as an independent reusable skill; promote if the workflow has cross-project value
- `17-21`: keep the skill, but rewrite or narrow before promotion
- `12-16`: split or keep local first
- `0-11`: merge, retire, or redesign

## How To Use The Score

- Use the total score to guide the decision, not replace judgment.
- Call out the lowest one or two dimensions first; they usually indicate the real fix.
- Re-score after major edits. Improvement matters more than the first number.
- If the score is high but the trigger still overlaps with another skill, merge or narrow anyway.
