---
name: api-design
description: Designs or reviews an API contract for clarity, compatibility, validation, and useful errors. Use when adding or changing HTTP, CLI, library, or plugin interfaces.
---
# API Design

Ground the design in current users and existing conventions. Define the contract before choosing internal structure.

## Checklist
- Inputs, types, defaults, bounds, and validation rules.
- Success response or output shape, stable identifiers, and pagination where applicable.
- Error categories, status or exit codes, safe messages, and retry guidance.
- Authentication, authorization, idempotency, rate limits, and privacy boundaries where relevant.
- Versioning and compatibility with existing clients, configuration, and generated artifacts.
- Examples for a normal call and a representative failure.

Trace existing consumers and tests before proposing breaking changes. Prefer explicit, stable semantics over clever inference. Present unresolved choices as options with consequences; do not silently decide product policy.
