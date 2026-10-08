---
name: product-usability-review
description: Reviews a user flow for clarity, friction, empty states, error recovery, and consistent language. Use when asked to polish an application or make it easier to use.
---
# Product Usability Review

Start from the target user, primary task, and actual interface. Inspect current copy and interaction behavior rather than inventing a new product direction.

## Review path
1. Follow the main task from entry to completion, including first use and returning use.
2. Check labels, hierarchy, next action, progress, empty/loading/error/success states, and recovery.
3. Look for unnecessary decisions, hidden requirements, duplicate controls, and unexplained jargon.
4. Ensure destructive or paid actions are clearly described before they occur.
5. Offer prioritized changes that can be tied to user outcomes; separate observed friction from design hypotheses.

Keep product copy concise, concrete, and consistent with the user's language. Do not add marketing claims or AI-authorship claims the user did not request.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `product-usability-review`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
