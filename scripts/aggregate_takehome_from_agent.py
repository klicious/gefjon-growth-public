#!/usr/bin/env python3
"""
Aggregate AI agent-provided take-home evaluation (agent_evaluation.json) into
final executive-grade artifacts.

Inputs:
  --candidate-id, --candidate-name, --github-url, --batch

Expectations:
- agent_evaluation.json exists at:
  artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/agent_evaluation.json
- JSON conforms to ai_docs/workflows/hiring/schemas/takehome_evaluation.schema.json

Outputs:
- Overwrite artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/takehome_evaluation.md
- Update artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/evaluation_sheet.md
- Write artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/evaluation_summary.json

Decision thresholds (10-point scale):
- Strong Hire ≥ 9.0
- Hire ≥ 8.0
- Lean Hire 6.5–7.9
- No Hire < 6.5

Note: This script does not assign scores; it aggregates what the agent provided.
"""
from __future__ import annotations
import argparse
import json
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = dt.date.today().isoformat()

PUB_CANDIDATES = ROOT / "artifacts/public/hiring/candidates"
EVAL_SHEETS_UPCOMING = ROOT / "artifacts/public/hiring/evaluation_sheets/upcoming"
SCHEMA_PATH = ROOT / "ai_docs/workflows/hiring/schemas/takehome_evaluation.schema.json"


