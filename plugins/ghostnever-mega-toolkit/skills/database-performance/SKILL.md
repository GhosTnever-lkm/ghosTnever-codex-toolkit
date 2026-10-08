---
name: database-performance
description: Finds evidence-backed database bottlenecks using query plans, indexes, and observed workload. Use when database latency or load needs diagnosis.
---
# Database Performance

Obtain the query, engine/version, schema, cardinality, indexes, workload, and a safe plan or metric sample. Redact user data from samples.

## Workflow
1. Identify a slow query from observed timings or traces; do not optimize by appearance alone.
2. Inspect the execution plan for scans, cardinality errors, sort/hash spills, repeated lookups, and lock waits.
3. Evaluate index order/selectivity and write overhead; avoid duplicate or speculative indexes.
4. Check N+1 access, over-fetching, unbounded result sets, and connection-pool pressure.
5. Compare before/after on representative data using the same query and environment.

State whether results are measured or inferred, and include write/storage tradeoffs. Never claim production speedup from a local toy dataset.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `database-performance`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
