---
name: logging-observability
description: Improves logs, metrics, and traces so failures can be diagnosed without exposing sensitive data. Use when an application is hard to monitor or debug.
---
# Logging and Observability

Map the request lifecycle and existing instrumentation before adding telemetry. Follow privacy policy and retention rules.

## Design
- Use structured, stable event names and include correlation IDs that do not identify a person.
- Record state transitions, durations, and bounded error categories rather than entire payloads.
- Keep metric labels low-cardinality; avoid user IDs, raw URLs, and exception text as labels.
- Make failures observable at the boundary and avoid duplicate noisy logs at every layer.
- Redact secrets and personal data before the logging sink.

Recommend the smallest instrumentation that distinguishes likely failure modes. Verify output shape and confirm sensitive examples do not appear in logs.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `logging-observability`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
