---
id: hiring_workflow_guide
type: runbook
domain: hiring
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.2/10
tags: [workflow, hiring, runbook]
visibility: public
version: 1.0
---

# Hiring Workflow: End-to-End Runbook

Purpose: Human-readable guide complementing hiring_end_to_end.yaml. Defines inputs, stages, outputs, and governance for executing the complete hiring process using candidate JSON input.

## Inputs
- Candidates JSON: data\public\hiring\resume\candidates.json (array)
- Job Description: artifacts\public\hiring\job_descriptions\backend_mid_level.md (role-specific)
- Evaluator GitHub Handle: <YOUR_GITHUB_HANDLE> (add as collaborator for take-home submissions)
- Context Files: 
  - context\company_info\mission_vision_values.yaml
  - context\hr_processes\hiring\hiring_stages.yaml
  - artifacts\public\hiring\interview_process.md

## Stages (mirror of YAML spec)
1. Context Load & Verification
   - Verify required context files, validate JSON schema, run context checklist.
   - Guardrails: stop if any context or schema errors.
2. Intake & Normalization
   - Normalize candidate fields, allocate IDs if missing (atlas_001, nova_002 pattern), redact PII.
   - Output: data\public\hiring\working\{run_id}\candidates.normalized.json
3. JD Mapping & Competency Alignment
   - Parse JD, compute skill diff, scan for value alignment evidence.
   - Output: jd_mapping.json per candidate.
4. Automated Screening & Recommendation
   - Apply ai_docs\plans\candidate_screening_plan.md; generate {name}_screening_report.md.
   - Approval: Platform Lead (required).
5. Personalized Take-Home Assessment
   - Select template from artifacts\public\hiring\takehome_assignment\entry_level; personalize.
   - Require candidate to add the evaluator as a GitHub collaborator: <YOUR_GITHUB_HANDLE>.
   - Outputs: assignment.md, evaluation_sheet.md under upcoming/{candidate_id}.
   - Approval: Platform Lead (required).
5b. Take-Home Assignment Evaluation
   - Use ai_docs\prompts\hiring\evaluate_take_home_assignment_prompt.md as the standard single-assignment evaluation sheet.
   - Verify GitHub collaboration access before review.
   - Output: artifacts\public\hiring\evaluation_sheets\upcoming\{candidate_id}\takehome_evaluation.md.
   - Decision Rule: Proceed if weighted score ≥ 60% (≥ 3.0/5); otherwise do not proceed.
6. Interview Kit Generation
   - Use prompt ai_docs\prompts\hiring\generate_interview_kit_prompt.md with candidates.json.
   - Outputs: candidate_context.md, interview_guide.md, interview_script.md in interview_materials/upcoming/{candidate_id}.
   - Approval: Platform Lead (required).
7. Structured Interview Loop
   - Conduct BEI, pair programming, system design, deep-dive (per interview_process.md).
   - Output: loop_schedule.md + captured notes templates.
8. Post-Interview Consolidation & Scoring
   - Aggregate rubrics and notes, bias check, write evaluation_sheets/upcoming/{candidate_id}/summary.md.
9. Decision, Offer, and Audit
   - Draft decision_record.yaml (private), offer letter (private), write audit log at data\public\ops-estate\hiring_runs\{run_id}.json.

## Execution Hints
- Interview Kits:
  gemini run \
    --prompt "ai_docs\prompts\hiring\generate_interview_kit_prompt.md" \
    --context "data\public\hiring\resume\candidates.json"

- Screening Reports: Use plan steps in ai_docs\plans\candidate_screening_plan.md; ensure outputs match artifacts\public\hiring\evaluation\ pattern.

## MCP Servers & Tools
- exa: company/candidate quick validation.
- sequential-thinking: stage planning and decomposition.
- playwright: optional portfolio/GitHub validation.
- fetch: retrieve assets.

## Quality, Compliance, Bias
- Quality threshold: ≥ 8.5/10 for generated artifacts.
- Approvals: Platform Lead at screening, assessment, interview kits.
- EEO-safe content, PII redaction, GDPR retention (refer security docs).

## Success Metrics
- Time-to-hire reduction 40–60%; interviewer hours -35–50%.
- Rubric completion ≥ 90%; artifact quality ≥ 8.5/10.

## References
- ai_docs\workflows\hiring_end_to_end.yaml
- context\hr_processes\hiring\hiring_stages.yaml
- artifacts\public\hiring\interview_process.md
- ai_docs\plans\candidate_screening_plan.md
