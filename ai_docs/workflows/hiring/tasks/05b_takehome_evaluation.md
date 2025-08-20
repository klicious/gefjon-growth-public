---
id: takehome_evaluation_task
type: task
domain: hiring
stage: 5.5
created_date: 2025-08-20
author: Junie
quality_score: 9.5/10
tags: [takehome, evaluation, evidence, rubric, github]
visibility: public
version: 1.0
---

# Task 5b: Take-Home Assignment Evaluation (Evidence-Required)

Purpose: Evaluate submitted take-home assignments with comprehensive, verifiable evidence for every score. Outputs determine eligibility for Stage 6 (Interview Kit Generation).

## Prerequisites
- Task 5 (Personalized Take-Home Assessment) completed and assignment submitted by candidate
- Candidate GitHub repository URL available
- Platform Lead availability for approval gate

## Objectives
- Perform rubric-based evaluation with strict evidence backing
- Ensure reproducibility and compliance (security, licenses)
- Assess observability and operational guardrails
- Produce decision and gating status for Stage 6

## Rubric (1–10 per criterion, 0.5 granularity)
1. Requirements Coverage
2. Code Quality
3. Architecture & Scalability
4. Correctness & Testing
5. Performance & Efficiency
6. Security & Compliance
7. Documentation & DX
8. Observability

Decision thresholds: Strong Hire ≥ 9.0, Hire ≥ 8.0, Lean Hire 6.5–7.9, No Hire < 6.5

## Mandatory Evidence Standard
For each scored criterion, include:
- Evidence: file_path:lineStart-lineEnd @ commitShortSHA
- Summary: 1–2 sentences explaining why the evidence supports the score
- Links: GitHub URL(s) to referenced file or commit (when available)

If line ranges are not applicable (e.g., README), indicate section header and line range within the file.

## Processing Steps (AI Agent Instructions)
1. Collect Inputs
   - Identify default branch and recent commit SHA (short)
   - Gather repository structure (key directories and files)
   - Read README/setup instructions for reproducibility
2. Analyze & Gather Evidence
   - Architecture: modules, layering, separation of concerns
   - Correctness: tests, CI configs, edge case handling
   - Security: secrets, input validation, error handling, license
   - Observability: logging, metrics, health endpoints, timeouts/retries
3. Score per Criterion
   - For each rubric item: Score, Evidence (path:lines @ SHA), Commentary
4. Generate Artifacts
   - Update takehome_evaluation.md (filled with scores + evidence)
   - Update evaluation_sheet.md (summary + totals)
   - Create evaluation_summary.json (per-criterion breakdown + decision)
5. Decision & Gating
   - Apply thresholds; default: proceed to Stage 6 if Overall ≥ 8.0
   - Record Platform Lead approval for Hire/Strong Hire
6. Quality & Bias Checks
   - Neutral, evidence-based language only
   - Complete Security & Compliance and Observability checklists

## Output Structure
- artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/takehome_evaluation.md
- artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/evaluation_sheet.md
- artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/evaluation_summary.json

## Quality Gates
- Evidence included for every criterion (path, lines, commit SHA) ✓
- Reproducibility validated or steps provided ✓
- Security & Compliance checklist completed ✓
- Observability assessment completed ✓
- Scores consistent with decision thresholds ✓
- Platform Lead approval recorded for decisions ≥ Hire ✓

## MCP Integration
- exa (primary): crawl repository pages and commits
- fetch (fallback): direct URL fetch for README and raw files

## Execution Example
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md" \
  --context "artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/" \
  --mode "production"
```

## Validation Checklist
- [ ] Repo URL and latest commit SHA captured
- [ ] Evidence provided for each rubric criterion
- [ ] Reproducibility confirmed or steps included
- [ ] Security & Observability checklists completed
- [ ] Overall score and decision recorded
- [ ] Gating and approvals documented
