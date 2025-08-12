#!/usr/bin/env python3
"""
Complete workflow integration script
Ensures all candidate materials are generated and up-to-date
"""

import subprocess
import sys
from pathlib import Path
import json

def run_script(script_path, description):
    """Run a script and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, check=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def verify_candidate_materials():
    """Verify that all candidates have complete materials"""
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    
    if not base_path.exists():
        print("❌ Consolidated directory not found")
        return False
    
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    print(f"🔍 Verifying materials for {len(candidate_dirs)} candidates...")
    
    incomplete_candidates = []
    
    for candidate_dir in candidate_dirs:
        candidate_name = candidate_dir.name
        required_files = [
            "candidate_summary.md",
            "screening/screening_report.md",
            "evaluation/evaluation_framework.md"
        ]
        
        missing_files = []
        for file_path in required_files:
            if not (candidate_dir / file_path).exists():
                missing_files.append(file_path)
        
        if missing_files:
            incomplete_candidates.append({
                "candidate": candidate_name,
                "missing": missing_files
            })
    
    if incomplete_candidates:
        print(f"⚠️  {len(incomplete_candidates)} candidates have missing materials:")
        for candidate in incomplete_candidates:
            print(f"   - {candidate['candidate']}: {', '.join(candidate['missing'])}")
        return False
    else:
        print(f"✅ All {len(candidate_dirs)} candidates have complete materials")
        return True

def generate_final_summary():
    """Generate final summary with material counts"""
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    summary_stats = {
        "total_candidates": len(candidate_dirs),
        "materials_by_type": {
            "screening_reports": 0,
            "takehome_assignments": 0,
            "interview_materials": 0,
            "evaluation_frameworks": 0
        },
        "candidates_by_status": {
            "ready_for_takehome": 0,
            "ready_for_interview": 0,
            "needs_additional_assessment": 0,
            "declined": 0
        }
    }
    
    for candidate_dir in candidate_dirs:
        # Count materials
        if (candidate_dir / "screening" / "screening_report.md").exists():
            summary_stats["materials_by_type"]["screening_reports"] += 1
        
        if (candidate_dir / "takehome" / "takehome_assignment.md").exists():
            summary_stats["materials_by_type"]["takehome_assignments"] += 1
        
        if (candidate_dir / "interview" / "interview_guide.md").exists():
            summary_stats["materials_by_type"]["interview_materials"] += 1
        
        if (candidate_dir / "evaluation" / "evaluation_framework.md").exists():
            summary_stats["materials_by_type"]["evaluation_frameworks"] += 1
    
    # Save summary
    summary_path = base_path / "workflow_completion_summary.json"
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary_stats, f, indent=2)
    
    print(f"📊 Final Summary:")
    print(f"   Total Candidates: {summary_stats['total_candidates']}")
    print(f"   Screening Reports: {summary_stats['materials_by_type']['screening_reports']}")
    print(f"   Take-home Assignments: {summary_stats['materials_by_type']['takehome_assignments']}")
    print(f"   Interview Materials: {summary_stats['materials_by_type']['interview_materials']}")
    print(f"   Evaluation Frameworks: {summary_stats['materials_by_type']['evaluation_frameworks']}")
    print(f"   Summary saved to: {summary_path}")

def main():
    """Run complete workflow integration"""
    print("🚀 Starting Complete Workflow Integration")
    print("=" * 50)
    
    # Step 1: Consolidate existing results (if not already done)
    consolidation_log = Path("artifacts/public/hiring/candidates/20250811_consolidated/consolidation_log.json")
    if not consolidation_log.exists():
        if not run_script("scripts/consolidate_hiring_results.py", "Consolidating hiring results"):
            return False
    else:
        print("✅ Results already consolidated")
    
    # Step 2: Generate complete candidate materials
    materials_log = Path("artifacts/public/hiring/candidates/20250811_consolidated/materials_generation_log.json")
    if not materials_log.exists():
        if not run_script("scripts/generate_complete_candidate_materials.py", "Generating complete candidate materials"):
            return False
    else:
        print("✅ Candidate materials already generated")
    
    # Step 3: Generate overall summary
    overall_summary = Path("artifacts/public/hiring/candidates/20250811_consolidated/HIRING_SUMMARY_COMPLETE.md")
    if not overall_summary.exists():
        if not run_script("scripts/generate_overall_summary.py", "Generating overall hiring summary"):
            return False
    else:
        print("✅ Overall summary already exists")
    
    # Step 4: Verify all materials are complete
    if not verify_candidate_materials():
        print("❌ Material verification failed")
        return False
    
    # Step 5: Generate final summary statistics
    generate_final_summary()
    
    print("\n" + "=" * 50)
    print("🎉 Complete Workflow Integration Successful!")
    print("\n📁 All candidate materials are now available at:")
    print("   artifacts/public/hiring/candidates/20250811_consolidated/")
    print("\n📋 Each candidate directory contains:")
    print("   - screening/screening_report.md")
    print("   - takehome/takehome_assignment.md (where applicable)")
    print("   - interview/interview_guide.md, interview_script.md, candidate_context.md")
    print("   - evaluation/evaluation_framework.md")
    print("   - candidate_summary.md")
    print("\n🎯 Team leads and HR personnel can now make informed hiring decisions!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)