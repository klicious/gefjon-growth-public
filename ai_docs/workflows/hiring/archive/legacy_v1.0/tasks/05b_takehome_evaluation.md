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

## Rubric (Agent input: 1–10 per criterion, 0.5 granularity; Executive rendering: 5-point weighted)
1. Functional Correctness & Completeness (25%)
2. Code Quality & Best Practices (20%)
3. Testing Approach & Coverage (15%)
4. Documentation Quality (10%)
5. Going Above and Beyond / Ownership (15%)
6. Scalability & Design Patterns (15%)
7. Quantitative & Logical Problem Solving (10%)

Executive decision thresholds (5-point overall): Strong Hire ≥ 4.5, Hire ≥ 3.8, Lean Hire ≥ 3.0, No Hire < 3.0

## Mandatory Evidence Standard
For each scored criterion, include:
- Evidence: file_path:lineStart-lineEnd @ commitShortSHA
- Summary: 1–2 sentences explaining why the evidence supports the score
- Links: GitHub URL(s) to referenced file or commit (when available)

If line ranges are not applicable (e.g., README), indicate section header and line range within the file.

## Processing Steps (AI Agent Instructions)
0. Agent‑First Evaluation Protocol (MANDATORY)
   - Evaluation MUST be performed by an AI agent using the provided per‑candidate template.
   - Python scripts are SUPPORTING ONLY: cloning, scaffolding templates, and optionally aggregating agent‑provided scores. No heuristic auto‑evaluation.
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
   - Populate: artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/agent_evaluation_template.md
   - Optional machine‑readable: artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/agent_evaluation.json
4. Generate Artifacts (by agent + optional aggregator)
   - Agent updates takehome_evaluation.md (scores + evidence) OR writes agent_evaluation.json
   - If agent_evaluation.json exists, run aggregator to compute totals and render final report
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


## Repository Cloning Protocol (MANDATORY)

- Clone each candidate's take-home repository to the private workspace for reproducibility:
  - Local path: data/private/hiring/repositories/{candidate_id}/repo
  - Meta files: data/private/hiring/repositories/{candidate_id}/repo_meta.json and META.md
- Recommended command (automated):
```bash
python scripts/execute_05b_takehome_evaluation.py \
  --candidate-id {candidate_id} \
  --candidate-name "{candidate_name}" \
  --github-url "{github_url}" \
  --batch "{batch}"
```
- Captured meta MUST include:
  - default_branch
  - head_commit_short (short SHA)
  - repo_local_path

## Evidence Requirements (Per Criterion)

- Mandatory evidence for EVERY score:
  - File path(s) and line ranges
  - Commit SHA reference in the format path:lineStart-lineEnd @ <shortSHA>
  - Brief commentary tying code to the rubric criterion
- Reproducibility steps:
  - Use README instructions or provide precise commands
  - Note any environment variables, secrets handling, and run scripts

## Output Updates
- Update artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/takehome_evaluation.md with:
  - Scores (1–10 with 0.5 granularity)
  - Evidence per criterion
  - Overall decision consistent with thresholds
  - Security & Compliance and Observability checklists
- Update artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/evaluation_sheet.md with summary and totals.

## Validation Checklist
- [ ] Repository cloned under data/private/hiring/repositories/{candidate_id}/repo
- [ ] repo_meta.json contains default_branch and head_commit_short
- [ ] Evidence (path:lines @ commit) present for ALL criteria
- [ ] Reproducibility steps documented
- [ ] Decision aligns with thresholds; neutrality check passed

## Note on Prior Skipping
- Previously skipped because workflow_config did not require takehome_evaluation.md and there was no explicit repository cloning protocol. Both gaps are now addressed in config and orchestrator.


## Git Access Protocol (Default: SSH)

