---
name: "meddra-pharmacovigilance"
description: "Extracts adverse events, maps them to lowest-level terms (LLT) in MedDRA, and computes proportional reporting ratios (PRR)"
version: "1.0.0"
category: "healthcare"
---

# Skill: meddra-pharmacovigilance

## Overview
Extracts adverse events, maps them to lowest-level terms (LLT) in MedDRA, and computes proportional reporting ratios (PRR).

## Execution Steps
1. Parse and validate runtime parameters against the formal domain schema.
2. Execute core computational and heuristic analysis pipeline.
3. Format structured observations for Maker-Checker dual control review.
4. Log all telemetry and performance metrics to the governance ledger.
