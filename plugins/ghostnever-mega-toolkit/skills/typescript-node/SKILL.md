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
