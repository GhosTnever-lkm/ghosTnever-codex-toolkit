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
