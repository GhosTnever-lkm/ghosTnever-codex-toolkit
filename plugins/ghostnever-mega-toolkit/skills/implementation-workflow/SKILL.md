---
name: implementation-workflow
description: Implements a requested code change in an existing repository with narrow scope and repository-native conventions. Use when asked to build a feature or make a code fix.
---
# Implementation Workflow

Start with repository guidance, then trace the exact behavior to change. Prefer the smallest complete implementation that fits the existing architecture. Inspect nearby code and tests before introducing abstractions or dependencies.

## Workflow
1. Confirm observable acceptance criteria from the request and current behavior.
2. Map callers, state, validation, errors, compatibility constraints, and relevant tests.
3. Implement the full user path, including empty, invalid, and failure states where applicable.
4. Keep changes focused; reuse established patterns and avoid unrelated formatting or API changes.
5. Run only the checks requested by the user or project instructions. Report unrun checks honestly.
6. Inspect the final diff for accidental files, secrets, generated output, and scope drift.

## Report
Summarize what changed and why, list touched areas, state the exact verification performed and its result, and name material limitations. Never claim a feature works end-to-end based only on compilation or a successful tool call.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `implementation-workflow`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
