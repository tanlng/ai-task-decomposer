import argparse
import os
from pathlib import Path
from pathlib import PureWindowsPath


def ps_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def load_public_key(public_key_file: str | None) -> tuple[str | None, str | None]:
    if not public_key_file:
        return None, None

    path = Path(os.path.expandvars(public_key_file)).expanduser()
    if not path.exists():
        return None, str(path)

    return path.read_text(encoding="utf-8").strip(), str(path)


def build_commands(
    local_user: str,
    remote_user: str,
    host: str,
    key_path: str,
    remote_home: str,
    public_key: str | None,
    public_key_file: str | None,
) -> str:
    pub_path = f"{key_path}.pub"
    remote_ssh = str(PureWindowsPath(remote_home) / ".ssh")
    remote_auth = str(PureWindowsPath(remote_ssh) / "authorized_keys")
    admin_auth = str(PureWindowsPath(r"C:\ProgramData\ssh") / "administrators_authorized_keys")

    key_path_q = ps_single_quote(key_path)
    pub_path_q = ps_single_quote(pub_path)
    remote_ssh_q = ps_single_quote(remote_ssh)
    remote_auth_q = ps_single_quote(remote_auth)
    admin_auth_q = ps_single_quote(admin_auth)

    lines = []
    lines.append("Local machine commands")
    lines.append("")
    lines.append("```powershell")
    lines.append(f"ssh-keygen -t ed25519 -C {ps_single_quote(f'{local_user}@local')} -f {key_path_q}")
    lines.append(f"Get-Content {pub_path_q}")
    lines.append("```")
    lines.append("")
    lines.append("Commands to run on the target machine")
    lines.append("")
    lines.append("```powershell")
    lines.append("$sshdConfig = 'C:\\ProgramData\\ssh\\sshd_config'")
    lines.append(f"$sshDir = {remote_ssh_q}")
    lines.append(f"$userAuthFile = {remote_auth_q}")
    lines.append(f"$adminAuthFile = {admin_auth_q}")
    lines.append("$isAdmin = [bool](whoami /groups | Select-String 'S-1-5-32-544')")
    lines.append("$adminOverride = $false")
    lines.append("if (Test-Path $sshdConfig) {")
    lines.append("  $configLines = Get-Content $sshdConfig")
    lines.append("  $hasAdminMatch = [bool]($configLines | Where-Object { $_ -match '^\\s*Match\\s+Group\\s+administrators\\b' })")
    lines.append("  $hasAdminAuthFile = [bool]($configLines | Where-Object { $_ -match '^\\s*AuthorizedKeysFile\\s+__PROGRAMDATA__/ssh/administrators_authorized_keys\\b' })")
    lines.append("  $adminOverride = $hasAdminMatch -and $hasAdminAuthFile")
    lines.append("}")
    lines.append("$authFile = if ($isAdmin -and $adminOverride) { $adminAuthFile } else { $userAuthFile }")
    lines.append("Write-Output \"Using auth file: $authFile\"")
    lines.append("if (Test-Path $sshdConfig) { Get-Content $sshdConfig | Select-String -Pattern 'AuthorizedKeysFile|Match Group administrators|PubkeyAuthentication|PasswordAuthentication' }")
    lines.append("New-Item -ItemType Directory -Force -Path $sshDir | Out-Null")
    lines.append("if (-not (Test-Path $authFile)) { New-Item -ItemType File -Force -Path $authFile | Out-Null }")
    lines.append("$backup = \"$authFile.bak-$(Get-Date -Format yyyyMMdd-HHmmss)\"")
    lines.append("Copy-Item -LiteralPath $authFile -Destination $backup -Force")
    if public_key:
        lines.append(f"$pubKey = {ps_single_quote(public_key)}")
    else:
        lines.append("$pubKey = '<paste-public-key-here>'")
    lines.append("$existing = [System.IO.File]::ReadAllText($authFile, [System.Text.Encoding]::ASCII)")
    lines.append("$normalized = $existing -replace \"`r`n\", \"`n\" -replace \"`r\", \"`n\"")
    lines.append("$lines = if ([string]::IsNullOrWhiteSpace($normalized)) { @() } else { $normalized.TrimEnd(\"`n\").Split(\"`n\") }")
    lines.append("if ($pubKey -ne '<paste-public-key-here>' -and $lines -notcontains $pubKey) {")
    lines.append("  if ($existing.Length -gt 0 -and -not ($existing.EndsWith(\"`r`n\") -or $existing.EndsWith(\"`n\") -or $existing.EndsWith(\"`r\"))) {")
    lines.append("    [System.IO.File]::AppendAllText($authFile, \"`r`n\", [System.Text.Encoding]::ASCII)")
    lines.append("  }")
    lines.append("  [System.IO.File]::AppendAllText($authFile, $pubKey + \"`r`n\", [System.Text.Encoding]::ASCII)")
    lines.append("}")
    lines.append("Get-Content $authFile")
    lines.append("```")
    lines.append("")
    if public_key_file and public_key:
        lines.append(f"Embedded public key source: `{public_key_file}`")
    else:
        lines.append("Replace `<paste-public-key-here>` with the full contents of the local `.pub` file before running the target-machine block.")
    lines.append("")
    lines.append("Verification commands")
    lines.append("")
    lines.append("```powershell")
    lines.append(f'ssh {remote_user}@{host} "whoami"')
    lines.append(f'ssh -v {remote_user}@{host} "whoami"')
    lines.append("```")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Windows PowerShell SSH key setup commands for a Windows target host."
    )
    parser.add_argument(
        "--local-user",
        default=os.environ.get("USERNAME", "local-user"),
        help="Local Windows username used for the SSH key comment.",
    )
    parser.add_argument("--remote-user", required=True, help="Remote SSH username.")
    parser.add_argument("--host", required=True, help="Remote host or IP.")
    parser.add_argument(
        "--key-path",
        default=r"$env:USERPROFILE\.ssh\id_ed25519",
        help=r"PowerShell key path expression. Default: $env:USERPROFILE\.ssh\id_ed25519",
    )
    parser.add_argument(
        "--public-key-file",
        default=str(Path.home() / ".ssh" / "id_ed25519.pub"),
        help=r"Local public key file to embed in the target-machine command block when it exists.",
    )
    parser.add_argument(
        "--remote-home",
        help=r"Remote user home path. Default: C:\Users\<remote_user>",
    )
    args = parser.parse_args()

    remote_home = args.remote_home or str(PureWindowsPath(r"C:\Users") / args.remote_user)
    public_key, public_key_file = load_public_key(args.public_key_file)
    print(
        build_commands(
            args.local_user,
            args.remote_user,
            args.host,
            args.key_path,
            remote_home,
            public_key,
            public_key_file,
        )
    )


if __name__ == "__main__":
    main()
