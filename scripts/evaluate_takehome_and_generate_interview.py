#!/usr/bin/env python3
"""
Minimal generator for Take-Home evaluation artifacts and BEI interview kits.

Purpose:
- Create rubric-based evaluation and interview materials aligned with ai_docs/workflows/hiring/orchestrator.md (v2.0).
- Avoid external network dependencies; reference GitHub URLs explicitly.

Usage:
  python scripts/evaluate_takehome_and_generate_interview.py \
    --candidate-id nova_002_nova-cand \
    --candidate-name "nova-cand" \
    --github-url "https://github.com/example-user/BitMex-Binance-REST-API" \
    --batch "20250811_consolidated"

  python scripts/evaluate_takehome_and_generate_interview.py \
    --candidate-id phoenix_005_phoenix-cand \
    --candidate-name "phoenix-cand" \
    --github-url "https://github.com/jyp-on/the firm" \
    --batch "20250811_consolidated"

This script writes files under:
- artifacts/public/hiring/candidates/{batch}/{candidate_id}/{takehome, evaluation, interview}/
- artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/

All generated files include metadata headers required by JUNIE.md.
"""
from __future__ import annotations
import argparse
import datetime as dt
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
PUB_CANDIDATES = ROOT / "artifacts/public/hiring/candidates"
INTERVIEW_UPCOMING = ROOT / "artifacts/public/hiring/interview_materials/upcoming"
EVAL_SHEETS_UPCOMING = ROOT / "artifacts/public/hiring/evaluation_sheets/upcoming"

TODAY = dt.date.today().isoformat()

CORE_VALUES = [
    "Technical Excellence & Scalable Elegance",
    "Customer-Centric Craftsmanship",
    "Ownership & Proactivity",
    "Observability & Guardrails",
    "Data-Informed Iteration",
    "Integrity & Reliability",
    "Security & Compliance First",
    "Collaboration & Knowledge-Sharing",
    "Continuous Learning & Mentorship",
    "Innovative Spirit",
]

TAKEHOME_RUBRIC = [
    ("Requirements Coverage", "How fully the solution meets the assignment requirements, edge cases, and spec."),
    ("Code Quality", "Readability, structure, naming, decomposition, comments, linting."),
    ("Architecture & Scalability", "Modularity, separation of concerns, scalability considerations."),
    ("Correctness & Testing", "Functional correctness, presence/quality of tests, CI readiness."),
    ("Performance & Efficiency", "Efficiency of critical paths, handling of rate limits/timeouts, resource usage."),
    ("Security & Compliance", "Secrets handling, dependencies, input validation, error handling, license compliance."),
    ("Documentation & DX", "README quality, setup steps, clarity of usage, API docs."),
    ("Observability", "Logging, metrics, traceability, diagnostics."),
]

STAR_GUIDANCE = """
For each question, probe using STAR:
- Situation: Context and constraints
- Task: Objective and role
- Action: Specific steps taken
- Result: Outcome, metrics, learnings
Follow-ups: What would you do differently? How did you validate success? What guardrails were in place?
""".strip()


def _md_header(doc_type: str, visibility: str = "public", version: str = "1.0", tags: list[str] | None = None, quality_score: str = "__TBD__") -> str:
    tags = tags or []
    header = {
        "id": f"{doc_type}_{TODAY}",
        "type": doc_type,
        "domain": "hiring",
        "created_date": TODAY,
        "last_updated": TODAY,
        "author": "Junie",
        "quality_score": f"{quality_score}",
        "tags": tags,
        "visibility": visibility,
        "version": version,
    }
    pairs = [f"{k}: {header[k]}" if not isinstance(header[k], list) else f"{k}: {header[k]}" for k in header]
    return "---\n" + "\n".join(pairs) + "\n---\n\n"


