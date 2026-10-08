---
name: git-workflow
description: Plans safe Git operations and explains repository state before staging, committing, branching, or synchronizing. Use for branch, commit, history, and remote workflow questions.
---
# Git Workflow

Inspect `git status`, current branch, remotes, recent commits, and repository guidance before acting. Never assume the user's branch is disposable or that uncommitted work can be overwritten.

## Workflow
1. Identify staged, unstaged, untracked, ignored, and conflicting files separately.
2. For a requested commit, inspect the full staged diff and exclude secrets, generated output, and unrelated work.
3. Preserve the configured identity; do not change global Git settings unless asked.
4. Before reset, rebase, force-push, or branch deletion, explain the exact affected commits and recovery path; avoid if a reversible path exists.
5. After sync, verify the intended branch and remote state.

Report actual commands and resulting commit IDs. Never claim a push succeeded until the remote confirms it.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `git-workflow`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
