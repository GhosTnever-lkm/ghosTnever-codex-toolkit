---
name: sql-query-review
description: Reviews SQL for correctness, injection risk, null semantics, transaction behavior, and portability. Use when authoring or changing database queries.
---
# SQL Query Review

Inspect the target database engine, schema, indexes, constraints, and calling code. Do not infer performance or semantics from generic SQL alone.

## Review
- Parameterize user-controlled values and constrain dynamic identifiers.
- Check NULL behavior, join multiplicity, aggregate semantics, collation, and timezone handling.
- Confirm transaction scope, isolation assumptions, locking, and retry behavior.
- Verify pagination is stable and bounded; avoid accidental full-table scans for common paths.
- Test representative empty, duplicate, and boundary data.

Report the exact query path and engine-specific assumptions. Never execute write queries against production during review.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `sql-query-review`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
