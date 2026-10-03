---
name: meddra-pharmacovigilance
description: Specialized capability for Clinical Adverse Event Monitor.
license: MIT
allowed-tools: ""
metadata:
  author: "Rucha Salpure"
  version: "1.0.0"
  category: healthcare
---

# Clinical Adverse Event Monitor — MEDDRA PHARMACOVIGILANCE Skill

## Purpose
The `meddra-pharmacovigilance` capability provides high-assurance execution routines for `Clinical Adverse Event Monitor`.

## Execution Workflow
1. Validate input parameters against typed schemas and invariant constraints.
2. Ingest contextual metrics and establish a deterministic baseline.
3. Formulate candidate recommendations with explicit confidence intervals.
4. Submit draft plans to the independent checker agent for verification.

## Boundary Conditions
- **Input validation:** Reject non-conforming or malformed payloads before evaluation.
- **Fail-safe:** Escalate immediately if telemetry indicators exhibit critical anomalies.
