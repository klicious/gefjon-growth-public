#!/usr/bin/env python3
"""
Final Complete Workflow Integration Script
Ensures all candidates have complete, production-ready materials
"""

import subprocess
import sys
from pathlib import Path
import json


def get_consolidated_path():
    """Get the consolidated results path (configurable)"""
    # Default to current date, but can be overridden
    import os
    date_str = os.environ.get('HIRING_RUN_DATE', '20250811')
    return Path(f"artifacts/public/hiring/candidates/{date_str}_consolidated")

def get_screening_data_path():
    """Get the screening data path (configurable)"""
    import os
    date_str = os.environ.get('HIRING_RUN_DATE', '20250811')
    return Path(f"data/public/hiring/working/{date_str}_enhanced_run/screening_summary_complete.json")

def run_script(script_path, description):
    """Run a script and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, check=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def verify_complete_materials():
    """Verify that all candidates have complete materials"""
    base_path = get_consolidated_path()
    
    if not base_path.exists():
        print("❌ Consolidated directory not found")
        return False
    
    # Load screening data to check expected materials
    screening_file = get_screening_data_path()
    with open(screening_file, 'r', encoding='utf-8') as f:
        screening_data = json.load(f)
    
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    print(f"🔍 Verifying complete materials for {len(candidate_dirs)} candidates...")
    
    incomplete_candidates = []
    
    for candidate_dir in candidate_dirs:
        candidate_name = candidate_dir.name
        
        # Extract candidate_id from directory name
        candidate_id = candidate_dir.name.split('_')[0] + '_' + candidate_dir.name.split('_')[1]
        
        # Find candidate's next step
        candidate_screening = next((c for c in screening_data['screening_results'] if c['candidate_id'] == candidate_id), None)
        if not candidate_screening:
            continue
        
        next_step = candidate_screening['next_step']
        
        # Check required files based on candidate status
        required_files = [
            "candidate_summary.md",
            "screening/screening_report.md",
            "evaluation/evaluation_framework.md"
        ]
        
        # Add conditional files based on status
        if next_step in ['take_home_assignment', 'senior_level_assessment']:
            required_files.append("takehome/takehome_assignment.md")
        
        if next_step in ['take_home_assignment', 'senior_level_assessment', 'additional_assessment']:
            required_files.extend([
                "interview/candidate_context.md",
                "interview/interview_guide.md", 
                "interview/interview_script.md"
            ])
        
        missing_files = []
        for file_path in required_files:
            if not (candidate_dir / file_path).exists():
                missing_files.append(file_path)
        
        if missing_files:
            incomplete_candidates.append({
                "candidate": candidate_name,
                "missing": missing_files,
                "status": next_step
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
    """Generate final comprehensive summary"""
    base_path = get_consolidated_path()
    
    # Load screening data
    screening_file = get_screening_data_path()
    with open(screening_file, 'r', encoding='utf-8') as f:
        screening_data = json.load(f)
    
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    summary_stats = {
        "workflow_completion_date": "2025-08-11",
        "total_candidates": len(candidate_dirs),
        "materials_by_type": {
            "screening_reports": 0,
            "takehome_assignments": 0,
            "interview_materials": 0,
            "evaluation_frameworks": 0,
            "communication_templates": 0
        },
        "candidates_by_status": {
            "strong_hire": len([c for c in screening_data['screening_results'] if c['recommendation'] == 'Strong Hire']),
            "hire": len([c for c in screening_data['screening_results'] if c['recommendation'] == 'Hire']),
            "lean_hire": len([c for c in screening_data['screening_results'] if c['recommendation'] == 'Lean Hire']),
            "no_hire": len([c for c in screening_data['screening_results'] if c['recommendation'] == 'No Hire'])
        },
        "next_steps": {
            "take_home_assignment": len([c for c in screening_data['screening_results'] if c['next_step'] == 'take_home_assignment']),
            "senior_level_assessment": len([c for c in screening_data['screening_results'] if c['next_step'] == 'senior_level_assessment']),
            "additional_assessment": len([c for c in screening_data['screening_results'] if c['next_step'] == 'additional_assessment']),
            "decline": len([c for c in screening_data['screening_results'] if c['next_step'] == 'decline'])
        }
    }
    
    # Count actual materials
    for candidate_dir in candidate_dirs:
        if (candidate_dir / "screening" / "screening_report.md").exists():
            summary_stats["materials_by_type"]["screening_reports"] += 1
        
        if (candidate_dir / "takehome" / "takehome_assignment.md").exists():
            summary_stats["materials_by_type"]["takehome_assignments"] += 1
        
        if (candidate_dir / "interview" / "interview_guide.md").exists():
            summary_stats["materials_by_type"]["interview_materials"] += 1
        
        if (candidate_dir / "evaluation" / "evaluation_framework.md").exists():
            summary_stats["materials_by_type"]["evaluation_frameworks"] += 1
        
        if (candidate_dir / "communication" / "communication_templates.md").exists():
            summary_stats["materials_by_type"]["communication_templates"] += 1
    
    # Save final summary
    summary_path = base_path / "FINAL_WORKFLOW_SUMMARY.json"
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary_stats, f, indent=2)
    
    print(f"📊 Final Workflow Summary:")
    print(f"   Total Candidates: {summary_stats['total_candidates']}")
    print(f"   Screening Reports: {summary_stats['materials_by_type']['screening_reports']}")
    print(f"   Take-home Assignments: {summary_stats['materials_by_type']['takehome_assignments']}")
    print(f"   Interview Materials: {summary_stats['materials_by_type']['interview_materials']}")
    print(f"   Evaluation Frameworks: {summary_stats['materials_by_type']['evaluation_frameworks']}")
    print(f"   Communication Templates: {summary_stats['materials_by_type']['communication_templates']}")
    print(f"   Summary saved to: {summary_path}")

def main():
    """Run final complete workflow integration"""
    print("🚀 Starting Final Complete Workflow Integration")
    print("=" * 60)
    
    all_passed = True
    
    # Step 1: Ensure consolidation is complete
    consolidation_log = Path("artifacts/public/hiring/candidates/20250811_consolidated/consolidation_log.json")
    if not consolidation_log.exists():
        if not run_script("scripts/consolidate_hiring_results.py", "Consolidating hiring results"):
            return False
    else:
        print("✅ Results already consolidated")
    
    # Step 2: Generate enhanced materials
    enhanced_log = Path("artifacts/public/hiring/candidates/20250811_consolidated/enhanced_materials_generation_log.json")
    if not enhanced_log.exists():
        if not run_script("scripts/generate_enhanced_materials.py", "Generating enhanced candidate materials"):
            return False
    else:
        print("✅ Enhanced materials already generated")
    
    # Step 3: Generate overall summary
    overall_summary = Path("artifacts/public/hiring/candidates/20250811_consolidated/HIRING_SUMMARY_COMPLETE.md")
    if not overall_summary.exists():
        if not run_script("scripts/generate_overall_summary.py", "Generating overall hiring summary"):
            return False
    else:
        print("✅ Overall summary already exists")
    
    # Step 4: Verify complete materials
    if not verify_complete_materials():
        print("❌ Material verification failed")
        all_passed = False
    
    # Step 5: Generate final summary statistics
    generate_final_summary()
    
    # Step 6: Run consistency verification
    if not run_script("scripts/verify_workflow_consistency.py", "Verifying workflow consistency"):
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 FINAL WORKFLOW INTEGRATION SUCCESSFUL!")
        print("\n✅ All candidate materials are complete and consistent")
        print("✅ Workflow configuration matches actual results")
        print("✅ All files properly organized and accessible")
        print("✅ Ready for production hiring decisions")
        
        print("\n📁 Complete materials available at:")
        print("   artifacts/public/hiring/candidates/20250811_consolidated/")
        
        print("\n📋 Each candidate directory contains:")
        print("   - screening/screening_report.md (comprehensive analysis)")
        print("   - takehome/takehome_assignment.md (where applicable)")
        print("   - interview/interview_guide.md, interview_script.md, candidate_context.md")
        print("   - evaluation/evaluation_framework.md (decision tracking)")
        print("   - candidate_summary.md (quick overview)")
        
        print("\n🎯 Team leads and HR personnel can now make informed hiring decisions!")
        print("🚀 The workflow is production-ready and future-proof!")
        
    else:
        print("⚠️  FINAL WORKFLOW INTEGRATION ISSUES FOUND!")
        print("\n🔧 Some aspects need attention before production use")
        print("📋 Review the issues above and resolve them")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)