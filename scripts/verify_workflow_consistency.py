#!/usr/bin/env python3
"""
Verify that the cleaned workflow matches the actual consolidated results
"""

import json
from pathlib import Path
import yaml

def load_workflow_config():
    """Load the workflow configuration"""
    config_path = Path("ai_docs/workflows/hiring/config/workflow_config.yaml")
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_candidate_data():
    """Load the original and normalized candidate data"""
    # Original data
    original_path = Path("data/public/hiring/resume/20250731/candidates_20250731.json")
    with open(original_path, 'r') as f:
        original_data = json.load(f)
    
    # Normalized data
    normalized_path = Path("data/public/hiring/working/20250811_enhanced_run/candidates.normalized.json")
    with open(normalized_path, 'r') as f:
        normalized_data = json.load(f)
    
    return original_data, normalized_data

def verify_directory_structure():
    """Verify the consolidated directory structure matches workflow config"""
    config = load_workflow_config()
    
    # Check base path
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    if not base_path.exists():
        return False, "Base consolidated directory not found"
    
    # Load screening data to check candidate status
    screening_path = Path("data/public/hiring/working/20250811_enhanced_run/screening_summary_complete.json")
    with open(screening_path, 'r') as f:
        screening_data = json.load(f)
    
    # Create lookup for candidate status
    candidate_status = {}
    for candidate in screening_data['screening_results']:
        candidate_status[candidate['candidate_id']] = candidate['next_step']
    
    # Get candidate directories
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    issues = []
    
    # Check each candidate directory
    for candidate_dir in candidate_dirs:
        # Extract candidate_id from directory name
        candidate_id = candidate_dir.name.split('_')[0] + '_' + candidate_dir.name.split('_')[1]
        next_step = candidate_status.get(candidate_id, 'unknown')
        
        # Check subdirectory structure
        expected_subdirs = config['directory_structure']['candidate_subdirectories']
        for subdir in expected_subdirs:
            subdir_path = candidate_dir / subdir
            if not subdir_path.exists():
                issues.append(f"Missing subdirectory: {candidate_dir.name}/{subdir}")
        
        # Check required files per stage
        for stage_name, stage_config in config['stages'].items():
            # Check if stage applies to this candidate
            if 'condition' in stage_config:
                condition = stage_config['condition']
                if 'take_home_assignment' in condition and next_step not in ['take_home_assignment', 'senior_level_assessment']:
                    continue  # Skip this stage for this candidate
                if 'additional_assessment' in condition and next_step not in ['take_home_assignment', 'senior_level_assessment', 'additional_assessment']:
                    continue  # Skip this stage for this candidate
            
            stage_dir = candidate_dir / stage_config['output_directory']
            if stage_dir.exists():
                for required_file in stage_config['required_files']:
                    file_path = stage_dir / required_file
                    if not file_path.exists():
                        issues.append(f"Missing required file: {candidate_dir.name}/{stage_config['output_directory']}/{required_file}")
    
    return len(issues) == 0, issues

