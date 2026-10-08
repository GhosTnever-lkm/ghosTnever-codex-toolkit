---
name: archive-hardening
description: Reviews archive ingestion and extraction for traversal, duplicate entries, symlinks, and resource exhaustion. Use for ZIP, TAR, mod, or backup archives.
---
# Archive Hardening

Treat archive names and metadata as attacker-controlled. Inspect before extraction and read the platform's path semantics.

## Threat checks
- Absolute paths, drive prefixes, UNC paths, `..`, alternate separators, and normalization collisions.
- Symlinks or hard links that escape the extraction root.
- Duplicate names, case-folding collisions, and ambiguous directory entries.
- Entry count, total expanded bytes, per-file size, compression ratio, and recursion limits.
- Partial writes, permissions, overwrite behavior, and cleanup after failure.

Resolve normalized targets and prove they remain under a dedicated extraction directory. Avoid extracting before validation; report limits and tested archive cases.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `archive-hardening`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
