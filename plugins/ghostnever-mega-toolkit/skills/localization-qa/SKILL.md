---
name: localization-qa
description: Checks translated interface and game-mod text for missing keys, placeholder mismatches, encoding, and layout risks. Use for localization files or translated UI.
---
# Localization QA

Identify source and target locales, file format, placeholder syntax, and product terminology. Preserve the project's encoding and key order conventions.

## Checks
1. Compare keys and report missing, duplicate, and unused entries.
2. Match placeholders, markup, plural rules, and escape sequences exactly.
3. Check encoding, line endings, BOM expectations, and unescaped control characters.
4. Flag likely clipping, unexpanded text, mixed-language strings, and inconsistent terminology.
5. Distinguish mechanical checks from linguistic review; do not invent authoritative translations for domain-specific terms.

Report exact file/key and a safe correction. Do not rewrite unrelated translations or change gameplay meaning.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `localization-qa`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
