---
name: integration-test-design
description: Designs checks across multiple components or process boundaries, including databases, APIs, files, and CLIs. Use when unit tests miss interaction failures.
---
# Integration Test Design

Identify the actual component boundary and the failure mode to detect. Follow project test setup; use isolated local fixtures and deterministic data.

## Workflow
1. Name the components and contract being exercised end to end.
2. Use temporary directories, disposable databases, or local fakes; never point a test at production.
3. Exercise serialization, process exit status, persistence, retries, and cleanup where they cross boundaries.
4. Assert externally visible outcomes and safe error behavior.
5. Keep setup, timeout, and cleanup explicit; avoid network calls unless the test is specifically about a live integration.

Report what the test proves and what remains outside its boundary. Do not label a mocked integration test as a live-service test.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `integration-test-design`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
