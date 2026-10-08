---
name: refactoring-plan
description: Plans a behavior-preserving refactor around a concrete maintenance problem. Use when asked to simplify, reorganize, or extract code without changing product behavior.
---
# Refactoring Plan

First establish behavior, public interfaces, and existing test coverage. Tie every proposed structural change to a specific maintenance cost or defect.

## Workflow
- Map the current dependency direction and the smallest affected area.
- Identify invariants, callers, serialization, configuration, and error behavior that must remain stable.
- Divide the refactor into incremental steps that leave the project runnable.
- Add characterization checks only when requested or required by project guidance.
- Separate cleanup from behavior changes so regressions are attributable.

Return a small sequence with explicit behavior-preservation checks. Avoid broad architecture rewrites, speculative abstractions, or claiming equivalence without evidence.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `refactoring-plan`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