def verify_candidate_mapping():
    """Verify that candidates from input data match consolidated output"""
    original_data, normalized_data = load_candidate_data()
    
    # Get consolidated candidates
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    candidate_dirs = [d.name for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    issues = []
    
    # Check if all normalized candidates have directories
    for candidate in normalized_data:
        candidate_id = candidate['candidate_id']
        candidate_name = candidate['name'].lower().replace(' ', '_')
        expected_dir = f"{candidate_id}_{candidate_name}"
        
        if expected_dir not in candidate_dirs:
            issues.append(f"Missing directory for candidate: {candidate_id} ({candidate['name']})")
    
    # Check if there are extra directories
    expected_dirs = []
    for candidate in normalized_data:
        candidate_id = candidate['candidate_id']
        candidate_name = candidate['name'].lower().replace(' ', '_')
        expected_dirs.append(f"{candidate_id}_{candidate_name}")
    
    for dir_name in candidate_dirs:
        if dir_name not in expected_dirs:
            issues.append(f"Unexpected directory: {dir_name}")
    
    return len(issues) == 0, issues

def verify_file_naming():
    """Verify file naming conventions match config"""
    config = load_workflow_config()
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    
    issues = []
    expected_files = config['file_naming']
    
    # Check a sample candidate directory
    sample_dir = next(d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.'))
    
    # Check screening files
    screening_dir = sample_dir / "screening"
    if screening_dir.exists():
        expected_screening = expected_files['screening_report']
        if not (screening_dir / expected_screening).exists():
            issues.append(f"Missing expected screening file: {expected_screening}")
    
    # Check interview files
    interview_dir = sample_dir / "interview"
    if interview_dir.exists():
        for file_key in ['interview_guide', 'interview_script', 'candidate_context']:
            expected_file = expected_files[file_key]
            if not (interview_dir / expected_file).exists():
                issues.append(f"Missing expected interview file: {expected_file}")
    
    return len(issues) == 0, issues

def main():
    """Main verification function"""
    print("🔍 Verifying Workflow Consistency")
    print("=" * 50)
    
    all_passed = True
    
    # Test 1: Directory Structure
    print("\n1. Checking directory structure...")
    structure_ok, structure_issues = verify_directory_structure()
    if structure_ok:
        print("   ✅ Directory structure matches workflow config")
    else:
        print("   ❌ Directory structure issues found:")
        for issue in structure_issues[:5]:  # Show first 5 issues
            print(f"      - {issue}")
        if len(structure_issues) > 5:
            print(f"      ... and {len(structure_issues) - 5} more issues")
        all_passed = False
    
    # Test 2: Candidate Mapping
    print("\n2. Checking candidate mapping...")
    mapping_ok, mapping_issues = verify_candidate_mapping()
    if mapping_ok:
        print("   ✅ All candidates properly mapped to directories")
    else:
        print("   ❌ Candidate mapping issues found:")
        for issue in mapping_issues:
            print(f"      - {issue}")
        all_passed = False
    
    # Test 3: File Naming
    print("\n3. Checking file naming conventions...")
    naming_ok, naming_issues = verify_file_naming()
    if naming_ok:
        print("   ✅ File naming matches workflow config")
    else:
        print("   ❌ File naming issues found:")
        for issue in naming_issues:
            print(f"      - {issue}")
        all_passed = False
    
    # Test 4: Check candidate count consistency
    print("\n4. Checking candidate count consistency...")
    original_data, normalized_data = load_candidate_data()
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    print(f"   Original candidates: {len(original_data)}")
    print(f"   Normalized candidates: {len(normalized_data)}")
    print(f"   Consolidated directories: {len(candidate_dirs)}")
    
    if len(normalized_data) == len(candidate_dirs):
        print("   ✅ Candidate counts match")
    else:
        print("   ❌ Candidate count mismatch")
        all_passed = False
    
    # Test 5: Check key files exist
    print("\n5. Checking key summary files...")
    key_files = [
        "HIRING_SUMMARY_COMPLETE.md",
        "QUICK_REFERENCE_GUIDE.md",
        "consolidation_log.json",
        "materials_generation_log.json"
    ]
    
    for key_file in key_files:
        file_path = base_path / key_file
        if file_path.exists():
            print(f"   ✅ {key_file}")
        else:
            print(f"   ❌ Missing: {key_file}")
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 WORKFLOW CONSISTENCY VERIFIED!")
        print("\n✅ The cleaned workflow matches the consolidated results")
        print("✅ All expected files and directories are present")
        print("✅ Candidate mapping is correct")
        print("✅ File naming conventions are followed")
        print("\n🚀 The workflow is ready for future execution")
    else:
        print("⚠️  WORKFLOW CONSISTENCY ISSUES FOUND!")
        print("\n🔧 Some aspects of the workflow don't match the results")
        print("📋 Review the issues above and update accordingly")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)