---
name: python-engineering
description: Builds or maintains Python packages and command-line tools using the repository's packaging, typing, and test conventions. Use for Python-specific implementation work.
---
# Python Engineering

Read `pyproject.toml`, supported Python versions, package layout, formatter/linter settings, and contributor instructions first. Do not add a framework just to solve a small task.

## Practices
- Keep imports and packaging metadata consistent with the supported Python range.
- Validate external input at boundaries; use `pathlib`, context managers, and explicit encoding where appropriate.
- Make CLI errors actionable and return stable exit codes; keep stdout machine-readable when promised.
- Preserve backwards compatibility for public functions, configuration, and serialized data.
- Use type hints for public interfaces and narrow types around untrusted values.
- Test behavior without network access unless the product explicitly depends on it.

Run only project-prescribed checks. Review generated files and package contents before reporting. Distinguish static checks from a built and executed package.
