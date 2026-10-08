---
name: mod-compatibility
description: Assesses whether a game mod is compatible with specified game, DLC, loader, and other mods. Use for compatibility claims and load-order conflicts.
---
# Mod Compatibility

Confirm game build, DLC set, mod version, loader, platform, and the exact mod combination. Use descriptors and project evidence; avoid defaulting to one storefront.

## Workflow
1. Compare dependency declarations, shared files, script hooks, localization keys, and load order.
2. Separate hard conflicts from intentional overrides and compatible additions.
3. Verify version-specific APIs or file paths against current game documentation or observed release data.
4. Produce a conflict table with path/key, both owners, expected precedence, and user-visible impact.
5. Mark in-game verification separately from static inspection.

Do not claim broad compatibility from a single pairwise test. State the tested versions and the combinations not covered.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `mod-compatibility`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
