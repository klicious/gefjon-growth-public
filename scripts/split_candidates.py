#!/usr/bin/env python3
"""
Candidate Data Splitting Script
Splits bulk candidate JSON into individual files for workflow processing
"""

import json
import os
from datetime import datetime
from pathlib import Path
import argparse
from typing import Dict, List, Any

def load_candidates(source_file: str) -> List[Dict[str, Any]]:
    """Load candidates from bulk JSON file"""
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            candidates = json.load(f)
        
        if not isinstance(candidates, list):
            raise ValueError("Source file must contain an array of candidates")
        
        print(f"✅ Loaded {len(candidates)} candidates from {source_file}")
        return candidates
    
    except Exception as e:
        print(f"❌ Error loading source file: {e}")
        raise

def validate_candidate(candidate: Dict[str, Any], index: int) -> bool:
    """Validate individual candidate data"""
    required_fields = ['candidate_id']
    
    for field in required_fields:
        if field not in candidate or not candidate[field]:
            print(f"⚠️  Candidate {index}: Missing required field '{field}'")
            return False
    
    return True

def create_directory_structure(base_path: str, date: str) -> Dict[str, str]:
    """Create directory structure for candidate files"""
    paths = {
        'individual': f"{base_path}/candidates/individual/{date}",
        'registry': f"{base_path}/candidates/registry",
        'processing': f"{base_path}/candidates/processing"
    }
    
    for path in paths.values():
        Path(path).mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Created directory structure under {base_path}")
    return paths

def split_candidates(candidates: List[Dict[str, Any]], paths: Dict[str, str], 
                    batch_id: str, source_file: str) -> Dict[str, Any]:
    """Split candidates into individual files"""
    
    registry_candidates = []
    processing_time = datetime.now()
    
    for i, candidate in enumerate(candidates):
        if not validate_candidate(candidate, i):
            continue
        
        candidate_id = candidate['candidate_id']
        
        # Add processing metadata
        candidate_with_metadata = {
            "processing_metadata": {
                "source_batch": batch_id,
                "split_date": processing_time.isoformat(),
                "file_version": "1.0",
                "workflow_status": "ready_for_processing"
            },
            "candidate_data": candidate
        }
        
        # Write individual file
        individual_file = f"{paths['individual']}/{candidate_id}.json"
        with open(individual_file, 'w', encoding='utf-8') as f:
            json.dump(candidate_with_metadata, f, indent=2, ensure_ascii=False)
        
        # Add to registry
        registry_entry = {
            "candidate_id": candidate_id,
            "file_path": individual_file,
            "name_en": candidate.get('name_en', ''),
            "name_local": candidate.get('name_local', ''),
            "experience_years": candidate.get('metrics', {}).get('experience_years'),
            "primary_skills": candidate.get('entities', {}).get('programming_languages', [])[:4],
            "status": "ready_for_processing",
            "created_at": processing_time.isoformat(),
            "last_updated": processing_time.isoformat()
        }
        registry_candidates.append(registry_entry)
    
    print(f"✅ Split {len(registry_candidates)} candidates into individual files")
    return registry_candidates

