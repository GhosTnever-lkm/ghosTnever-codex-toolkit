---
name: accessibility-audit
description: Audits an interface for practical keyboard, screen-reader, contrast, and motion barriers. Use when asked to improve accessibility or review UI accessibility.
---
# Accessibility Audit

Inspect the rendered interface and its actual markup where available. Follow the project's design conventions and target conformance level if specified; do not claim full certification from a quick review.

## Check
- Semantic structure, headings, landmarks, labels, accessible names, and status announcements.
- Keyboard-only navigation, visible focus, logical order, escape/close behavior, and no keyboard traps.
- Contrast and non-color cues for text, icons, controls, and states.
- Zoom/reflow, responsive behavior, reduced motion, and touch target usability.
- Form errors and validation connected to fields and announced clearly.

Prioritize blockers by user impact, cite exact components, and offer concrete fixes. Automated scans are useful evidence but cannot replace keyboard and assistive-technology checks; state what was and was not tested.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `accessibility-audit`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
