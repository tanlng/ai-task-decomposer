---
name: windows-ssh-key-setup
description: Generate Windows PowerShell commands for SSH key login setup between a local machine and a target Windows machine. Use when Codex needs to create a reusable SSH onboarding flow that includes local key generation, target-machine authorized_keys append commands, and verification commands for OpenSSH access.
---

# Windows SSH Key Setup

Generate commands instead of narrating the process. Prefer using the bundled script to emit a ready-to-run command set for the user's exact `local_user`, `remote_user`, `host`, and optional key path.

## Workflow

1. Confirm the scenario matches this skill:
   - Local machine uses Windows PowerShell.
   - Target machine is reachable by SSH.
   - Target account should accept key-based login through `authorized_keys`.
2. Run `scripts/generate_windows_ssh_setup.py` to produce the command set.
3. Return the output grouped as:
   - Local machine commands
   - Commands for the user to run on the target machine
   - Verification commands
4. If the user did not provide `remote_home`, default to `C:\Users\<remote_user>`.
5. If the user did not provide `key_path`, default to `$env:USERPROFILE\.ssh\id_ed25519`.
6. Always emit a target-side inspection step before any write step.
7. Never emit a write command that replaces the whole `authorized_keys` file with only one key.

## Command Requirements

Always include these command categories:

- Local key generation command
- Local public key inspection command
- Target-side inspection commands that show which auth file is likely effective
- Remote-side fallback commands that the user can run directly on the target machine
- Verification command
- Optional verbose verification command

## Output Rules

- Keep commands in PowerShell form unless the user asks for another shell.
- Use concrete paths and usernames in the emitted commands.
- Include a verification command that proves key login works.
- Include a verbose verification command when debugging is likely useful.
- Detect whether the effective auth file is the user profile file or `C:\ProgramData\ssh\administrators_authorized_keys` before generating the write step.
- Back up the target auth file before writing.
- Use explicit ASCII when writing key files on Windows OpenSSH.
- Append only after duplicate checking.
- If the user asks only for the commands, do not add long explanation around them.
- Do not generate a single-shot local command that pipes a key straight into the remote file unless the user explicitly asks for that style.

## Script

Use `scripts/generate_windows_ssh_setup.py` with arguments for the target values. The script prints a full command pack ready to share. If the local public key already exists, the script embeds it into the target-machine command block automatically.

Example:

```powershell
python "$env:USERPROFILE\.codex\skills\windows-ssh-key-setup\scripts\generate_windows_ssh_setup.py" `
  --local-user "Admin" `
  --remote-user "remote-user" `
  --host "192.168.51.55"
```
