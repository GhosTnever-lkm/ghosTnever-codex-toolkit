---
name: typescript-node
description: Builds or maintains TypeScript and Node.js applications with attention to runtime boundaries, types, packaging, and async behavior. Use for JavaScript/TypeScript repository work.
---
# TypeScript and Node.js Engineering

Inspect package scripts, module format, target Node versions, tsconfig, lint rules, and lockfile before editing. Keep runtime assumptions aligned with the published package.

## Practices
- Validate values arriving from JSON, environment variables, files, and network responses; TypeScript types do not validate runtime data.
- Handle rejected promises and stream/file cleanup explicitly.
- Preserve ESM/CommonJS boundaries and export maps; check what consumers can actually import.
- Avoid shell-string construction from user input; use argument arrays and bounded subprocesses.
- Keep browser and Node APIs separated when both environments are supported.
- Test package build and real entry points, not only source compilation.

Follow existing code style and scripts. Report Node versions and commands actually used; do not claim cross-runtime support from a single local run.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `typescript-node`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
