---
name: configuration-management
description: Designs configuration defaults, precedence, validation, and migration for an application or tool. Use when adding settings or changing config formats.
---
# Configuration Management

Read existing configuration conventions and identify user, project, environment, and default layers. Preserve backward compatibility unless the request authorizes a break.

## Checklist
- Document precedence and where each value is stored.
- Validate types, ranges, unknown keys, and mutually exclusive settings.
- Keep secrets out of committed defaults and diagnostics.
- Make defaults safe and explainable; avoid hidden network or data collection behavior.
- Migrate older settings without overwriting user changes; retain an error path for invalid data.
- Test missing, partial, malformed, and future-version configuration.

Return the schema, precedence, migration behavior, and examples. Do not silently discard unknown user data.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `configuration-management`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
