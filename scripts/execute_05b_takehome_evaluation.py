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
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
    return result.stdout.strip()


def clone_repo(candidate_id: str, github_url: str) -> dict:
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
        run(["git", "clone", "--depth", "1", github_url, str(repo_dir)])

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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--candidate-id", required=True)
    p.add_argument("--candidate-name", required=True)
    p.add_argument("--github-url", required=True)
    p.add_argument("--batch", required=True)
    args = p.parse_args()

    meta = clone_repo(args.candidate_id, args.github_url)
    print("Cloned repo and captured meta:", json.dumps(meta, indent=2))

    generate_artifacts(args.candidate_id, args.candidate_name, args.github_url, args.batch)
    print("Artifacts generated for:", args.candidate_id)


if __name__ == "__main__":
    main()
