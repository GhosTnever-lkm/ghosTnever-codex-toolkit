---
name: bug-hunting
description: Investigates a reported failure by reproducing its path, finding the root cause, and proposing or applying a focused fix. Use for concrete bugs, crashes, or incorrect results.
---
# Bug Hunting

Treat the report as a reproducible observation, not as a diagnosis. Read local instructions and inspect the exact code path before changing anything.

## Workflow
1. Record the reported input, expected result, actual result, environment, and reproduction steps.
2. Reproduce with the smallest safe case. If reproduction is impossible, say exactly which evidence is missing.
3. Trace data and control flow from input through validation, state changes, and output. Check neighboring failure paths.
4. Identify the earliest incorrect assumption or state transition; do not mask symptoms with broad catches or silent fallbacks.
5. Add or update a focused regression check when the task or repository requires tests; fix the root cause.
6. Re-run the reproduction and relevant checks, then inspect the diff.

## Findings
Separate reproduced facts from hypotheses. Give the root cause, impact, exact fix, and verification result. Do not invent a reproduction or claim a regression test exists unless it was run.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `bug-hunting`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
