---
name: shell-scripting
description: Creates or reviews shell and PowerShell automation with safe quoting, predictable failures, and clear input handling. Use for scripts that automate files, processes, or builds.
---
# Shell Scripting

Use the repository's existing shell and supported OS. Read local instructions and test the script in a temporary workspace before touching important data.

## Practices
- Validate arguments, paths, and environment variables before mutation.
- Quote values; pass subprocess arguments as arrays instead of building command strings.
- Make failures visible with meaningful exit codes and actionable messages.
- Handle temporary files and cleanup explicitly; avoid broad recursive deletion.
- Keep scripts idempotent where practical and provide a dry-run for destructive actions.
- Test spaces, non-ASCII paths, missing inputs, and expected failure cases.

State platform assumptions and exact verification. Never run a destructive script against user data as a test.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `shell-scripting`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
