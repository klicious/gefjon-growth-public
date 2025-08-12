#!/usr/bin/env python3
"""
Analyze gaps between ideal workflow and current implementation
Identify what needs to be fixed for the ideal state
"""

import json
from pathlib import Path
import yaml

def analyze_input_data_flow():
    """Analyze the input data flow and identify gaps"""
    print("🔍 Analyzing Input Data Flow...")
    
    gaps = []
    
    # Check expected vs actual input paths
    expected_input = "data/public/hiring/candidates/individual/{date}/"
    actual_input = "data/public/hiring/resume/20250731/candidates_20250731.json"
    
    print(f"   Expected Input: {expected_input}")
    print(f"   Actual Input: {actual_input}")
    
    if not Path("data/public/hiring/candidates/individual/").exists():
        gaps.append({
            "type": "input_structure",
            "issue": "Expected individual candidate files directory doesn't exist",
            "expected": expected_input,
            "actual": actual_input,
            "fix": "Create data transformation step or update orchestrator expectations"
        })
    
    # Check if the actual input file exists
    actual_input_path = Path(actual_input)
    if actual_input_path.exists():
        print(f"   ✅ Actual input file exists")
        
        # Load and analyze structure
        with open(actual_input_path, 'r', encoding='utf-8') as f:
            candidates_data = json.load(f)
        
        print(f"   📊 Contains {len(candidates_data)} candidates")
        
        # Check if normalized data exists (which is what the workflow actually uses)
        normalized_path = Path("data/public/hiring/working/20250811_enhanced_run/candidates.normalized.json")
        if normalized_path.exists():
            with open(normalized_path, 'r', encoding='utf-8') as f:
                normalized_data = json.load(f)
            
            print(f"   📊 Normalized data contains {len(normalized_data)} candidates")
            
            # Check normalized data structure
            if normalized_data:
                sample_candidate = normalized_data[0]
                required_fields = ['candidate_id', 'name', 'skills', 'experience_years']
                missing_fields = [field for field in required_fields if field not in sample_candidate]
                
                if missing_fields:
                    gaps.append({
                        "type": "data_structure",
                        "issue": f"Missing required fields in normalized candidate data: {missing_fields}",
                        "fix": "Update data normalization or workflow expectations"
                    })
                else:
                    print(f"   ✅ Normalized candidate data structure looks good")
        else:
            # Check original data structure
            if candidates_data:
                sample_candidate = candidates_data[0]
                required_fields = ['candidate_id', 'name_en', 'skills', 'experience_years']
                missing_fields = [field for field in required_fields if field not in sample_candidate]
                
                if missing_fields:
                    gaps.append({
                        "type": "data_structure",
                        "issue": f"Missing required fields in original candidate data: {missing_fields}",
                        "fix": "Update data normalization or workflow expectations"
                    })
                else:
                    print(f"   ✅ Original candidate data structure looks good")
    else:
        gaps.append({
            "type": "missing_input",
            "issue": f"Input file doesn't exist: {actual_input}",
            "fix": "Ensure input data is available before workflow execution"
        })
    
    return gaps

def analyze_workflow_stages():
    """Analyze workflow stages and their implementation"""
    print("\n🔍 Analyzing Workflow Stages...")
    
    gaps = []
    
    # Load workflow config
    config_path = Path("ai_docs/workflows/hiring/config/workflow_config.yaml")
    if not config_path.exists():
        gaps.append({
            "type": "missing_config",
            "issue": "Workflow configuration file missing",
            "fix": "Ensure workflow_config.yaml exists"
        })
        return gaps
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Check if stages are properly implemented
    stages = config.get('stages', {})
    
    for stage_name, stage_config in stages.items():
        print(f"   Checking stage: {stage_name}")
        
        output_dir = stage_config.get('output_directory')
        required_files = stage_config.get('required_files', [])
        
        # Check if scripts handle this stage
        stage_implemented = False
        
        # Check in generate_enhanced_materials.py
        script_path = Path("scripts/generate_enhanced_materials.py")
        if script_path.exists():
            with open(script_path, 'r') as f:
                script_content = f.read()
                if output_dir in script_content or f"generate_{output_dir}" in script_content:
                    stage_implemented = True
        
        if stage_implemented:
            print(f"      ✅ Stage implemented")
        else:
            gaps.append({
                "type": "stage_implementation",
                "issue": f"Stage {stage_name} not fully implemented in scripts",
                "stage": stage_name,
                "fix": f"Ensure scripts generate files for {output_dir} directory"
            })
    
    return gaps

