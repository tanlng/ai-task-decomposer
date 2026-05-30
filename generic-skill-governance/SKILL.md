---
name: generic-skill-governance
description: 通用 Skill 治理、评分与编写流程。Use when Codex needs to score, create, rewrite, merge, split, promote, publish, or install a reusable skill, especially when skill boundaries are unclear, triggers overlap, or a `SKILL.md` needs to be rewritten into a concise heuristic-first form.
---

# Generic Skill Governance

Use this skill to score, shape, and publish reusable skills.

Use it to:

- decide whether a skill should exist, merge, split, stay local, or become shared
- rewrite `SKILL.md` so the trigger and workflow are clear
- prepare a reusable skill for Git publication and installation across AI tools

Resolve the shared skill repository before editing. Prefer a user-provided path. Otherwise look for a clear shared skill repo first. Common env names: `AI_TASK_DECOMPOSER_REPO`, `SHARED_SKILL_REPO`.

## Quick Score

Score the candidate before deciding whether to keep, merge, split, or promote it:

- Entry problem clarity: `0-5`
- Trigger uniqueness: `0-5`
- Reuse and sanitization readiness: `0-5`
- Packaging and installation readiness: `0-5`
- Context efficiency: `0-5`

Decision thresholds:

- `22-25`: keep as an independent reusable skill; promote if cross-project value exists
- `17-21`: promising, but rewrite or narrow before promotion
- `12-16`: keep local for now, or split generic and project-specific parts
- `0-11`: merge, retire, or redesign because the skill boundary is weak

Read `references/skill-scorecard.md` for the full rubric and `references/promotion-criteria.md` for promotion rules.

## Governance Workflow

1. Identify the candidate skill or the overlapping skill pair and its current location.
2. Score it using the quick score and confirm the weakest dimensions.
3. Decide the ownership boundary first:
   - Overlap: pick one owner for one entry problem, then merge or narrow the others.
   - Reusable: decide whether it stays local or is promoted.
4. Rewrite the surviving `SKILL.md` so its frontmatter and workflow match that ownership boundary.
5. Remove project-only assumptions, secrets, machine-specific paths, and private examples from any skill that will become shared.
6. Choose a lowercase hyphen-case skill name under 64 characters.
7. Create or update a top-level folder in the shared skill repository:

```text
shared-skill-repo/
  skill-name/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
    assets/
```

Only create resource folders that are actually needed.

8. Put trigger conditions in `SKILL.md` frontmatter `description`, not only in the body.
9. Keep `SKILL.md` concise. Move long policy, examples, or tool-specific installation details into `references/`.
10. Add or update `agents/openai.yaml` when the skill should be visible in tool UIs.
11. Validate structure, score, and content, then re-score after meaningful edits.
12. Commit and push through Git.
13. Install from the Git repository through cc-switch, then sync to Codex or other target tools.

Read `references/git-and-install-flow.md` for the Git and install handoff.

## Heuristics

Every reusable skill should have:

- `SKILL.md` with only `name` and `description` in YAML frontmatter.
- A clear workflow in the body.
- Explicit trigger wording in `description`.
- No full API keys, credentials, private tokens, or customer secrets.
- No project-only paths unless the skill is explicitly a project-governance skill.

Prefer:

- Trigger clarity first.
- Short decision trees.
- Concrete examples.
- One-level references.
- Scripts only for deterministic repeated operations.
- One entry problem per skill.
- Heuristic workflows over long templates.

Avoid:

- Long README-style background.
- Changelogs, installation essays, or duplicate docs inside the skill folder.
- Vague descriptions like “helps with architecture” without trigger scenarios.
- Two skills competing for the same entry problem.

## `SKILL.md` Writing Rules

When the skill already has the right owner and only its content needs work:

- Make `description` say both what the skill does and when it should trigger.
- Name concrete request shapes, not abstract intentions.
- Mention competing cases that should use another skill instead.
- Keep the body to the minimum useful workflow.
- Move long examples and checklists into `references/` when they are not needed for triggering.

Use this compact body shape by default:

1. `What To Use It For`
2. `Core Heuristics`
3. `Workflow` or `Decision Rules`
4. `Minimal Output` when the skill controls visible deliverables
5. `Anti-Patterns` when misuse is likely

## Validation And Handoff

When editing the shared skill repo:

```powershell
git status --short --untracked-files=all
```

Review existing skill naming and structure before adding a new folder. Do not overwrite unrelated local changes.

After edits:

```powershell
git diff --stat
git status --short --untracked-files=all
```

If asked to publish, stage only relevant files and create a focused commit. Do not invent `cc-switch` commands; check local help first:

```powershell
Get-Command cc-switch -ErrorAction SilentlyContinue
cc-switch --help
```

If `cc-switch` is unavailable or unclear, provide a handoff with:

- Git repository URL or local repo path.
- Skill folder name.
- Target tools: cc-switch, Codex, Claude Code, or others.
- Files changed.
- Validation performed.

Validate at three levels:

1. Structure: required `SKILL.md`, valid frontmatter, sensible folder name.
2. Trigger: `description` says exactly when to use the skill.
3. Reuse: no hidden project context is required to apply the skill elsewhere.

If the repository provides `scripts/evaluate_skills.py`, run it and use the score as a supporting signal, not the only decision maker.

If Python validation tooling is available, run the skill validator. If it fails because dependencies such as PyYAML are missing, report that and still manually inspect the frontmatter.

When done, report:

- Skill name and path.
- Quick score and weakest dimensions.
- Why it is generic or why it stayed local.
- Files added or changed.
- Validation result.
- Git status or commit hash if published.
- Installation handoff for cc-switch and Codex.
