#!/usr/bin/env python3
"""
Consolidate hiring results into single candidate directories
Following the enhanced workflow configuration
"""

import os
import json
import shutil
from pathlib import Path
import re

def normalize_name(name):
    """Normalize candidate name for directory naming"""
    return re.sub(r'[^a-zA-Z0-9]', '_', name.lower())

def create_candidate_directory_structure(base_path, candidate_id, candidate_name):
    """Create standardized directory structure for a candidate"""
    normalized_name = normalize_name(candidate_name)
    candidate_dir = base_path / f"{candidate_id}_{normalized_name}"
    
    # Create subdirectories
    subdirs = ["screening", "takehome", "interview", "evaluation", "communication"]
    for subdir in subdirs:
        (candidate_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    return candidate_dir

def consolidate_candidate_files(candidate_id, candidate_name, candidate_dir):
    """Consolidate all files for a candidate into their directory"""
    
    # Source directories to check
    source_dirs = [
        Path("artifacts/public/hiring/evaluation_sheets/upcoming") / candidate_id,
        Path("artifacts/public/hiring/interview_materials/upcoming") / candidate_id,
        Path("artifacts/public/hiring/takehome_assignment/upcoming") / candidate_id
    ]
    
    files_moved = []
    
    for source_dir in source_dirs:
        if source_dir.exists():
            for file_path in source_dir.rglob("*"):
                if file_path.is_file():
                    # Determine target subdirectory based on file type
                    if "screening" in file_path.name or "screening" in str(file_path.parent):
                        target_subdir = "screening"
                    elif "takehome" in file_path.name or "assignment" in file_path.name or "evaluation_sheet" in file_path.name:
                        target_subdir = "takehome"
                    elif "interview" in file_path.name or "candidate_context" in file_path.name:
                        target_subdir = "interview"
                    else:
                        target_subdir = "evaluation"
                    
                    target_path = candidate_dir / target_subdir / file_path.name
                    
                    # Copy file to new location
                    shutil.copy2(file_path, target_path)
                    files_moved.append({
                        "source": str(file_path),
                        "target": str(target_path),
                        "category": target_subdir
                    })
    
    return files_moved

def generate_candidate_summary(candidate_data, candidate_dir):
    """Generate a comprehensive summary for each candidate"""
    
    summary_content = f"""# Candidate Summary: {candidate_data['candidate_name']}

## Overview
- **Candidate ID**: {candidate_data['candidate_id']}
- **Name**: {candidate_data['candidate_name']}
- **Overall Score**: {candidate_data['overall_score']}/10
- **Recommendation**: {candidate_data['recommendation']}
- **Confidence**: {candidate_data['confidence']}
- **Next Step**: {candidate_data['next_step']}

## Key Strengths
{chr(10).join(f"- {strength}" for strength in candidate_data['key_strengths'])}

## Areas of Concern
{chr(10).join(f"- {concern}" for concern in candidate_data['areas_of_concern'])}

## Process Status
- ✅ Screening Completed
- {'✅' if (candidate_dir / 'takehome').exists() and list((candidate_dir / 'takehome').glob('*.md')) else '⏳'} Take-home Assignment
- {'✅' if (candidate_dir / 'interview').exists() and list((candidate_dir / 'interview').glob('*.md')) else '⏳'} Interview Materials
- ⏳ Final Evaluation

## Files Available
"""
    
    # List available files by category
    for subdir in ["screening", "takehome", "interview", "evaluation"]:
        subdir_path = candidate_dir / subdir
        if subdir_path.exists():
            files = list(subdir_path.glob("*.md"))
            if files:
                summary_content += f"\n### {subdir.title()}\n"
                for file_path in files:
                    summary_content += f"- {file_path.name}\n"
    
    # Write summary file
    summary_path = candidate_dir / "candidate_summary.md"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    return summary_path

def main():
    """Main consolidation function"""
    
    # Load screening results
    screening_file = Path("data/public/hiring/working/20250811_enhanced_run/screening_summary_complete.json")
    
    if not screening_file.exists():
        print(f"Screening summary file not found: {screening_file}")
        return
    
    with open(screening_file, 'r', encoding='utf-8') as f:
        screening_data = json.load(f)
    
    # Create base directory for consolidated results
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    base_path.mkdir(parents=True, exist_ok=True)
    
    consolidation_log = {
        "consolidation_date": "2025-08-11",
        "total_candidates": len(screening_data['screening_results']),
        "candidates_processed": [],
        "files_moved": 0,
        "errors": []
    }
    
    # Process each candidate
    for candidate_data in screening_data['screening_results']:
        try:
            candidate_id = candidate_data['candidate_id']
            candidate_name = candidate_data['candidate_name']
            
            print(f"Processing candidate: {candidate_id} - {candidate_name}")
            
            # Create candidate directory structure
            candidate_dir = create_candidate_directory_structure(base_path, candidate_id, candidate_name)
            
            # Consolidate files
            files_moved = consolidate_candidate_files(candidate_id, candidate_name, candidate_dir)
            
            # Generate candidate summary
            summary_path = generate_candidate_summary(candidate_data, candidate_dir)
            
            consolidation_log["candidates_processed"].append({
                "candidate_id": candidate_id,
                "candidate_name": candidate_name,
                "directory": str(candidate_dir),
                "files_moved": len(files_moved),
                "summary_generated": str(summary_path)
            })
            
            consolidation_log["files_moved"] += len(files_moved)
            
            print(f"  ✅ Processed {len(files_moved)} files")
            
        except Exception as e:
            error_msg = f"Error processing {candidate_id}: {str(e)}"
            print(f"  ❌ {error_msg}")
            consolidation_log["errors"].append(error_msg)
    
    # Save consolidation log
    log_path = base_path / "consolidation_log.json"
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(consolidation_log, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Consolidation complete!")
    print(f"📁 Results saved to: {base_path}")
    print(f"📊 Processed {consolidation_log['total_candidates']} candidates")
    print(f"📄 Moved {consolidation_log['files_moved']} files")
    print(f"📋 Log saved to: {log_path}")

if __name__ == "__main__":
    main()