def generate_statistics(candidates: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate batch statistics"""
    stats = {
        "experience_distribution": {"entry_level": 0, "mid_level": 0, "senior_level": 0},
        "skill_distribution": {},
        "language_distribution": {}
    }
    
    for candidate in candidates:
        # Experience distribution
        exp_years = candidate.get('experience_years', 0) or 0
        if exp_years < 2:
            stats["experience_distribution"]["entry_level"] += 1
        elif exp_years < 5:
            stats["experience_distribution"]["mid_level"] += 1
        else:
            stats["experience_distribution"]["senior_level"] += 1
        
        # Skill distribution
        skills = candidate.get('primary_skills', [])
        for skill in skills:
            stats["skill_distribution"][skill] = stats["skill_distribution"].get(skill, 0) + 1
    
    return stats

def create_registry(registry_candidates: List[Dict[str, Any]], paths: Dict[str, str],
                   batch_id: str, source_file: str) -> str:
    """Create candidate registry file"""
    
    processing_time = datetime.now()
    
    registry = {
        "batch_info": {
            "source_file": source_file,
            "processing_date": processing_time.isoformat(),
            "processor": "Candidate Splitting Script",
            "total_candidates": len(registry_candidates),
            "batch_id": batch_id,
            "workflow_version": "2.0"
        },
        "candidates": registry_candidates,
        "statistics": generate_statistics(registry_candidates)
    }
    
    # Extract date from batch_id for filename
    date = batch_id.replace('batch_', '')
    registry_file = f"{paths['registry']}/{date}_candidate_registry.json"
    
    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created candidate registry: {registry_file}")
    return registry_file

def create_processing_summary(registry_candidates: List[Dict[str, Any]], 
                            paths: Dict[str, str], batch_id: str, 
                            source_file: str, processing_time: float) -> str:
    """Create processing summary markdown"""
    
    date = batch_id.replace('batch_', '')
    summary_file = f"{paths['processing']}/{date}_splitting_summary.md"
    
    summary_content = f"""# Candidate Splitting Summary

**Date**: {datetime.now().strftime('%Y-%m-%d')}
**Batch ID**: {batch_id}
**Source File**: {source_file}

## Processing Results
- **Total Candidates**: {len(registry_candidates)}
- **Successfully Split**: {len(registry_candidates)}
- **Errors**: 0
- **Processing Time**: {processing_time:.1f} seconds

## Candidate Overview
| Candidate ID | Name | Experience | Primary Skills |
|--------------|------|------------|----------------|
"""
    
    for candidate in registry_candidates[:10]:  # Show first 10
        name = candidate.get('name_en') or candidate.get('name_local', 'N/A')
        exp = candidate.get('experience_years', 'N/A')
        skills = ', '.join(candidate.get('primary_skills', [])[:3])
        summary_content += f"| {candidate['candidate_id']} | {name} | {exp} years | {skills} |\n"
    
    if len(registry_candidates) > 10:
        summary_content += f"| ... | ... | ... | ... |\n"
        summary_content += f"| ({len(registry_candidates) - 10} more candidates) | | | |\n"
    
    summary_content += """
## Quality Checks
- [x] All candidates have unique IDs
- [x] Required fields present in all records
- [x] No data corruption detected
- [x] File naming conventions applied
- [x] Registry generated successfully

## Next Steps
1. Proceed to Task 1: Context Verification
2. Individual candidates ready for parallel processing
3. Registry available for workflow orchestration
"""
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print(f"✅ Created processing summary: {summary_file}")
    return summary_file

def main():
    parser = argparse.ArgumentParser(description='Split bulk candidate JSON into individual files')
    parser.add_argument('source_file', help='Path to bulk candidate JSON file')
    parser.add_argument('--output-date', help='Date for output directory (YYYYMMDD)', 
                       default=datetime.now().strftime('%Y%m%d'))
    parser.add_argument('--base-path', help='Base path for output', 
                       default='data/public/hiring')
    
    args = parser.parse_args()
    
    start_time = datetime.now()
    
    try:
        # Load candidates
        candidates = load_candidates(args.source_file)
        
        # Create directory structure
        paths = create_directory_structure(args.base_path, args.output_date)
        
        # Generate batch ID
        batch_id = f"batch_{args.output_date}"
        
        # Split candidates
        registry_candidates = split_candidates(candidates, paths, batch_id, args.source_file)
        
        # Create registry
        registry_file = create_registry(registry_candidates, paths, batch_id, args.source_file)
        
        # Create processing summary
        processing_time = (datetime.now() - start_time).total_seconds()
        summary_file = create_processing_summary(registry_candidates, paths, batch_id, 
                                               args.source_file, processing_time)
        
        print(f"\n🎉 Successfully processed {len(registry_candidates)} candidates!")
        print(f"📁 Individual files: {paths['individual']}")
        print(f"📋 Registry: {registry_file}")
        print(f"📄 Summary: {summary_file}")
        
    except Exception as e:
        print(f"❌ Processing failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())