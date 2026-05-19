# Git And Installation Flow

This reference describes the expected lifecycle after a skill is promoted into a shared, Git-backed skill repository.

## Source Of Truth

The configured shared skill repository is the source of truth. Resolve it from an explicit user-provided path, an environment variable, or the current Git workspace before editing.

```text
AI_TASK_DECOMPOSER_REPO=<path-to-shared-skill-repo>
SHARED_SKILL_REPO=<path-to-shared-skill-repo>
```

A promoted skill lives as a top-level folder:

```text
shared-skill-repo/
  skill-name/
    SKILL.md
```

## Git Publication

Before commit:

```powershell
git status --short --untracked-files=all
git diff --stat
```

Stage only relevant files:

```powershell
git add skill-name
git status --short
```

Commit with a focused message:

```powershell
git commit -m "Add skill-name skill"
```

Push using the repository's configured remote:

```powershell
git remote -v
git push
```

Do not push if unrelated user changes are present and mixed into the commit.

## cc-switch Installation

The exact cc-switch command is environment-specific. Do not guess flags.

Discovery commands:

```powershell
Get-Command cc-switch -ErrorAction SilentlyContinue
cc-switch --help
```

Look for commands that install or sync skills from a Git repository. The required inputs are usually:

- Git repository URL or local path.
- Skill folder name.
- Target tool profile.
- Destination tool, such as Codex or Claude Code.

If cc-switch is not installed or its syntax is unknown, provide this handoff:

```text
source_repo: <git remote or local path>
skill_name: <skill-name>
skill_path: <repo>/<skill-name>
target_tools: cc-switch, codex
validation: <commands run>
```

## Codex Direct Fallback

If the user explicitly wants direct Codex installation and cc-switch is unavailable, install the skill folder into the active Codex skills directory.

Common Windows destination:

```text
%USERPROFILE%\.codex\skills\<skill-name>
```

Prefer a Git-based install or sync when possible, so local copies can be updated cleanly.

## Post-Install Check

After installation, start a fresh agent/session or reload skills if the tool supports it. Confirm:

- The skill appears in the available skills list.
- The `description` triggers on realistic requests.
- The body instructions are enough without hidden project context.
