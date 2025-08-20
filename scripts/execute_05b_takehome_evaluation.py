#!/usr/bin/env python3
"""
Execute Task 5b (Take-Home Assignment Evaluation) end-to-end for a single candidate:
- Clone the candidate's GitHub repository into data/private/hiring/repositories/{candidate_id}/repo
- Capture default branch and HEAD commit SHA
- Write repo meta to data/private/hiring/repositories/{candidate_id}/repo_meta.json
- Generate evaluation artifacts via scripts/evaluate_takehome_and_generate_interview.py

Usage:
  python scripts/execute_05b_takehome_evaluation.py \
    --candidate-id nova_002_nova-cand \
    --candidate-name "nova-cand" \
    --github-url "https://github.com/example-user/BitMex-Binance-REST-API" \
    --batch "20250811_consolidated"

Notes:
- Network access and git must be available.
- This script does not evaluate code automatically; it prepares artifacts and ensures reproducibility data for evidence-based scoring.
"""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path
import datetime as dt

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_BASE = ROOT / "data/private/hiring/repositories"
EVAL_SCRIPT = ROOT / "scripts/evaluate_takehome_and_generate_interview.py"
TODAY = dt.date.today().isoformat()


def run(cmd: list[str], cwd: Path | None = None) -> str:
    import os
    env = os.environ.copy()
    # Ensure git never prompts for credentials in non-interactive environment
    env.update({
        "GIT_TERMINAL_PROMPT": "0",
        "GCM_INTERACTIVE": "Never",
        "GIT_ASKPASS": "echo",
        # Auto-accept new host key for github.com to avoid interactive prompt on first SSH connect
        "GIT_SSH_COMMAND": "ssh -o StrictHostKeyChecking=accept-new",
    })
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
    return result.stdout.strip()


