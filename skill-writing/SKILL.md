---
name: skill-writing
description: Write or refine Codex skills when a repository needs a new `SKILL.md` or an existing skill should become clearer, shorter, and more reliable. Use for drafting skill frontmatter, tightening trigger wording, simplifying structure, moving detail out of the main file, and making skills heuristic-first instead of template-heavy.
---

# Skill Writing

Write skills to be clear, short, and easy to trigger correctly.

## Use This Skill To
- create a new skill
- rewrite an overgrown `SKILL.md`
- sharpen a skill's trigger description
- merge overlapping skills
- move detail from `SKILL.md` into references
- turn a rigid checklist into a heuristic workflow

## Core Heuristics
1. Put trigger clarity first.
2. Keep the main file short; move depth to references only when needed.
3. Prefer decision rules over long explanations.
4. Prefer heuristics over exhaustive templates.
5. Make one skill own one entry problem.
6. If two skills compete for the same trigger, merge or narrow them.

## Write In This Order
1. Define the entry problem.
2. Write the frontmatter `description` so trigger conditions are explicit.
3. Keep the body to the minimum useful workflow.
4. Add references only for detail that would clutter the main file.
5. End with a short anti-pattern section if mistakes are likely.

## Frontmatter Rules
- Make `description` say both what the skill does and when it should trigger.
- Name concrete request shapes, not abstract intentions.
- Mention competing cases that should use another skill instead.
- Do not waste description space on philosophy or repetition.

## Body Shape
Use a compact structure by default:
1. `What To Use It For`
2. `Core Heuristics`
3. `Workflow` or `Decision Rules`
4. `Minimal Output` if the skill controls visible deliverables
5. `Anti-Patterns` when failure modes matter

Do not keep boilerplate sections that add no guidance.

## When To Split Into References
Move content out of `SKILL.md` when:
- it is mainly a checklist or field template
- it contains long examples
- it is useful only after the main decision is already made
- it makes the main file hard to scan

Keep in `SKILL.md` when:
- it affects triggering
- it changes the default workflow
- it prevents common misuse

## Review Checklist
- Is the trigger description concrete and narrow enough?
- Can another agent understand the entry problem in under 30 seconds?
- Is the main file mostly workflow and heuristics, not explanation?
- Are repeated details pushed into references?
- Would this skill still be understandable if half the sections were removed?

## Anti-Patterns
- writing a skill like user documentation
- keeping broad trigger wording that collides with another skill
- copying the init template structure without pruning it
- putting every checklist into the main file
- explaining too much instead of giving usable heuristics