def analyze_output_structure():
    """Analyze the output structure against expectations"""
    print("\n🔍 Analyzing Output Structure...")
    
    gaps = []
    
    # Check consolidated directory
    consolidated_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    if not consolidated_path.exists():
        gaps.append({
            "type": "missing_output",
            "issue": "Consolidated output directory doesn't exist",
            "fix": "Run workflow to generate consolidated results"
        })
        return gaps
    
    # Load workflow config for expected structure
    config_path = Path("ai_docs/workflows/hiring/config/workflow_config.yaml")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    expected_subdirs = config['directory_structure']['candidate_subdirectories']
    
    # Check a sample candidate directory
    candidate_dirs = [d for d in consolidated_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    if not candidate_dirs:
        gaps.append({
            "type": "no_candidates",
            "issue": "No candidate directories found in consolidated output",
            "fix": "Run consolidation script"
        })
        return gaps
    
    sample_dir = candidate_dirs[0]
    print(f"   Checking sample directory: {sample_dir.name}")
    
    # Check subdirectory structure
    for expected_subdir in expected_subdirs:
        subdir_path = sample_dir / expected_subdir
        if not subdir_path.exists():
            gaps.append({
                "type": "missing_subdirectory",
                "issue": f"Missing subdirectory: {expected_subdir}",
                "candidate": sample_dir.name,
                "fix": f"Ensure scripts create {expected_subdir} directory"
            })
        else:
            print(f"      ✅ {expected_subdir} directory exists")
    
    # Check file completeness based on candidate status
    # Load screening data to check candidate status
    screening_file = Path("data/public/hiring/working/20250811_enhanced_run/screening_summary_complete.json")
    if screening_file.exists():
        with open(screening_file, 'r') as f:
            screening_data = json.load(f)
        
        # Find the sample candidate's status
        sample_candidate_id = sample_dir.name.split('_')[0] + '_' + sample_dir.name.split('_')[1]
        candidate_screening = next((c for c in screening_data['screening_results'] if c['candidate_id'] == sample_candidate_id), None)
        
        if candidate_screening:
            next_step = candidate_screening['next_step']
            print(f"      Sample candidate status: {next_step}")
            
            # Check files based on status
            stages = config.get('stages', {})
            for stage_name, stage_config in stages.items():
                output_dir = stage_config.get('output_directory')
                required_files = stage_config.get('required_files', [])
                condition = stage_config.get('condition')
                
                # Check if this stage applies to this candidate
                stage_applies = True
                if condition:
                    if 'take_home_assignment' in condition and next_step not in ['take_home_assignment', 'senior_level_assessment']:
                        stage_applies = False
                    elif 'additional_assessment' in condition and next_step not in ['take_home_assignment', 'senior_level_assessment', 'additional_assessment']:
                        stage_applies = False
                
                if stage_applies:
                    stage_dir = sample_dir / output_dir
                    if stage_dir.exists():
                        for required_file in required_files:
                            file_path = stage_dir / required_file
                            if not file_path.exists():
                                gaps.append({
                                    "type": "missing_file",
                                    "issue": f"Missing required file: {output_dir}/{required_file}",
                                    "candidate": sample_dir.name,
                                    "stage": stage_name,
                                    "status": next_step,
                                    "fix": f"Ensure scripts generate {required_file}"
                                })
                            else:
                                print(f"      ✅ {output_dir}/{required_file} exists")
                    else:
                        if stage_name not in ['2_takehome']:  # takehome might not exist for some candidates
                            gaps.append({
                                "type": "missing_directory",
                                "issue": f"Missing stage directory: {output_dir}",
                                "candidate": sample_dir.name,
                                "stage": stage_name,
                                "fix": f"Ensure scripts create {output_dir} directory"
                            })
                else:
                    print(f"      ⏭️  Stage {stage_name} doesn't apply to this candidate ({next_step})")
    else:
        print(f"      ⚠️  Cannot verify file completeness - screening data not found")
    
    return gaps

def analyze_script_consistency():
    """Analyze script consistency with workflow expectations"""
    print("\n🔍 Analyzing Script Consistency...")
    
    gaps = []
    
    # Check primary scripts exist
    primary_scripts = [
        "complete_workflow_final.py",
        "generate_enhanced_materials.py",
        "consolidate_hiring_results.py",
        "generate_overall_summary.py",
        "verify_workflow_consistency.py"
    ]
    
    for script_name in primary_scripts:
        script_path = Path("scripts") / script_name
        if not script_path.exists():
            gaps.append({
                "type": "missing_script",
                "issue": f"Primary script missing: {script_name}",
                "fix": f"Ensure {script_name} exists in scripts directory"
            })
        else:
            print(f"   ✅ {script_name} exists")
    
    # Check if scripts use correct input paths
    master_script = Path("scripts/complete_workflow_final.py")
    if master_script.exists():
        with open(master_script, 'r') as f:
            content = f.read()
            
            # Check for hardcoded paths that might not match expectations
            if "20250811_consolidated" in content and "get_consolidated_path" not in content:
                gaps.append({
                    "type": "hardcoded_path",
                    "issue": "Master script has hardcoded date-specific path",
                    "fix": "Make paths configurable or date-agnostic"
                })
            elif "get_consolidated_path" in content:
                print(f"   ✅ Script uses configurable paths")
            
            if "screening_summary_complete.json" in content:
                print(f"   ✅ Script references screening data correctly")
    
    return gaps

def generate_ideal_state_fixes(all_gaps):
    """Generate fixes to achieve ideal state"""
    print("\n🔧 Generating Ideal State Fixes...")
    
    fixes = []
    
    # Group gaps by type
    gap_types = {}
    for gap in all_gaps:
        gap_type = gap['type']
        if gap_type not in gap_types:
            gap_types[gap_type] = []
        gap_types[gap_type].append(gap)
    
    # Generate fixes for each type
    for gap_type, gaps in gap_types.items():
        if gap_type == "input_structure":
            fixes.append({
                "priority": "high",
                "type": "input_normalization",
                "description": "Create input data normalization step",
                "action": "Add preprocessing step to convert candidates_20250731.json to expected individual files format",
                "script": "create_input_normalization_script"
            })
        
        elif gap_type == "hardcoded_path":
            fixes.append({
                "priority": "medium",
                "type": "path_configuration",
                "description": "Make paths configurable",
                "action": "Update scripts to use configurable date/path parameters",
                "script": "update_path_configuration"
            })
        
        elif gap_type == "missing_file" or gap_type == "missing_subdirectory":
            fixes.append({
                "priority": "high",
                "type": "material_generation",
                "description": "Ensure complete material generation",
                "action": "Update material generation scripts to create all required files",
                "script": "enhance_material_generation"
            })
        
        elif gap_type == "stage_implementation":
            fixes.append({
                "priority": "high",
                "type": "stage_completion",
                "description": "Complete workflow stage implementation",
                "action": "Ensure all workflow stages are fully implemented in scripts",
                "script": "complete_stage_implementation"
            })
    
    return fixes

def main():
    """Main analysis function"""
    print("🔍 WORKFLOW GAP ANALYSIS")
    print("=" * 60)
    
    all_gaps = []
    
    # Run all analyses
    all_gaps.extend(analyze_input_data_flow())
    all_gaps.extend(analyze_workflow_stages())
    all_gaps.extend(analyze_output_structure())
    all_gaps.extend(analyze_script_consistency())
    
    print(f"\n📊 ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"Total gaps identified: {len(all_gaps)}")
    
    if all_gaps:
        print("\n❌ GAPS FOUND:")
        for i, gap in enumerate(all_gaps, 1):
            print(f"{i}. {gap['type'].upper()}: {gap['issue']}")
            print(f"   Fix: {gap['fix']}")
        
        # Generate fixes
        fixes = generate_ideal_state_fixes(all_gaps)
        
        print(f"\n🔧 RECOMMENDED FIXES:")
        for i, fix in enumerate(fixes, 1):
            print(f"{i}. [{fix['priority'].upper()}] {fix['description']}")
            print(f"   Action: {fix['action']}")
        
        return False
    else:
        print("\n✅ NO GAPS FOUND!")
        print("The workflow matches the ideal state.")
        return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)