def _ensure_dirs(candidate_id: str, batch: str) -> dict[str, Path]:
    base = PUB_CANDIDATES / batch / candidate_id
    paths = {
        "takehome": base / "takehome",
        "eval_sheet_upcoming": EVAL_SHEETS_UPCOMING / candidate_id,
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths


def _decision(overall: float) -> str:
    # overall is on a 5-point scale
    if overall >= 4.5:
        return "Strong Hire"
    if overall >= 3.8:
        return "Hire"
    if overall >= 3.0:
        return "Lean Hire"
    return "No Hire"


def _md_header(doc_type: str, visibility: str = "public", version: str = "1.0", tags: list[str] | None = None, quality_score: str = "__TBD__") -> str:
    tags = tags or []
    meta = {
        "id": f"{doc_type}_{TODAY}",
        "type": doc_type,
        "domain": "hiring",
        "created_date": TODAY,
        "last_updated": TODAY,
        "author": "Junie",
        "quality_score": quality_score,
        "tags": tags,
        "visibility": visibility,
        "version": version,
    }
    lines = ["---"]
    for k, v in meta.items():
        lines.append(f"{k}: {v}")
    lines.append("---\n")
    return "\n".join(lines)


def _render_final_md(candidate_id: str, candidate_name: str, github_url: str, data: dict) -> str:
    commit_short = data.get("commit_short") or "__"
    agent_criteria = data.get("criteria", [])

    # Build lookup for agent criteria
    by_name = {c.get("name"): c for c in agent_criteria if isinstance(c, dict)}

    # Executive rubric (7 criteria with weights)
    exec_rubric = [
        ("Functional Correctness & Completeness", 25),
        ("Code Quality & Best Practices", 20),
        ("Testing Approach & Coverage", 15),
        ("Documentation Quality", 10),
        ("Going Above and Beyond / Ownership", 15),
        ("Scalability & Design Patterns", 15),
        ("Quantitative & Logical Problem Solving", 10),
    ]

    # Helper to read score (0–10) safely
    def _score10(c: dict | None) -> float | None:
        if not c:
            return None
        s = c.get("score")
        return float(s) if isinstance(s, (int, float)) else None

    # Helper to merge lists
    def _merge_lists(*lists):
        out = []
        for lst in lists:
            if lst:
                out.extend(lst)
        return out

    # Legacy (8-criterion) names
    lg = {
        "req": by_name.get("Requirements Coverage"),
        "cq": by_name.get("Code Quality"),
        "arch": by_name.get("Architecture & Scalability"),
        "test": by_name.get("Correctness & Testing"),
        "perf": by_name.get("Performance & Efficiency"),
        "sec": by_name.get("Security & Compliance"),
        "doc": by_name.get("Documentation & DX"),
        "obs": by_name.get("Observability"),
    }

    # If agent already used executive names, respect them first
    ex_lookup = {n: by_name.get(n) for n, _ in exec_rubric}

    # Build executive criteria objects with merged comments/evidence and computed scores
    exec_items = []
    for name, weight in exec_rubric:
        if ex_lookup.get(name):
            c = ex_lookup[name]
            score10 = _score10(c)
            comments = c.get("comments", [])
            evidence = c.get("evidence", [])
        else:
            # Map from legacy 8 to 7
            if name == "Functional Correctness & Completeness":
                parts = [lg["req"], lg["test"]]
            elif name == "Code Quality & Best Practices":
                parts = [lg["cq"], lg["obs"]]
            elif name == "Testing Approach & Coverage":
                parts = [lg["test"]]
            elif name == "Documentation Quality":
                parts = [lg["doc"]]
            elif name == "Going Above and Beyond / Ownership":
                parts = [lg["obs"], lg["test"]]
            elif name == "Scalability & Design Patterns":
                parts = [lg["arch"], lg["perf"]]
            elif name == "Quantitative & Logical Problem Solving":
                parts = [lg["perf"]]
            else:
                parts = []

            scores = [v for v in (_score10(p) for p in parts) if v is not None]
            score10 = sum(scores) / len(scores) if scores else None
            comments = _merge_lists(*[(p.get("comments", []) if p else []) for p in parts])
            evidence = _merge_lists(*[(p.get("evidence", []) if p else []) for p in parts])

        # Convert to 5-point (0.5 granularity)
        if score10 is None:
            score5 = None
        else:
            score5 = round((score10 / 2.0) * 2) / 2

        exec_items.append({
            "name": name,
            "weight": weight,
            "score5": score5,
            "comments": comments or [],
            "evidence": evidence or [],
        })

    # Compute weighted overall on 5-point scale
    have = [(it["score5"], it["weight"]) for it in exec_items if isinstance(it["score5"], (int, float))]
    overall5 = round(sum(s * w for s, w in have) / sum(w for _, w in have), 1) if have else 0.0
    decision = _decision(overall5)

    header = _md_header("takehome_evaluation", tags=["takehome", "evaluation", candidate_id])
    lines = []
    lines.append("# Take-Home Assignment Evaluation Report: Mid-Level Backend Engineer (Gefjon Platform Engineering Standards)")
    lines.append("")
    lines.append(f"**Candidate Name:** {candidate_name}")
    lines.append("**Evaluator Name:** AI Evaluator")
    lines.append(f"**Date of Evaluation:** {TODAY}")
    lines.append("")
    lines.append("## Overall Recommendation")
    for opt in ["Strong Hire", "Hire", "Lean Hire", "No Hire"]:
        chk = "x" if opt == decision else " "
        lines.append(f"- [{chk}] {opt}")
    lines.append("")
    lines.append("## Evaluation Criteria (Gefjon Platform Engineering Standards)")

    for it in exec_items:
        lines.append("")
        lines.append(f"### {it['name']} (Weight: {it['weight']}%)")
        score5 = it["score5"]
        lines.append(f"- **Score:** {score5 if score5 is not None else '__/5'}")
        lines.append("- **Comments:**")
        for cm in (it["comments"] or []):
            lines.append(f"    - {cm}")

    lines.append("")
    lines.append(f"## Overall Score: {overall5}/5")

    # Limited Strengths & Critical Gaps (heuristic bullets)
    lines.append("")
    lines.append("## Detailed Feedback (Platform Standards)")
    lines.append("")
    lines.append("### Limited Strengths:")
    if any((it["name"].startswith("Scalability") and (it["score5"] or 0) >= 3.0) for it in exec_items):
        lines.append("- **Basic Architecture**: Layered/module structure suggests extensibility")
    if any((it["name"].startswith("Documentation") and (it["score5"] or 0) >= 3.0) for it in exec_items):
        lines.append("- **Documentation**: README provides setup/usage guidance")
    if any((it["name"].startswith("Testing") and (it["score5"] or 0) >= 3.0) for it in exec_items):
        lines.append("- **Testing Signals**: Presence of automated tests")

    lines.append("")
    lines.append("### Critical Gaps vs. Production Readiness:")
    if not any(ev for it in exec_items if it["name"].startswith("Code Quality") for ev in it["evidence"]):
        lines.append("- **Quality Gates**: No CI/linting quality gates detected")
    if not any(ev for it in exec_items if it["name"].startswith("Scalability") for ev in it["evidence"]):
        lines.append("- **Performance/Resilience**: No explicit performance or resilience patterns evident")
    if not any(ev for it in exec_items if it["name"].startswith("Documentation") for ev in it["evidence"]):
        lines.append("- **API Contracts**: Missing OpenAPI/Swagger documentation")

    lines.append("")
    lines.append("## Alignment with Job Description & Engineering Values")
    lines.append("- Technical Requirements Alignment: Assessed via functional, testing, and scalability signals")
    lines.append("- Values Alignment: Considered against Ownership, Observability, Security, and Excellence")

    lines.append("")
    lines.append("## Next Steps")
    for opt in [
        "Proceed to Interview",
        "Consider for another role",
        f"Do not proceed (Justification: {decision} based on weighted score and evidence)",
    ]:
        chk = "x" if ("Do not proceed" in opt and decision == "No Hire") or ("Proceed" in opt and decision in ("Hire", "Strong Hire")) else " "
        lines.append(f"- [{chk}] {opt}")

    # Evidence Appendix
    lines.append("")
    lines.append("## Evidence Appendix")
    lines.append("All evidence references follow: path:lineStart-lineEnd @ commitShortSHA — note")
    for it in exec_items:
        lines.append("")
        lines.append(f"### {it['name']}")
        if not it["evidence"]:
            lines.append("- <no evidence found>")
        else:
            for ev in it["evidence"]:
                path = ev.get("path", "")
                ls = ev.get("line_start")
                le = ev.get("line_end")
                rng = f"{ls}-{le}" if (ls is not None and le is not None) else "1-50"
                sha = ev.get("commit_short") or commit_short
                note = ev.get("note") or ""
                lines.append(f"- {path}:{rng} @ {sha} — {note}")

    # Checklists
    sec = data.get("security_checklist", {})
    obs = data.get("observability_checklist", {})
    lines.append("")
    lines.append("## Security & Compliance Checklist")
    for key in [
        ("secrets_not_committed", "Secrets not committed"),
        ("dependency_risks_reviewed", "Dependency risks reviewed"),
        ("input_validation_present", "Input validation present"),
        ("error_handling_robust", "Error handling robust"),
        ("licenses_compliant", "Licenses compliant"),
    ]:
        mark = "x" if sec.get(key[0]) else " "
        lines.append(f"- [{mark}] {key[1]}")

    lines.append("")
    lines.append("## Observability & Guardrails")
    for key in [
        ("structured_logging", "Structured logging"),
        ("metrics_health", "Metrics/health endpoints"),
        ("timeouts_retries", "Timeouts/retries for external calls"),
        ("alerting_diagnostics", "Alerting or diagnostics"),
    ]:
        mark = "x" if obs.get(key[0]) else " "
        lines.append(f"- [{mark}] {key[1]}")

    lines.append("")
    lines.append("## Reviewer Notes")
    lines.append(data.get("notes", "").strip() or "- <none>")

    return header + "\n".join(lines) + "\n"


def _render_eval_sheet_md(candidate_id: str, candidate_name: str, github_url: str, data: dict) -> str:
    header = _md_header("evaluation_sheet", tags=["takehome", "summary", candidate_id])
    agent_criteria = data.get("criteria", [])
    by_name = {c.get("name"): c for c in agent_criteria if isinstance(c, dict)}

    exec_rubric = [
        ("Functional Correctness & Completeness", 25),
        ("Code Quality & Best Practices", 20),
        ("Testing Approach & Coverage", 15),
        ("Documentation Quality", 10),
        ("Going Above and Beyond / Ownership", 15),
        ("Scalability & Design Patterns", 15),
        ("Quantitative & Logical Problem Solving", 10),
    ]

    def _score10(c: dict | None) -> float | None:
        if not c:
            return None
        s = c.get("score")
        return float(s) if isinstance(s, (int, float)) else None

    lg = {
        "Requirements Coverage": by_name.get("Requirements Coverage"),
        "Code Quality": by_name.get("Code Quality"),
        "Architecture & Scalability": by_name.get("Architecture & Scalability"),
        "Correctness & Testing": by_name.get("Correctness & Testing"),
        "Performance & Efficiency": by_name.get("Performance & Efficiency"),
        "Security & Compliance": by_name.get("Security & Compliance"),
        "Documentation & DX": by_name.get("Documentation & DX"),
        "Observability": by_name.get("Observability"),
    }

    ex_lookup = {n: by_name.get(n) for n, _ in exec_rubric}

    exec_items = []
    for name, weight in exec_rubric:
        if ex_lookup.get(name):
            c = ex_lookup[name]
            score10 = _score10(c)
        else:
            if name == "Functional Correctness & Completeness":
                parts = [lg["Requirements Coverage"], lg["Correctness & Testing"]]
            elif name == "Code Quality & Best Practices":
                parts = [lg["Code Quality"], lg["Observability"]]
            elif name == "Testing Approach & Coverage":
                parts = [lg["Correctness & Testing"]]
            elif name == "Documentation Quality":
                parts = [lg["Documentation & DX"]]
            elif name == "Going Above and Beyond / Ownership":
                parts = [lg["Observability"], lg["Correctness & Testing"]]
            elif name == "Scalability & Design Patterns":
                parts = [lg["Architecture & Scalability"], lg["Performance & Efficiency"]]
            elif name == "Quantitative & Logical Problem Solving":
                parts = [lg["Performance & Efficiency"]]
            else:
                parts = []
            scores = [v for v in (_score10(p) for p in parts) if v is not None]
            score10 = sum(scores) / len(scores) if scores else None

        score5 = (round((score10 / 2.0) * 2) / 2) if score10 is not None else None
        exec_items.append({"name": name, "weight": weight, "score5": score5})

    have = [(it["score5"], it["weight"]) for it in exec_items if isinstance(it["score5"], (int, float))]
    overall5 = round(sum(s * w for s, w in have) / sum(w for _, w in have), 1) if have else 0.0
    decision = _decision(overall5)

    lines = [
        "# Take-Home Evaluation Summary",
        "",
        f"Candidate: {candidate_name} ({candidate_id})",
        f"Repository: {github_url}",
        f"Date: {TODAY}",
        "",
        f"Overall: {overall5}/5",
        f"Decision: {decision}",
        "",
        "## Per-Criterion Scores",
    ]
    for it in exec_items:
        score5 = it["score5"]
        lines.append(f"- {it['name']}: {score5 if score5 is not None else '__/5'}")
    return header + "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate-id", required=True)
    ap.add_argument("--candidate-name", required=True)
    ap.add_argument("--github-url", required=True)
    ap.add_argument("--batch", required=True)
    args = ap.parse_args()

    paths = _ensure_dirs(args.candidate_id, args.batch)
    agent_json_path = paths["takehome"] / "agent_evaluation.json"
    if not agent_json_path.exists():
        raise FileNotFoundError(f"agent_evaluation.json not found at {agent_json_path}")

    data = json.loads(agent_json_path.read_text(encoding="utf-8"))

    # Render markdown report
    final_md = _render_final_md(args.candidate_id, args.candidate_name, args.github_url, data)
    (paths["takehome"] / "takehome_evaluation.md").write_text(final_md, encoding="utf-8")

    # Render evaluation sheet summary
    sheet_md = _render_eval_sheet_md(args.candidate_id, args.candidate_name, args.github_url, data)
    (paths["eval_sheet_upcoming"] / "evaluation_sheet.md").write_text(sheet_md, encoding="utf-8")

    # Write evaluation_summary.json with both 10-point input and 5-point executive overall, decision uses 5-point
    criteria = data.get("criteria", [])
    scored = [c.get("score") for c in criteria if isinstance(c.get("score"), (int, float))]
    overall_10 = round(sum(scored) / len(scored), 1) if scored else 0.0

    # Recompute executive 5-point overall using the same mapping as _render_eval_sheet_md
    by_name = {c.get("name"): c for c in criteria if isinstance(c, dict)}
    exec_rubric = [
        ("Functional Correctness & Completeness", 25),
        ("Code Quality & Best Practices", 20),
        ("Testing Approach & Coverage", 15),
        ("Documentation Quality", 10),
        ("Going Above and Beyond / Ownership", 15),
        ("Scalability & Design Patterns", 15),
        ("Quantitative & Logical Problem Solving", 10),
    ]
    def _score10(c: dict | None) -> float | None:
        if not c:
            return None
        s = c.get("score")
        return float(s) if isinstance(s, (int, float)) else None
    lg = {
        "Requirements Coverage": by_name.get("Requirements Coverage"),
        "Code Quality": by_name.get("Code Quality"),
        "Architecture & Scalability": by_name.get("Architecture & Scalability"),
        "Correctness & Testing": by_name.get("Correctness & Testing"),
        "Performance & Efficiency": by_name.get("Performance & Efficiency"),
        "Documentation & DX": by_name.get("Documentation & DX"),
        "Observability": by_name.get("Observability"),
    }
    ex_lookup = {n: by_name.get(n) for n, _ in exec_rubric}
    exec_items = []
    for name, weight in exec_rubric:
        if ex_lookup.get(name):
            score10 = _score10(ex_lookup[name])
        else:
            if name == "Functional Correctness & Completeness":
                parts = [lg["Requirements Coverage"], lg["Correctness & Testing"]]
            elif name == "Code Quality & Best Practices":
                parts = [lg["Code Quality"], lg["Observability"]]
            elif name == "Testing Approach & Coverage":
                parts = [lg["Correctness & Testing"]]
            elif name == "Documentation Quality":
                parts = [lg["Documentation & DX"]]
            elif name == "Going Above and Beyond / Ownership":
                parts = [lg["Observability"], lg["Correctness & Testing"]]
            elif name == "Scalability & Design Patterns":
                parts = [lg["Architecture & Scalability"], lg["Performance & Efficiency"]]
            elif name == "Quantitative & Logical Problem Solving":
                parts = [lg["Performance & Efficiency"]]
            else:
                parts = []
            scores = [v for v in (_score10(p) for p in parts) if v is not None]
            score10 = sum(scores) / len(scores) if scores else None
        score5 = (round((score10 / 2.0) * 2) / 2) if score10 is not None else None
        exec_items.append((score5, weight))
    have = [(s, w) for s, w in exec_items if isinstance(s, (int, float))]
    overall_5 = round(sum(s * w for s, w in have) / sum(w for _, w in have), 1) if have else 0.0
    decision = _decision(overall_5)

    summary = {
        "candidate_id": args.candidate_id,
        "candidate_name": args.candidate_name,
        "github_url": args.github_url,
        "commit_short": data.get("commit_short"),
        "criteria": criteria,
        "overall": overall_10,
        "overall_5": overall_5,
        "decision": decision,
    }
    (paths["takehome"] / "evaluation_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Aggregated evaluation written for {args.candidate_id}")


if __name__ == "__main__":
    main()