- Default protocol for all cloning operations is SSH.
- The evaluation runner will automatically rewrite any GitHub HTTPS URL (https://github.com/owner/repo[.git]) to SSH format (git@github.com:owner/repo.git).
- Prerequisites:
  - Configure an SSH key and add it to your GitHub account.
  - Verify access before running: ssh -T git@github.com
- Non-interactive behavior:
  - The runner sets GIT_TERMINAL_PROMPT=0 to avoid blocking credential prompts.
  - If SSH is not configured, cloning will fail fast with a clear error message and guidance.
- Rationale:
  - Avoids HTTPS credential prompts and PAT requirements in CI/non-interactive environments.


## Report Format Standard (Executive-grade)

All AI agent evaluations MUST produce an executive-grade report using Gefjon Platform Engineering Standards. Use the following structure and language:

- Title: "Take-Home Assignment Evaluation Report: Mid-Level Backend Engineer (Gefjon Platform Engineering Standards)"
- Header:
  - Candidate Name, Evaluator (AI Evaluator), Date of Evaluation (YYYY-MM-DD)
- Overall Recommendation (checkboxes): Strong Hire | Hire | Lean Hire | No Hire
- Evaluation Criteria (weights shown; per-criterion 5-point score displayed; underlying 10-point agent JSON allowed):
  1) Functional Correctness & Completeness (25%)
  2) Code Quality & Best Practices (20%)
  3) Testing Approach & Coverage (15%)
  4) Documentation Quality (10%)
  5) Going Above and Beyond / Ownership (15%)
  6) Scalability & Design Patterns (15%)
  7) Quantitative & Logical Problem Solving (10%)
- For each criterion:
  - Score: X/5
  - Comments: 3–7 succinct bullets, balanced (✅ strengths, ❌ gaps), neutral and evidence-based
  - Evidence Appendix: concrete references in format path:lineStart-lineEnd @ commitShortSHA — note
- Overall Score: X.X/5 and Decision mapping
- Detailed Feedback sections:
  - Limited Strengths
  - Critical Gaps vs. Production Readiness
  - Alignment with Job Description & Engineering Values
- Next Steps (checkboxes)
- Security & Compliance Checklist (checkboxes)
- Observability & Guardrails (checkboxes)
- Reviewer Notes

Constraints and language policy:
- Use "Gefjon Platform Engineering Standards"—avoid vendor-specific branding. No "Google level" terms.
- Every assigned score MUST be justified by at least one concrete evidence entry.
- Reproducibility: include steps or cite README sections; if missing, explicitly note.

Rendering pipeline:
- Preferred path: Fill agent_evaluation.json (10-point per rubric item) + run scripts/aggregate_takehome_from_agent.py to render executive-grade Markdown.
- Direct authoring of Markdown is acceptable if all evidence and checklists are complete, but JSON is recommended for consistency.


## Agent Prompt Reference
- Use: ai_docs/prompts/hiring/takehome_evaluation_prompt.md
- Agents MUST follow this prompt to produce the executive-grade report aligned with Gefjon Platform Engineering Standards.

## Code-First Evidence Policy & Penalties
- Primary evidence MUST be code or test artifacts. README may only serve as supporting evidence for Documentation & DX and reproducibility.
- Forbidden as sole evidence for engineering criteria (Functional Correctness, Code Quality, Testing, Ownership, Scalability, Quantitative):
  - README excerpts alone
  - Package manager/tool choice alone (e.g., uv, poetry, Gradle)
  - Architecture docs/diagrams without corresponding code references
- Penalty caps when only non-code evidence is provided for a criterion:
  - Code Quality & Best Practices: max 2/5
  - Functional Correctness & Completeness: max 2/5
  - Testing Approach & Coverage: max 2/5
  - Ownership & Proactivity: max 2/5
  - Scalability & Design Patterns: max 2.5/5
  - Quantitative & Logical Problem Solving: max 2/5
- Every score must include at least one code reference: path:lineStart-lineEnd @ commitShort — short note.
