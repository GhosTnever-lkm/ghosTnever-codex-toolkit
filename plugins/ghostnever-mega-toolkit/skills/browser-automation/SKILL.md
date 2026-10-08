---
name: browser-automation
description: Builds reliable browser automation for a web app using existing project tools and accessible UI behavior. Use for Playwright or browser-test implementation and debugging.
---
# Browser Automation

Inspect the project's browser framework, test fixtures, and accessibility conventions first. Prefer role, label, and visible-text locators over brittle selectors.

## Workflow
- Define the user-visible scenario and expected state transition.
- Reuse authenticated fixtures safely; never store real credentials in tests.
- Wait for meaningful UI state, not arbitrary delays.
- Cover navigation, loading, empty, error, and success states relevant to the change.
- Keep tests isolated and deterministic; mock external services at the boundary unless live behavior is the target.
- Capture useful failure diagnostics without logging tokens or personal data.

Run only the authorized or project-prescribed test. Report browser, viewport, and integration limits accurately.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `browser-automation`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
