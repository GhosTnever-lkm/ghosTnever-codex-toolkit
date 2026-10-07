---
name: docs-from-code
description: Creates or improves developer documentation grounded in current source code and repository conventions. Use for setup guides, architecture notes, and API docs.
---

# Documentation from Code

Write developer documentation that matches the implementation as it exists today. Use for setup instructions, architecture notes, API behavior, and contributor guidance.

## Workflow

1. Read repository guidance and current docs/templates; follow the project's language and formatting conventions.
2. Trace every documented command, configuration key, API route, and behavior to source, tests, manifests, or CI.
3. Identify the intended reader and answer the task they need to complete. Keep prerequisites and expected results explicit.
4. Draft concise steps, include working examples only when grounded in code, and link to relevant paths.
5. Check for outdated or conflicting nearby docs before editing. Make the smallest coherent doc change.
6. Summarize changed files and note any behavior that could not be verified from source.

## Guardrails

- Never fabricate API behavior, environment variables, compatibility claims, or commands.
- Do not include credentials, private endpoints, or real secret examples. Use obvious placeholders.
- Do not rewrite broad documentation areas when the request is narrow.
- If asked to edit, preserve accurate existing content and avoid changing application code unless requested.

## Output shape

State the audience and goal; provide steps with prerequisites, commands, expected result, and links to implementation. Use tables only when they make choices easier to compare.

