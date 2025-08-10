---
id: workflows_index
type: documentation
domain: hr_workflows
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [workflows, hiring, orchestration]
visibility: public
version: 1.0
---

# Gefjon Growth Workflows

Purpose: Centralize well-defined, executable workflows for HR automation. This directory contains the canonical end-to-end hiring workflow specification consumed by AI agents and humans.

## Contents
- hiring_end_to_end.yaml — canonical, executable workflow spec for hiring
- hiring_end_to_end.md — narrative guide for humans (overview, roles, governance)

## Conventions
- Inputs are passed as Windows paths (e.g., `data\public\hiring\resume\candidates.json`).
- Outputs are written under `artifacts\public\hiring\...` unless noted as private.
- All generated files include YAML metadata headers per JUNIE.md.
- Agents should honor approvals, guardrails, and bias checks defined in the spec.
- Take-home assessments: candidates must add the evaluator as a GitHub collaborator. Configure the handle via `inputs.evaluator_github_handle` in `ai_docs\workflows\hiring_end_to_end.yaml`. 

## Execution Pattern (example)
- Generate Interview Kits (per candidate JSON):
  gemini run \
    --prompt "ai_docs\prompts\hiring\generate_interview_kit_prompt.md" \
    --context "data\public\hiring\resume\candidates.json"

## Related Context
- context\hr_processes\hiring\hiring_stages.yaml
- artifacts\public\hiring\interview_process.md
- ai_docs\prompts\hiring\
- ai_docs\prompts\hiring\evaluate_take_home_assignment_prompt.md (standard single-assignment evaluation sample)
- ai_docs\plans\candidate_screening_plan.md

## Governance & Quality Gates
- Manual approvals: Platform Lead for screening, assessment, interview kits.
- Quality threshold: All generated materials must score ≥ 8.5/10.
- Compliance: EEO-safe prompts, PII redaction, GDPR-aware retention in artifacts.
