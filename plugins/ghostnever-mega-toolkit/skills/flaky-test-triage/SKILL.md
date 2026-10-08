---
name: flaky-test-triage
description: Diagnoses intermittent test failures by comparing runs, timing, shared state, and environment. Use when a test passes sometimes and fails sometimes.
---
# Flaky Test Triage

Preserve failing output and identify exact test, runtime, parallelism, and environmental conditions. Do not hide flakiness by increasing retries before finding a cause.

## Investigate
- Shared files, databases, ports, global state, and test-order dependence.
- Time zones, locale, random seeds, race conditions, and asynchronous cleanup.
- Resource pressure, external service dependence, rate limits, and network timing.
- Different runtime versions or platform-specific behavior.

Reproduce with a bounded repeat count and capture failure frequency. Make the smallest isolation or synchronization fix, then verify both focused and normal suite behavior when authorized. State whether the root cause is confirmed or still a hypothesis.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `flaky-test-triage`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
