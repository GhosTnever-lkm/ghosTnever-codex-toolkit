# Changelog

## 1.1.5 - 2026-10-25

- Reject extra skill names on the PowerShell list/reset commands so malformed reset invocations cannot silently clear disabled skills.
- Add a Windows regression that verifies rejected reset arguments leave the settings file unchanged.

## 1.1.4 - 2026-10-12

- Verify the 41 task skills match both plugin manifests and both settings helpers.
- Add end-to-end regression coverage for local enable/disable controls on Windows and Linux.
- Keep Russian CLI messages readable when output is redirected on Windows.

## 1.1.3 - 2026-10-12

- Preserve unrelated local settings when enabling, disabling, or resetting skills.
- Validate that the settings file contains a JSON object before updating it.

## 1.1.2 - 2026-10-08

- Added Windows PowerShell controls and direct settings changes in Codex.

## 1.1.1 - 2026-10-08

- Added 20 task workflows for a total of 41, plus the settings guide.
- Added local per-workflow enable and disable controls.
- Updated setup instructions and marketplace metadata.
