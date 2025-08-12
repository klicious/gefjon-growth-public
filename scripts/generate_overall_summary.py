#!/usr/bin/env python3
"""
Generate overall hiring summary with all important data
"""

import json
from pathlib import Path
from datetime import datetime

def load_screening_data():
    """Load the screening summary data"""
    screening_file = Path("data/public/hiring/working/20250811_enhanced_run/screening_summary_complete.json")
    with open(screening_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_consolidation_log():
    """Load the consolidation log"""
    log_file = Path("artifacts/public/hiring/candidates/20250811_consolidated/consolidation_log.json")
    with open(log_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_overall_summary():
    """Generate comprehensive hiring summary"""
    
    screening_data = load_screening_data()
    consolidation_log = load_consolidation_log()
    
    # Calculate additional statistics
    candidates = screening_data['screening_results']
    
    # Group by recommendation
    strong_hire = [c for c in candidates if c['recommendation'] == 'Strong Hire']
    hire = [c for c in candidates if c['recommendation'] == 'Hire']
    lean_hire = [c for c in candidates if c['recommendation'] == 'Lean Hire']
    no_hire = [c for c in candidates if c['recommendation'] == 'No Hire']
    
    # Group by next steps
    takehome_candidates = [c for c in candidates if c['next_step'] == 'take_home_assignment']
    additional_assessment = [c for c in candidates if c['next_step'] == 'additional_assessment']
    senior_assessment = [c for c in candidates if c['next_step'] == 'senior_level_assessment']
    declined = [c for c in candidates if c['next_step'] == 'decline']
    
    summary_content = f"""# Gefjon Growth Hiring Summary - August 11, 2025

## Executive Summary

**Total Candidates Processed**: {screening_data['total_candidates']}  
**Screening Completion Date**: {screening_data['screening_completed_at']}  
**Overall Pass Rate**: {screening_data['screening_statistics']['pass_rate']:.1%}  
**Average Score**: {screening_data['screening_statistics']['average_score']}/10  

### Recommendation Distribution
- **Strong Hire**: {len(strong_hire)} candidates ({len(strong_hire)/len(candidates):.1%})
- **Hire**: {len(hire)} candidates ({len(hire)/len(candidates):.1%})
- **Lean Hire**: {len(lean_hire)} candidates ({len(lean_hire)/len(candidates):.1%})
- **No Hire**: {len(no_hire)} candidates ({len(no_hire)/len(candidates):.1%})

### Next Steps Distribution
- **Take-home Assignment**: {len(takehome_candidates)} candidates
- **Additional Assessment**: {len(additional_assessment)} candidates
- **Senior Level Assessment**: {len(senior_assessment)} candidates
- **Declined**: {len(declined)} candidates

## Top Candidates (Strong Hire + High-Score Hire)

"""
    
    # Add top candidates section
    top_candidates = sorted([c for c in candidates if c['recommendation'] in ['Strong Hire', 'Hire'] and c['overall_score'] >= 8.0], 
                          key=lambda x: x['overall_score'], reverse=True)
    
    for i, candidate in enumerate(top_candidates, 1):
        summary_content += f"""### {i}. {candidate['candidate_name']} ({candidate['candidate_id']})
- **Score**: {candidate['overall_score']}/10
- **Recommendation**: {candidate['recommendation']}
- **Confidence**: {candidate['confidence']:.0%}
- **Next Step**: {candidate['next_step']}
- **Key Strengths**: {', '.join(candidate['key_strengths'][:2])}
- **Directory**: `artifacts/public/hiring/candidates/20250811_consolidated/{candidate['candidate_id']}_{candidate['candidate_name'].lower().replace(' ', '_')}/`

"""
    
    # Add detailed candidate breakdown
    summary_content += """## Detailed Candidate Analysis

### Strong Hire Candidates
"""
    
    for candidate in strong_hire:
        summary_content += f"""
#### {candidate['candidate_name']} ({candidate['candidate_id']})
- **Score**: {candidate['overall_score']}/10 | **Confidence**: {candidate['confidence']:.0%}
- **Strengths**: {'; '.join(candidate['key_strengths'])}
- **Concerns**: {'; '.join(candidate['areas_of_concern'])}
- **Next Step**: {candidate['next_step']}
"""
    
    summary_content += """
### Hire Candidates
"""
    
    for candidate in hire:
        summary_content += f"""
#### {candidate['candidate_name']} ({candidate['candidate_id']})
- **Score**: {candidate['overall_score']}/10 | **Confidence**: {candidate['confidence']:.0%}
- **Strengths**: {'; '.join(candidate['key_strengths'])}
- **Concerns**: {'; '.join(candidate['areas_of_concern'])}
- **Next Step**: {candidate['next_step']}
"""
    
    summary_content += """
### Candidates Requiring Additional Assessment
"""
    
    for candidate in lean_hire:
        summary_content += f"""
#### {candidate['candidate_name']} ({candidate['candidate_id']})
- **Score**: {candidate['overall_score']}/10 | **Confidence**: {candidate['confidence']:.0%}
- **Strengths**: {'; '.join(candidate['key_strengths'])}
- **Concerns**: {'; '.join(candidate['areas_of_concern'])}
- **Next Step**: {candidate['next_step']}
"""
    
    summary_content += """
### Declined Candidates
"""
    
    for candidate in no_hire:
        summary_content += f"""
#### {candidate['candidate_name']} ({candidate['candidate_id']})
- **Score**: {candidate['overall_score']}/10 | **Confidence**: {candidate['confidence']:.0%}
- **Strengths**: {'; '.join(candidate['key_strengths'])}
- **Concerns**: {'; '.join(candidate['areas_of_concern'])}
- **Reason**: {candidate['next_step']}
"""
    
    # Add process statistics
    summary_content += f"""
## Process Statistics

### Experience Distribution
- **Entry Level (0-2 years)**: {screening_data['experience_distribution']['entry_level_0_2_years']} candidates
- **Mid Level (2-5 years)**: {screening_data['experience_distribution']['mid_level_2_5_years']} candidates
- **Senior Level (5+ years)**: {screening_data['experience_distribution']['senior_level_5_plus_years']} candidates

### Quality Metrics
- **Quality Threshold Met**: {screening_data['screening_statistics']['quality_threshold_met']}
- **Bias Check Passed**: {screening_data['screening_statistics']['bias_check_passed']}
- **Strong Hire Rate**: {screening_data['screening_statistics']['strong_hire_rate']:.1%}
- **Overall Hire Rate**: {screening_data['screening_statistics']['hire_rate']:.1%}

## File Organization

All candidate materials have been consolidated into individual directories under:
`artifacts/public/hiring/candidates/20250811_consolidated/`

Each candidate directory contains:
- **screening/**: Screening reports and evaluations
- **takehome/**: Take-home assignments and evaluations (where applicable)
- **interview/**: Interview materials and guides (where applicable)
- **evaluation/**: Final evaluations and decisions (to be completed)
- **communication/**: Email templates and correspondence (to be added)
- **candidate_summary.md**: Individual candidate overview

### Files Processed
- **Total Files Moved**: {consolidation_log['files_moved']}
- **Candidates with Materials**: {len([c for c in consolidation_log['candidates_processed'] if c['files_moved'] > 0])}
- **Consolidation Date**: {consolidation_log['consolidation_date']}

## Immediate Action Items

### For Take-home Assignment Candidates ({len(takehome_candidates)} candidates)
{chr(10).join(f"- {c['candidate_name']} ({c['candidate_id']})" for c in takehome_candidates)}

### For Additional Assessment ({len(additional_assessment)} candidates)
{chr(10).join(f"- {c['candidate_name']} ({c['candidate_id']})" for c in additional_assessment)}

### For Senior Level Assessment ({len(senior_assessment)} candidates)
{chr(10).join(f"- {c['candidate_name']} ({c['candidate_id']})" for c in senior_assessment)}

## Recommendations

1. **Immediate Priority**: Process take-home assignments for the 8 qualified candidates
2. **Secondary Priority**: Conduct additional assessments for 3 lean hire candidates
3. **Senior Consideration**: Evaluate titan_006 (titan-cand) for senior-level positions
4. **Process Improvement**: Address missing contact information for several candidates

---
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Source Data: 20250811_enhanced_run screening results*
*Consolidated Structure: Single candidate directories with all materials*
"""
    
    return summary_content

def main():
    """Generate and save the overall summary"""
    
    summary_content = generate_overall_summary()
    
    # Save to multiple locations for easy access
    summary_paths = [
        Path("artifacts/public/hiring/candidates/20250811_consolidated/HIRING_SUMMARY_COMPLETE.md"),
        Path("data/public/hiring/working/20250811_enhanced_run/HIRING_SUMMARY_COMPLETE.md")
    ]
    
    for summary_path in summary_paths:
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        print(f"✅ Summary saved to: {summary_path}")
    
    print(f"\n📊 Overall hiring summary generated successfully!")
    print(f"📁 Contains analysis of 13 candidates with consolidated file structure")
    print(f"🎯 Key insight: 8 candidates ready for take-home assignments")

if __name__ == "__main__":
    main()