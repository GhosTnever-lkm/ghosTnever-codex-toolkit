---
name: pull-request-prep
description: Prepares a focused pull request from a completed change, including evidence-based title, summary, test results, and review risks. Use when asked to open or polish a PR.
---
# Pull Request Preparation

Inspect the branch diff against its actual base and read contribution guidelines. A PR description must reflect the patch, not intended work that was not completed.

## Checklist
- Confirm branch, base, changed files, and clean working-tree state.
- Summarize user-facing behavior and implementation at a useful level.
- List only checks that actually ran, with outcomes; state unrun checks.
- Mention compatibility, data migration, security, or rollout risks when evidenced.
- Avoid secrets, personal data, speculative claims, and unnecessary marketing.

Do not create or send a PR unless requested. When asked to publish, verify the resulting PR URL, title, body, and diff.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `pull-request-prep`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
