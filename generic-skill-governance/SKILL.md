---
name: generic-skill-governance
description: 通用 Skill 治理与编写流程。Use when Codex needs to create, rewrite, merge, split, promote, publish, or install a reusable skill, especially when skill boundaries are unclear, triggers overlap, or a `SKILL.md` needs to be rewritten into a concise heuristic-first form.
---

# Generic Skill Governance

## Purpose

Use this skill to own the full lifecycle of a reusable skill:

- decide whether a skill should exist, merge, split, stay local, or become shared
- rewrite `SKILL.md` so the trigger and workflow are clear
- prepare the skill for Git publication and installation across AI tools

Resolve the shared skill repository before editing. Prefer an explicit user-provided path. Otherwise look for a current Git workspace that is clearly the shared skill repository, or ask for the path.

Common environment variable names teams may use:

```text
AI_TASK_DECOMPOSER_REPO
SHARED_SKILL_REPO
```

## Decision First

Before changing any skill, classify the problem:

- Keep as-is: the skill already owns one clear entry problem and only needs minor content edits.
- Keep local: project-specific workflow, secrets, repo-only paths, one-off process.
- Promote to shared repo: reusable across projects, stable trigger words, no private implementation details, useful for multiple AI tools.
- Split: generic workflow goes to shared repo; project-specific examples stay in the project.
- Merge or narrow: when two skills compete for the same trigger, assign one entry problem to one skill before editing content.

For detailed criteria, read `references/promotion-criteria.md`.

## Governance Workflow

1. Identify the candidate skill or the overlapping skill pair and its current location.
2. Decide the ownership boundary first:
   - If two skills overlap, decide which skill owns the entry problem and whether the other should narrow or merge.
   - If one skill is reusable, decide whether it stays local or is promoted.
3. Rewrite the surviving `SKILL.md` so its frontmatter and workflow match that ownership boundary.
4. Remove project-only assumptions, secrets, machine-specific paths, and private examples from any skill that will become shared.
5. Choose a lowercase hyphen-case skill name under 64 characters.
6. Create or update a top-level folder in the shared skill repository:

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

7. Put trigger conditions in `SKILL.md` frontmatter `description`, not only in the body.
8. Keep `SKILL.md` concise. Move long policy, examples, or tool-specific installation details into `references/`.
9. Add or update `agents/openai.yaml` when the skill should be visible in tool UIs.
10. Validate structure and content.
11. Commit and push through Git.
12. Install from the Git repository through cc-switch, then sync to Codex or other target tools.

For the Git and installation handoff, read `references/git-and-install-flow.md`.

## Skill Content Rules

Every promoted skill must have:

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

## Repository Rules

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

If asked to publish, stage only relevant files and create a focused commit.

## cc-switch And Tool Installation

Do not invent cc-switch commands. First check whether `cc-switch` is installed and inspect its local help or docs:

```powershell
Get-Command cc-switch -ErrorAction SilentlyContinue
cc-switch --help
```

If the command is unavailable or the install syntax is unclear, provide a handoff with:

- Git repository URL or local repo path.
- Skill folder name.
- Target tools: cc-switch, Codex, Claude Code, or others.
- Files changed.
- Validation performed.

For Codex direct fallback, a skill folder must ultimately be available under the active Codex skills directory. On Windows this is commonly:

```text
%USERPROFILE%\.codex\skills\skill-name
```

Prefer the user's cc-switch flow when available.

## Validation

Validate at three levels:

1. Structure: required `SKILL.md`, valid frontmatter, sensible folder name.
2. Trigger: `description` says exactly when to use the skill.
3. Reuse: no hidden project context is required to apply the skill elsewhere.

If Python validation tooling is available, run the skill validator. If it fails because dependencies such as PyYAML are missing, report that and still manually inspect the frontmatter.

## Final Report

When done, report:

- Skill name and path.
- Why it is generic or why it stayed local.
- Files added or changed.
- Validation result.
- Git status or commit hash if published.
- Installation handoff for cc-switch and Codex.
