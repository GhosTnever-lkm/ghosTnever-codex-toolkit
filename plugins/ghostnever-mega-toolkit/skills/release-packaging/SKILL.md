---
name: release-packaging
description: Prepares reproducible release archives with correct contents, version metadata, checksums, and installation instructions. Use before publishing a software or mod release.
---
# Release Packaging

Read the project's release policy and compare the package contents with the repository's supported install path. Never include secrets, caches, user data, or unrelated build outputs.

## Workflow
- Build from a clean, known commit and record the source revision.
- Include required manifests, license, changelog, and runtime assets; exclude development files unless needed.
- Verify archive paths, executable bits, encoding, and package size.
- Generate checksums and test a fresh extraction/install in a temporary directory.
- Check the README command against the actual archive layout and version.

Report the artifact name, version, source commit, checksum, and exact install check. Do not publish until the user asks.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `release-packaging`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
