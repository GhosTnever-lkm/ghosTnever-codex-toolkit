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
