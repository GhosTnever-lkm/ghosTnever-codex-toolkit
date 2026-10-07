---
name: change-review
description: Performs a focused review of a working-tree or commit diff, prioritizing concrete bugs and regressions over style preferences.
---

# Change Review

Review the requested diff as a careful maintainer. Find actionable correctness issues, not cosmetic preferences. Use when the user asks for a code review, risk check, or second look at a patch.

## Workflow

1. Read repository instructions and establish the exact review scope: staged, unstaged, branch diff, or named commit.
2. Inspect the diff and enough surrounding code, callers, tests, and configuration to understand behavior.
3. Trace changed inputs and outputs, error paths, state transitions, and compatibility surfaces.
4. Validate suspected issues against actual code. Do not report hypothetical concerns as findings.
5. Return findings first, sorted by severity. Include file/line, concrete scenario, impact, and a focused fix direction.
6. If no finding is supported, say so and list remaining verification gaps succinctly.

## Severity

- **P1**: likely data loss, security boundary failure, or broad service breakage.
- **P2**: material bug affecting a common or important path.
- **P3**: narrower bug with a concrete reproduction.
- Skip preferences, speculative edge cases, and issues already handled by nearby code.

## Guardrails

- Review only; never modify code unless separately asked to fix findings.
- Do not run tests unless the user asked for verification. If a test was not run, do not imply it passed.
- Do not surface secrets from diffs. Report exposure safely without repeating the value.
- Keep findings independent and avoid duplicate reports for one root cause.

## Finding format

`[P2] Short issue title` — `path/to/file.ext:line`

Explain the triggering condition, observable failure, and why the changed lines cause it. Add a minimal remediation direction.

