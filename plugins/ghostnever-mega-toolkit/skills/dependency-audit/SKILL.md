---
name: dependency-audit
description: Reviews project dependencies for necessity, version constraints, maintenance risk, and supply-chain exposure. Use when asked to inspect or reduce dependency risk.
---
# Dependency Audit

Read manifests, lockfiles, install scripts, and CI configuration. Verify what is direct versus transitive and identify dependencies that execute code during install or build.

## Workflow
1. Inventory runtime, development, optional, and action dependencies from project files.
2. Check for unused or duplicated packages using actual imports and build references.
3. Review version ranges, lockfile coverage, integrity hashes, lifecycle scripts, and pinned external actions.
4. If current vulnerability information is needed, use a trusted live advisory source and record its date; do not infer vulnerability from age alone.
5. Recommend the smallest safe change. Do not upgrade a major version without compatibility evidence.
6. Run the package manager's lockfile and focused CI checks only when authorized or project-required.

Report package, role, evidence, concrete risk, proposed action, and migration/testing impact. Distinguish verified advisories from general maintenance concerns.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `dependency-audit`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
