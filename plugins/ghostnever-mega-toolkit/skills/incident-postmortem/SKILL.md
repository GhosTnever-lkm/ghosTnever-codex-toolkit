---
name: incident-postmortem
description: Writes a blameless incident review based on a verified timeline, impact, contributing factors, and follow-up actions. Use after a service incident or production outage.
---
# Incident Postmortem

Use confirmed incident records and protect personal, customer, and security-sensitive information. Do not infer a root cause from timing alone.

## Structure
- Summary and user impact with a clear time window.
- Detection and response timeline with timestamps and evidence.
- What happened, contributing conditions, and what limited or extended recovery.
- What worked and what needs improvement, without assigning personal blame.
- Owned follow-ups with measurable outcomes and realistic priority.

Mark unknowns explicitly. Separate immediate trigger from systemic contributors. Do not state a corrective action is complete until there is evidence.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `incident-postmortem`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
