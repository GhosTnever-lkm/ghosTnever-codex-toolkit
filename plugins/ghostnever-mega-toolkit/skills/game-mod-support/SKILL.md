---
name: game-mod-support
description: Helps maintain game mods by mapping files, validating metadata and archives, diagnosing conflicts, and preparing safe releases. Use for modding projects, especially Paradox-style data mods.
---
# Game Mod Support

Identify the game, platform, version, mod loader, directory layout, and intended compatibility from repository evidence. Do not assume Steam paths or game versions.

## Workflow
1. Inspect descriptors, manifests, load-order metadata, localization, scripts, assets, and packaging rules.
2. Validate references, duplicate paths, encoding, identifiers, and dependency/load-order assumptions.
3. Compare behavior against the target game version and relevant upstream documentation when semantics may have changed.
4. Preserve source and user data; inspect archives for traversal, symlinks, duplicate entries, and size bombs before extraction.
5. Provide a reproducible local validation path and a clean release archive with version and changelog.
6. Clearly separate static checks from in-game verification; never say the mod runs unless tested in the actual game.

Report findings by severity with file paths and exact evidence. Avoid altering unrelated balance or lore while fixing a technical defect.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `game-mod-support`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