def clone_repo(candidate_id: str, github_url: str) -> dict:
    def _to_ssh(url: str) -> str:
        if url.startswith("git@"):
            return url
        if url.startswith("https://github.com/"):
            path = url[len("https://github.com/"):]
            if path.endswith("/"):
                path = path[:-1]
            if path.endswith(".git"):
                path = path[:-4]
            return f"git@github.com:{path}.git"
        return url
    clone_url = _to_ssh(github_url)
    base_dir = PRIVATE_BASE / candidate_id
    repo_dir = base_dir / "repo"
    base_dir.mkdir(parents=True, exist_ok=True)
    if repo_dir.exists():
        # If already cloned, fetch latest and reset to origin/HEAD
        try:
            run(["git", "fetch", "--all", "--prune"], cwd=repo_dir)
        except Exception:
            pass
    else:
        try:
            run(["git", "clone", "--depth", "1", clone_url, str(repo_dir)])
        except Exception as e:
            raise RuntimeError(
                f"Git clone failed using SSH URL '{clone_url}'. "
                f"Ensure your SSH key is configured and authorized on GitHub (test: ssh -T git@github.com).\n"
                f"Original error: {e}"
            )

    # Detect default branch
    # 'git remote show origin' prints 'HEAD branch: main' or similar
    remote_info = run(["git", "remote", "show", "origin"], cwd=repo_dir)
    default_branch = ""
    for line in remote_info.splitlines():
        if "HEAD branch:" in line:
            default_branch = line.split(":", 1)[1].strip()
            break
    if not default_branch:
        # Fallback to main/master check
        for b in ("main", "master"):
            try:
                run(["git", "rev-parse", f"origin/{b}"], cwd=repo_dir)
                default_branch = b
                break
            except Exception:
                continue
        if not default_branch:
            default_branch = run(["git", "symbolic-ref", "--short", "HEAD"], cwd=repo_dir)

    # Ensure we are on default branch
    try:
        run(["git", "checkout", default_branch], cwd=repo_dir)
    except Exception:
        pass

    # Capture HEAD commit SHA (short)
    commit_sha = run(["git", "rev-parse", "--short", "HEAD"], cwd=repo_dir)

    meta = {
        "candidate_id": candidate_id,
        "github_url": github_url,
        "clone_url": clone_url,
        "repo_local_path": str(repo_dir.relative_to(ROOT)),
        "default_branch": default_branch,
        "head_commit_short": commit_sha,
        "captured_at": TODAY,
    }

    with (base_dir / "repo_meta.json").open("w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    # Also write a small META.md to aid reviewers
    meta_md = f"""---
id: repo_meta_{candidate_id}
type: repo_meta
domain: hiring
created_date: {TODAY}
last_updated: {TODAY}
author: Junie
quality_score: 10/10
visibility: private
version: 1.0
---

# Repository Meta
- Candidate: {candidate_id}
- GitHub URL: {github_url}
- Clone URL (used): {clone_url}
- Local Path: {meta['repo_local_path']}
- Default Branch: {default_branch}
- HEAD Commit (short): {commit_sha}
"""
    (base_dir / "META.md").write_text(meta_md, encoding="utf-8")

    return meta


def generate_artifacts(candidate_id: str, candidate_name: str, github_url: str, batch: str) -> None:
    cmd = [
        "python",
        str(EVAL_SCRIPT),
        "--candidate-id", candidate_id,
        "--candidate-name", candidate_name,
        "--github-url", github_url,
        "--batch", batch,
    ]
    run(cmd, cwd=ROOT)


def _ensure_dirs(candidate_id: str, batch: str) -> dict:
    pub_base = ROOT / "artifacts/public/hiring/candidates" / batch / candidate_id
    paths = {
        "takehome": pub_base / "takehome",
        "eval_sheet_upcoming": ROOT / "artifacts/public/hiring/evaluation_sheets/upcoming" / candidate_id,
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths


def scaffold_agent_files(candidate_id: str, candidate_name: str, github_url: str, batch: str, commit_short: str | None) -> None:
    paths = _ensure_dirs(candidate_id, batch)
    # Agent evaluation template (Markdown)
    template_md = f"""---
id: agent_evaluation_template_{candidate_id}
type: agent_evaluation_template
domain: hiring
created_date: {TODAY}
last_updated: {TODAY}
author: Junie
quality_score: 10/10
tags: ['takehome','agent','template','{candidate_id}']
visibility: public
version: 1.0
---

# Agent Evaluation Template (Take-Home)

Candidate: {candidate_name} ({candidate_id})
Repository: {github_url}
Commit (short): {commit_short or '__'}
Date: {TODAY}

Instructions for AI Agent:
- Follow prompt: ai_docs/prompts/hiring/takehome_evaluation_prompt.md
- Fill each criterion with a Score (1–10, 0.5 granularity), concise Comments, and Evidence entries.
- Evidence must reference file path, lineStart-lineEnd, and commit short SHA.
- Maintain neutral, evidence-based language. Complete the checklists.
- Code-First Evidence Policy:
  DO:
    - Cite code/tests as primary evidence
    - Include path:lineStart-lineEnd @ commitShort — note
  DON'T:
    - Use README/config as sole evidence for engineering criteria
    - Use package manager choice (e.g., uv/poetry) as sole quality evidence
- Penalty caps when only non-code evidence exists:
  - Code Quality, Functional Correctness, Testing, Ownership: max 2/5
  - Scalability & Design Patterns: max 2.5/5
  - Quantitative & Logical Problem Solving: max 2/5

## Criteria (Executive 7-Category Rubric)
"""
    rubric_items = [
        "Functional Correctness & Completeness",
        "Code Quality & Best Practices",
        "Testing Approach & Coverage",
        "Documentation Quality",
        "Going Above and Beyond / Ownership",
        "Scalability & Design Patterns",
        "Quantitative & Logical Problem Solving",
    ]
    for item in rubric_items:
        template_md += f"\n### {item}\n- Score: __/10\n- Comments:\n  - <bullet>\n- Evidence:\n  - path:lineStart-lineEnd @ commitShort — note\n"

    template_md += "\n## Security & Compliance Checklist\n- [ ] Secrets not committed\n- [ ] Dependency risks reviewed\n- [ ] Input validation present\n- [ ] Error handling robust\n- [ ] Licenses compliant\n\n## Observability & Guardrails\n- [ ] Structured logging\n- [ ] Metrics/health endpoints\n- [ ] Timeouts/retries for external calls\n- [ ] Alerting or diagnostics\n\n## Overall Recommendation\n- [ ] Strong Hire\n- [ ] Hire\n- [ ] Lean Hire\n- [ ] No Hire\n\nRationale: <concise rationale>\n\n"
    tpl_path = paths["eval_sheet_upcoming"] / "agent_evaluation_template.md"
    if not tpl_path.exists():
        tpl_path.write_text(template_md, encoding="utf-8")

    # agent_evaluation.json stub
    stub = {
        "$schema": "ai_docs/workflows/hiring/schemas/takehome_evaluation.schema.json",
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "github_url": github_url,
        "commit_short": commit_short,
        "criteria": [
            {"name": n, "score": None, "comments": [], "evidence": []} for n in rubric_items
        ],
        "overall_recommendation": None,
        "notes": "",
    }
    agent_json_path = paths["takehome"] / "agent_evaluation.json"
    if not agent_json_path.exists():
        agent_json_path.write_text(json.dumps(stub, indent=2), encoding="utf-8")

    # Pending evaluation file
    pending_md = f"""---
id: takehome_evaluation_pending_{candidate_id}
type: takehome_evaluation
domain: hiring
created_date: {TODAY}
last_updated: {TODAY}
author: Junie
quality_score: __TBD__
tags: ['takehome','evaluation','pending','{candidate_id}']
visibility: public
version: 1.0
---

# Take-Home Assignment Evaluation — Pending AI Agent Input

Candidate: {candidate_name} ({candidate_id})
Repository: {github_url}
Commit (short): {commit_short or '__'}
Date: {TODAY}

Status: Waiting for AI Agent to complete agent_evaluation_template.md or agent_evaluation.json.

Next:
1) Agent fills artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/agent_evaluation_template.md and/or updates artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/agent_evaluation.json.
2) Run aggregator:
   python scripts/aggregate_takehome_from_agent.py \
     --candidate-id {candidate_id} \
     --candidate-name "{candidate_name}" \
     --github-url "{github_url}" \
     --batch "{batch}"
"""
    pending_path = paths["takehome"] / "takehome_evaluation.md"
    if not pending_path.exists():
        pending_path.write_text(pending_md, encoding="utf-8")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--candidate-id", required=True)
    p.add_argument("--candidate-name", required=True)
    p.add_argument("--github-url", required=True)
    p.add_argument("--batch", required=True)
    p.add_argument("--legacy-auto", action="store_true", help="Run legacy auto-evaluation generator (not recommended).")
    args = p.parse_args()

    meta = clone_repo(args.candidate_id, args.github_url)
    print("Cloned repo and captured meta:", json.dumps(meta, indent=2))

    # Always scaffold agent-first files
    scaffold_agent_files(args.candidate_id, args.candidate_name, args.github_url, args.batch, meta.get("head_commit_short"))
    print("Scaffolded agent evaluation template and stub for:", args.candidate_id)

    # Optionally run legacy generator for demo/back-compat
    if args.legacy_auto:
        generate_artifacts(args.candidate_id, args.candidate_name, args.github_url, args.batch)
        print("Legacy artifacts generated for:", args.candidate_id)


if __name__ == "__main__":
    main()
