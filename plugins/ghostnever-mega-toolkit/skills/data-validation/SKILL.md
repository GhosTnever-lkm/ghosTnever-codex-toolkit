---
name: data-validation
description: Defines checks for imported or transformed data so malformed, duplicated, or inconsistent records are caught early. Use for ETL, CSV, JSON, or batch processing.
---
# Data Validation

Start with the source contract, expected consumers, and consequences of bad records. Preserve original data and state how invalid rows are handled.

## Workflow
1. Define required fields, types, ranges, formats, uniqueness, references, and cross-field invariants.
2. Separate parse errors, schema errors, business-rule failures, and warnings.
3. Make validation deterministic and bounded for large inputs.
4. Provide row/record location and safe context without printing secrets.
5. Choose an explicit policy: reject all, quarantine invalid records, or accept with warnings.
6. Test empty input, encoding issues, duplicates, malformed rows, and boundary values.

Summarize counts by category and explain data-loss risk. Never silently coerce invalid values without a documented rule.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `data-validation`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
