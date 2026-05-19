---
name: generic-skill-governance
description: 通用 Skill 治理、抽取、发布与安装流程。Use when Codex needs to decide whether a project-local or ad-hoc skill should become a reusable general capability; create or refactor a skill into a configured shared skill repository; prepare it for Git publication; or install/sync that Git-hosted skill through cc-switch and onward into Codex, Claude Code, or other AI tools.
---

# Generic Skill Governance

## Purpose

Use this skill to promote useful project-local skills into a shared, Git-backed skill repository and make them installable across AI tools.

Resolve the shared skill repository before editing. Prefer an explicit user-provided path. Otherwise look for a current Git workspace that is clearly the shared skill repository, or ask for the path.

Common environment variable names teams may use:

```text
AI_TASK_DECOMPOSER_REPO
SHARED_SKILL_REPO
```

## Decision First

Before moving any skill, classify it:

- Keep local: project-specific workflow, secrets, repo-only paths, one-off process.
- Promote to shared repo: reusable across projects, stable trigger words, no private implementation details, useful for multiple AI tools.
- Split: generic workflow goes to shared repo; project-specific examples stay in the project.

For detailed criteria, read `references/promotion-criteria.md`.

## Promotion Workflow

1. Identify the candidate skill and its current location.
2. Remove project-only assumptions, secrets, machine-specific paths, and private examples.
3. Choose a lowercase hyphen-case skill name under 64 characters.
4. Create or update a top-level folder in the shared skill repository:

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

5. Put trigger conditions in `SKILL.md` frontmatter `description`, not only in the body.
6. Keep `SKILL.md` concise. Move long policy, examples, or tool-specific installation details into `references/`.
7. Add or update `agents/openai.yaml` when the skill should be visible in tool UIs.
8. Validate structure and content.
9. Commit and push through Git.
10. Install from the Git repository through cc-switch, then sync to Codex or other target tools.

For the Git and installation handoff, read `references/git-and-install-flow.md`.

## Skill Content Rules

Every promoted skill must have:

- `SKILL.md` with only `name` and `description` in YAML frontmatter.
- A clear workflow in the body.
- Explicit trigger wording in `description`.
- No full API keys, credentials, private tokens, or customer secrets.
- No project-only paths unless the skill is explicitly a project-governance skill.

Prefer:

- Short decision trees.
- Concrete examples.
- One-level references.
- Scripts only for deterministic repeated operations.

Avoid:

- Long README-style background.
- Changelogs, installation essays, or duplicate docs inside the skill folder.
- Vague descriptions like “helps with architecture” without trigger scenarios.

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
