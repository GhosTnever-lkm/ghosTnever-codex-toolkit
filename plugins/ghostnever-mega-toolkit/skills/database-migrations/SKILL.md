---
name: database-migrations
description: Plans or reviews a database schema/data migration with safety for existing records and deploy order. Use when changing tables, indexes, constraints, or stored formats.
---
# Database Migrations

Inspect schema, migration history, ORM conventions, backups, and deployment flow before editing. Assume the database contains real data unless the user says otherwise.

## Workflow
1. Identify affected tables, row counts or scale assumptions, constraints, and all application readers/writers.
2. Design forward and rollback behavior; state explicitly if rollback is lossy or unavailable.
3. For risky changes, prefer expand, migrate, contract: deploy compatible schema, backfill safely, switch code, then remove old fields later.
4. Make backfills bounded, restartable, observable, and idempotent where feasible.
5. Consider locks, index build strategy, nullability, defaults, and mixed-version deployments.
6. Verify migration syntax and behavior using project-approved local fixtures or a disposable database; never target production without direct authorization.

Report deployment order, data impact, rollback path, and verification. Never describe a destructive migration as reversible if data will be discarded.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `database-migrations`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
