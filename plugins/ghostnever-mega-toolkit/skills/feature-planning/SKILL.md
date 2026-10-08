---
name: feature-planning
description: Turns a product request into a scoped implementation plan grounded in the current repository. Use before a multi-file feature or when requirements need to become reviewable tasks.
---
# Feature Planning

Create a plan that a maintainer can implement and verify. First read the repository's `AGENTS.md`, existing documentation, architecture, and relevant tests. Identify the user-visible outcome, existing behavior, affected components, and repository conventions.

## Workflow
1. Restate the requested outcome in observable terms; list any assumptions separately.
2. Trace the current flow through UI/API, domain logic, persistence, and tests. Cite actual paths and symbols.
3. Split work into small ordered changes. For each, name likely files, behavior, and a direct verification method.
4. Cover failure states, compatibility, accessibility, security, migrations, and rollback only where relevant.
5. Identify questions that truly block safe implementation. Otherwise choose a conservative default and state it.

## Output
Give a short goal statement, current-state evidence, numbered implementation steps, acceptance checks, and risks. Keep the plan proportional: no speculative infrastructure, unrelated refactors, or invented requirements. Do not edit files while only planning.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `feature-planning`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
