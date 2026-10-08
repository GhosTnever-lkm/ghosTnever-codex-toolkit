---
name: test-engineering
description: Designs and implements focused tests for a behavior, regression, or component. Use when asked to add tests, improve coverage, or verify a specific change.
---
# Test Engineering

Tests should prove observable contracts with minimal brittleness. Read the project test instructions and existing fixtures before choosing a framework or adding dependencies.

## Workflow
1. Identify the public behavior and the failure or boundary the test must distinguish.
2. Choose the closest existing test layer: unit, integration, CLI, browser, or end-to-end.
3. Cover a normal case, the reported regression, and only the most important edge cases.
4. Keep test data deterministic and local. Avoid real credentials, external services, timing assumptions, and broad snapshots.
5. Run the focused test first, then the repository-prescribed broader check if requested or required.
6. Confirm a failing test would detect the old bug when feasible; report what was actually executed.

Do not inflate counts with duplicate examples. Tests should assert outcomes and error semantics, not private implementation details unless unavoidable.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `test-engineering`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
