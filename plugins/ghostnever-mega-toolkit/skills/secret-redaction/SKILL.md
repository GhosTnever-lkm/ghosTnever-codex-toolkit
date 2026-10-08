---
name: secret-redaction
description: Reviews or improves redaction of credentials and personal data in logs, reports, crash files, and support bundles. Use before sharing diagnostic output.
---
# Secret Redaction

Determine the exact data sources and output sinks. Treat logs as sensitive until checked; never repeat detected credential values in the response.

## Workflow
1. Inventory token formats, authorization headers, cookies, private keys, URLs, account IDs, emails, and user paths relevant to the product.
2. Redact before serialization or upload, not only in display formatting.
3. Preserve useful structure with stable placeholders; avoid over-redaction that makes diagnostics useless.
4. Test mixed case, whitespace, encoded values, multiline secrets, and nested JSON where applicable.
5. Ensure reports and temporary artifacts do not retain the original data.

Report categories and locations only. Do not send files or logs to external services unless the user explicitly requests the destination.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `secret-redaction`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
