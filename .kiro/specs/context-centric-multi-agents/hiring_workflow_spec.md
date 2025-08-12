---
id: kiro_hiring_workflow_spec
type: spec
domain: hr_automation
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [kiro, multi-agent, workflow, hiring]
visibility: public
version: 1.0
---

# Context-Centric Multi-Agents: Hiring Workflow Spec

This specification binds the multi-agent task framework to the canonical hiring workflow.

Primary workflow reference:
- ai_docs\workflows\hiring_end_to_end.yaml (executable spec)
- ai_docs\workflows\hiring_end_to_end.md (runbook)

## Agent Roles & Responsibilities
- Context Manager Agent — Load/verify context, enforce checklists.
- Profile Processor Agent — Normalize candidate JSON, allocate IDs, redact PII.
- Analysis Agent — JD mapping, competency and values alignment.
- Screening Agent — Apply candidate_screening_plan, generate recommendations.
- Assessment Generator — Personalize assignment and rubric.
- Assessment Evaluator — Evaluate take-home submissions using Top-Tier Industry Standards (evaluate_take_home_assignment_prompt.md); compute Strong Hire/Hire/Lean Hire/No Hire.
- Interview Kit Generator — Produce candidate_context.md, interview_guide.md, interview_script.md.
- Orchestrator Agent — Enforce approval gates, schedule interview loop, route handoffs.
- Scoring & Consolidation Agent — Aggregate rubrics/notes, bias check, summary.
- Decision & Audit Agent — Decision record, offer draft, audit logging.

## Stage Mapping (Summary)
Refer to stages in ai_docs\workflows\hiring_end_to_end.yaml:
1. context_engineering → Context Manager
2. intake → Profile Processor
3. jd_mapping → Analysis Agent
4. screening → Screening Agent (approval: Platform Lead)
5. assessment → Assessment Generator (approval: Platform Lead)
6. assessment_evaluation → Assessment Evaluator (Top-Tier Industry Standards: Strong Hire ≥4.5, Hire ≥3.8, Lean Hire ≥3.0, No Hire <3.0)
7. interview_preparation → Interview Kit Generator (approval: Platform Lead)
8. interviewing → Human-led, Orchestrator support
9. consolidation → Scoring & Consolidation Agent
10. decision → Decision & Audit Agent

## Inputs & Outputs (Canonical Paths)
- Input: data\public\hiring\resume\candidates.json
- Public Outputs: artifacts\public\hiring\...
- Take-home evaluation: artifacts\public\hiring\evaluation_sheets\upcoming\{candidate_id}\takehome_evaluation.md
- Private Outputs: artifacts\private\hiring\...
- Audit: data\public\ops-estate\hiring_runs\{run_id}.json

## Guardrails & Approvals
- Approval gates at screening, assessment, interview kits (Platform Lead).
- Quality threshold ≥ 8.5/10; re-run or revision if below.
- Bias checks on consolidation; PII redaction at intake.

## Acceptance Criteria
- For each candidate in input JSON, the system produces:
  - Screening report with justification and next steps.
  - Take-home assignment + evaluation sheet using Top-Tier Industry Standards at `artifacts\public\hiring\evaluation_sheets\upcoming\{candidate_id}\takehome_evaluation.md`. Decision thresholds: Strong Hire (≥4.5), Hire (≥3.8), Lean Hire (≥3.0), No Hire (<3.0).
  - Interview kit (context, guide, script) before loop.
  - Consolidated evaluation summary after loop.
  - Decision record and audit log on completion.

## Observability
- Trace ID = {run_id} across stages.
- Audit fields: candidate_id, stage, actor, tool, timestamp, quality_score, approver.

## Execution Notes
- Use MCP servers: exa, sequential-thinking, playwright, fetch as needed.
- Invoke prompts per spec; e.g., interview kits via ai_docs\prompts\hiring\generate_interview_kit_prompt.md.
