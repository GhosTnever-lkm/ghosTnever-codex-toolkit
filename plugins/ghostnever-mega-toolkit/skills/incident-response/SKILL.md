---
name: incident-response
description: Helps contain and diagnose a software incident using observable evidence and reversible actions. Use for outages, data corruption, or production regressions.
---
# Incident Response

Prioritize user safety, service recovery, and evidence preservation. Follow the organization's incident policy and user authorization. Do not make high-impact production changes without authorization.

## Workflow
1. Establish impact, start time, affected versions, scope, and current user-visible symptoms.
2. Gather read-only logs, metrics, traces, and recent changes; protect personal data and secrets.
3. Form testable hypotheses and rank by evidence; separate symptoms from root cause.
4. Recommend a reversible mitigation with owner, expected effect, and rollback signal.
5. Verify service recovery with a relevant health check and user-facing behavior.
6. Record timeline, confirmed facts, unknowns, and follow-up actions without blame.

Never delete data or rotate credentials as a guess. State exactly what is confirmed, what remains uncertain, and what monitoring should confirm stability.
