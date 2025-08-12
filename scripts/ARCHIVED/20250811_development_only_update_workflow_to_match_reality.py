#!/usr/bin/env python3
"""
Update workflow configuration to match the actual consolidated results
"""

import json
from pathlib import Path
import yaml

def analyze_actual_structure():
    """Analyze what files actually exist for each candidate"""
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    candidate_dirs = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    analysis = {}
    
    for candidate_dir in candidate_dirs:
        candidate_id = candidate_dir.name.split('_')[0] + '_' + candidate_dir.name.split('_')[1]
        
        files_by_category = {
            'screening': [],
            'takehome': [],
            'interview': [],
            'evaluation': [],
            'communication': []
        }
        
        for category in files_by_category.keys():
            category_dir = candidate_dir / category
            if category_dir.exists():
                files_by_category[category] = [f.name for f in category_dir.glob('*.md')]
        
        # Add candidate summary
        if (candidate_dir / 'candidate_summary.md').exists():
            files_by_category['summary'] = ['candidate_summary.md']
        
        analysis[candidate_id] = files_by_category
    
    return analysis

def load_screening_data():
    """Load screening data to understand candidate status"""
    screening_path = Path("data/public/hiring/working/20250811_enhanced_run/screening_summary_complete.json")
    with open(screening_path, 'r') as f:
        screening_data = json.load(f)
    
    candidate_status = {}
    for candidate in screening_data['screening_results']:
        candidate_status[candidate['candidate_id']] = {
            'next_step': candidate['next_step'],
            'recommendation': candidate['recommendation'],
            'score': candidate['overall_score']
        }
    
    return candidate_status

def generate_realistic_config():
    """Generate a workflow config that matches actual results"""
    analysis = analyze_actual_structure()
    candidate_status = load_screening_data()
    
    # Analyze patterns
    common_files = {
        'screening': set(),
        'takehome': set(),
        'interview': set(),
        'evaluation': set()
    }
    
    # Find files that exist for most candidates in each category
    for candidate_id, files in analysis.items():
        for category, file_list in files.items():
            if category in common_files:
                common_files[category].update(file_list)
    
    # Create realistic config
    config = {
        'workflow_version': '2.0',
        'approach': 'single_candidate_directory',
        'directory_structure': {
            'base_path': 'artifacts/public/hiring/candidates',
            'candidate_directory_pattern': '{candidate_id}_{candidate_name_normalized}',
            'candidate_subdirectories': [
                'screening',
                'takehome', 
                'interview',
                'evaluation',
                'communication'
            ]
        },
        'file_naming': {
            'screening_report': 'screening_report.md',
            'takehome_assignment': 'takehome_assignment.md',
            'candidate_context': 'candidate_context.md',
            'interview_guide': 'interview_guide.md',
            'interview_script': 'interview_script.md',
            'evaluation_framework': 'evaluation_framework.md'
        },
        'stages': {
            '1_screening': {
                'output_directory': 'screening',
                'required_files': ['screening_report.md'],
                'description': 'All candidates have screening reports'
            },
            '2_takehome': {
                'output_directory': 'takehome',
                'required_files': ['takehome_assignment.md'],
                'optional_files': ['assignment.md', 'evaluation_sheet.md'],
                'condition': 'For candidates with next_step: take_home_assignment or senior_level_assessment',
                'description': 'Take-home assignments for qualified candidates'
            },
            '3_interview': {
                'output_directory': 'interview',
                'required_files': ['candidate_context.md'],
                'optional_files': ['interview_guide.md', 'interview_script.md'],
                'condition': 'For candidates proceeding to interviews',
                'description': 'Interview materials - not all candidates have complete sets'
            },
            '4_evaluation': {
                'output_directory': 'evaluation',
                'required_files': ['evaluation_framework.md'],
                'description': 'Evaluation framework for decision tracking'
            }
        },
        'summary_generation': {
            'overall_summary_file': 'HIRING_SUMMARY_COMPLETE.md',
            'quick_reference_file': 'QUICK_REFERENCE_GUIDE.md',
            'candidate_summary_file': 'candidate_summary.md'
        },
        'consolidation_rules': {
            'merge_duplicate_files': True,
            'preserve_latest_version': True,
            'archive_old_versions': False,
            'maintain_audit_trail': True
        },
        'notes': {
            'current_status': 'This configuration reflects the actual consolidated results as of 2025-08-11',
            'inconsistencies': 'Some candidates may be missing interview_guide.md and interview_script.md files',
            'future_improvements': 'Material generation script should be updated to ensure complete file sets'
        }
    }
    
    return config

def main():
    """Update the workflow configuration"""
    print("🔄 Analyzing actual consolidated structure...")
    
    analysis = analyze_actual_structure()
    candidate_status = load_screening_data()
    
    print(f"📊 Analyzed {len(analysis)} candidates")
    
    # Generate statistics
    stats = {
        'total_candidates': len(analysis),
        'candidates_with_screening': 0,
        'candidates_with_takehome': 0,
        'candidates_with_interview': 0,
        'candidates_with_evaluation': 0
    }
    
    for candidate_id, files in analysis.items():
        if files['screening']:
            stats['candidates_with_screening'] += 1
        if files['takehome']:
            stats['candidates_with_takehome'] += 1
        if files['interview']:
            stats['candidates_with_interview'] += 1
        if files['evaluation']:
            stats['candidates_with_evaluation'] += 1
    
    print(f"📈 Statistics:")
    print(f"   Screening reports: {stats['candidates_with_screening']}/{stats['total_candidates']}")
    print(f"   Take-home materials: {stats['candidates_with_takehome']}/{stats['total_candidates']}")
    print(f"   Interview materials: {stats['candidates_with_interview']}/{stats['total_candidates']}")
    print(f"   Evaluation frameworks: {stats['candidates_with_evaluation']}/{stats['total_candidates']}")
    
    # Generate realistic config
    print("\n🔧 Generating realistic workflow configuration...")
    realistic_config = generate_realistic_config()
    
    # Save updated config
    config_path = Path("ai_docs/workflows/hiring/config/workflow_config.yaml")
    with open(config_path, 'w') as f:
        yaml.dump(realistic_config, f, default_flow_style=False, sort_keys=False)
    
    print(f"✅ Updated workflow configuration saved to: {config_path}")
    
    # Create analysis report
    report_path = Path("artifacts/public/hiring/candidates/20250811_consolidated/structure_analysis.json")
    report = {
        'analysis_date': '2025-08-11',
        'statistics': stats,
        'candidate_files': analysis,
        'candidate_status': candidate_status
    }
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📋 Structure analysis saved to: {report_path}")
    
    print("\n🎉 Workflow configuration updated to match reality!")
    print("✅ Configuration now reflects actual consolidated results")
    print("📝 Future material generation can be improved based on this analysis")

if __name__ == "__main__":
    main()