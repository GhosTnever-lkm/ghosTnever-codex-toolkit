---
name: performance-analysis
description: Diagnoses a measurable performance problem and identifies an evidence-backed bottleneck. Use when asked to speed up a slow path, reduce memory, or assess scaling.
---
# Performance Analysis

Start from the user's workload and measured symptom. Avoid optimizing by intuition alone.

## Workflow
1. Establish workload size, environment, latency or memory target, and current measurement.
2. Trace the hot path and identify repeated work, algorithmic complexity, blocking I/O, excessive rendering, or avoidable allocation.
3. Prefer a representative local benchmark or profiler. Keep inputs and environment reproducible.
4. Compare before and after using the same workload; include variance and warm-up considerations when relevant.
5. Check correctness, memory growth, and worst-case behavior after an optimization.
6. If measurement tools or a baseline are unavailable, present a ranked hypothesis list rather than claiming a speedup.

Deliver the bottleneck evidence, focused change, measured result, and tradeoffs. Avoid broad caching or concurrency changes that complicate invalidation or safety without demonstrated need.
