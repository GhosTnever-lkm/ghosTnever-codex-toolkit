---
name: conflict-resolution
description: Resolves Git merge or rebase conflicts while preserving intent from both sides. Use when a repository contains unresolved conflict markers or an operation is paused.
---
# Conflict Resolution

Read repository instructions, conflict status, base commit, and both sides of each conflict. Do not choose ours or theirs wholesale without understanding the semantic change.

## Workflow
1. List conflicted files and group by code, configuration, generated data, and documentation.
2. Compare each side with its parent and inspect callers/tests affected by both changes.
3. Merge behavior deliberately; preserve both requirements where compatible and document genuine incompatibility.
4. Remove conflict markers and check for duplicated imports, branches, keys, or lost data.
5. Run project-requested checks and inspect the final diff before continuing the merge/rebase.

Do not abort, reset, or force-push without authorization. Report any conflict whose intended behavior cannot be inferred safely.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `conflict-resolution`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