def ensure_dirs(candidate_id: str, batch: str) -> dict[str, Path]:
    base = PUB_CANDIDATES / batch / candidate_id
    paths = {
        "base": base,
        "takehome": base / "takehome",
        "evaluation": base / "evaluation",
        "interview": base / "interview",
        "interview_upcoming": INTERVIEW_UPCOMING / candidate_id,
        "eval_sheets_upcoming": EVAL_SHEETS_UPCOMING / candidate_id,
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths


def build_evaluation_framework_md(candidate_id: str, candidate_name: str, github_url: str) -> str:
    header = _md_header("evaluation_framework", tags=["takehome", "rubric", candidate_id])
    body = f"""
# Take-Home Evaluation Framework

Candidate: {candidate_name} ({candidate_id})
Repository: {github_url}

Scoring: 1–10 per criterion (0.5 granularity allowed). Thresholds: Strong Hire ≥ 9.0, Hire ≥ 8.0, Lean Hire 6.5–7.9, No Hire < 6.5.

## Criteria & Notes
"""
    for name, desc in TAKEHOME_RUBRIC:
        body += f"\n### {name}\n- Description: {desc}\n- Score: __/10\n- Evidence: <add concrete references: files, lines, commits>\n"
    body += "\n## Overall Recommendation\n- Preliminary decision: __Strong Hire|Hire|Lean Hire|No Hire__\n- Rationale: <concise evidence-based rationale>\n- Risks & Mitigations: <list>\n"
    return header + body


def build_takehome_evaluation_md(candidate_id: str, candidate_name: str, github_url: str) -> str:
    header = _md_header("takehome_evaluation", tags=["takehome", "evaluation", candidate_id])
    body = f"""
# Take-Home Assignment Evaluation

Candidate: {candidate_name} ({candidate_id})
Repository: {github_url}
Date: {TODAY}

This evaluation follows the orchestrator Stage 5 rubric and quality gates. All scores are provisional until review approval.

## Summary
- Overall Score: __/10
- Decision: __Strong Hire|Hire|Lean Hire|No Hire__
- Key Strengths: <bullets>
- Improvement Areas: <bullets>

## Detailed Scoring & Evidence
"""
    for name, desc in TAKEHOME_RUBRIC:
        body += f"\n### {name}\n- Score: __/10\n- Evidence: <files/lines/commits>\n- Commentary: {desc}\n"
    body += f"""

## Security & Compliance Checklist
- [ ] Secrets not committed
- [ ] Dependency risks reviewed
- [ ] Input validation present
- [ ] Error handling robust
- [ ] Licenses compliant

## Observability & Guardrails
- [ ] Structured logging
- [ ] Metrics/health endpoints
- [ ] Timeouts/retries for external calls
- [ ] Alerting or diagnostics

## Reviewer Notes
- Additional comments: <text>
- Follow-up questions: <bullets>
"""
    return header + body


def build_candidate_context_md(candidate_id: str, candidate_name: str, github_url: str) -> str:
    header = _md_header("candidate_context", tags=["interview", "bei", candidate_id])
    body = f"""
# Candidate Context & Value Gap Analysis

Candidate: {candidate_name} ({candidate_id})
Repository for review: {github_url}

## Executive Briefing
- Role Fit: <summary>
- Experience Highlights: <bullets>
- Risks to probe: <bullets>

## Core Values Mapping (PROVEN / SUGGESTED / MISSING)
"""
    for v in CORE_VALUES:
        body += f"\n- {v}: __PROVEN|SUGGESTED|MISSING__  — Evidence: <specific examples from resume/screening/take-home>"
    body += "\n\n## Interview Strategy\n- Priorities: <values to verify/deepen>\n- Time allocation: 50–60 minutes BEI, total 90–120 minutes\n"
    return header + body


def build_interview_guide_md(candidate_id: str, candidate_name: str) -> str:
    header = _md_header("interview_guide", tags=["interview", "bei", candidate_id])
    body = f"""
# BEI Interview Guide

Candidate: {candidate_name} ({candidate_id})

## Structure
- Total: 90–120 minutes
- BEI Focus: 50–60 minutes (min 2 values per 15 minutes)
- Technical Deep-Dive aligned with demonstrated skills

## BEI Value-by-Value Focus
"""
    for v in CORE_VALUES:
        body += f"\n### {v}\n- What to verify: <behavioral indicators>\n- Red flags: <language/risk patterns>\n- Evidence to confirm: <from materials>\n- STAR questions: see interview_script.md\n"
    body += "\n## Technical Assessment Calibration\n- Topics: <list based on take-home/experience>\n- Depth: <junior/mid/senior>\n- Success indicators: <bullets>\n"
    return header + body


def build_interview_script_md(candidate_id: str, candidate_name: str) -> str:
    header = _md_header("interview_script", tags=["interview", "bei", candidate_id])
    intro = f"""
# Interview Script (BEI – STAR)

Candidate: {candidate_name} ({candidate_id})

Instructions:
{STAR_GUIDANCE}
"""
    body = intro + "\n\n## Questions by Core Value\n"
    for v in CORE_VALUES:
        body += textwrap.dedent(f"""
        
        ### {v}
        1. Situation/Task: Tell me about a time you demonstrated "{v}" in a high-stakes context. What was your specific objective?
           - Follow-up: What guardrails or constraints shaped your approach?
        2. Action: Walk me through your decision-making and the concrete steps you took.
           - Follow-up: How did you balance trade-offs and risks?
        3. Result: What measurable outcomes did you achieve? How did you validate success?
           - Follow-up: In retrospect, what would you change and why?
        4. Transfer: How would you apply this behavior to our context at Gefjon?
        """)
    return header + body


def write_candidate_artifacts(candidate_id: str, candidate_name: str, github_url: str, batch: str) -> list[Path]:
    paths = ensure_dirs(candidate_id, batch)
    outputs: list[Path] = []

    # Evaluation framework and take-home evaluation
    eval_framework_md = build_evaluation_framework_md(candidate_id, candidate_name, github_url)
    takehome_eval_md = build_takehome_evaluation_md(candidate_id, candidate_name, github_url)

    (paths["evaluation"] / "evaluation_framework.md").write_text(eval_framework_md, encoding="utf-8")
    outputs.append(paths["evaluation"] / "evaluation_framework.md")

    (paths["takehome"] / "takehome_evaluation.md").write_text(takehome_eval_md, encoding="utf-8")
    outputs.append(paths["takehome"] / "takehome_evaluation.md")

    # BEI interview materials
    candidate_context_md = build_candidate_context_md(candidate_id, candidate_name, github_url)
    interview_guide_md = build_interview_guide_md(candidate_id, candidate_name)
    interview_script_md = build_interview_script_md(candidate_id, candidate_name)

    (paths["interview"] / "candidate_context.md").write_text(candidate_context_md, encoding="utf-8")
    (paths["interview"] / "interview_guide.md").write_text(interview_guide_md, encoding="utf-8")
    (paths["interview"] / "interview_script.md").write_text(interview_script_md, encoding="utf-8")

    outputs += [
        paths["interview"] / "candidate_context.md",
        paths["interview"] / "interview_guide.md",
        paths["interview"] / "interview_script.md",
    ]

    # Mirror to interview_materials/upcoming per orchestrator
    (paths["interview_upcoming"] / "candidate_context.md").write_text(candidate_context_md, encoding="utf-8")
    (paths["interview_upcoming"] / "interview_guide.md").write_text(interview_guide_md, encoding="utf-8")
    (paths["interview_upcoming"] / "interview_script.md").write_text(interview_script_md, encoding="utf-8")

    return outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--candidate-name", required=True)
    parser.add_argument("--github-url", required=True)
    parser.add_argument("--batch", required=True, help="e.g., 20250811_consolidated")
    args = parser.parse_args()

    outputs = write_candidate_artifacts(
        candidate_id=args.candidate_id,
        candidate_name=args.candidate_name,
        github_url=args.github_url,
        batch=args.batch,
    )

    print("Generated files:")
    for p in outputs:
        print(" -", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
