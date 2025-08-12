# Single Candidate Workflow

## Overview
This workflow maintains a single version of results for each candidate, eliminating duplicate files and providing a clean, organized structure for the hiring process.

## Key Improvements

### 1. Single Directory Per Candidate
- Each candidate gets one consolidated directory: `{candidate_id}_{normalized_name}`
- All materials for a candidate are stored in their dedicated directory
- No more scattered files across multiple locations

### 2. Standardized Subdirectory Structure
```
artifacts/public/hiring/candidates/{date}_consolidated/
├── {candidate_id}_{normalized_name}/
│   ├── screening/           # Screening reports and evaluations
│   ├── takehome/           # Take-home assignments and evaluations
│   ├── interview/          # Interview materials and guides
│   ├── evaluation/         # Final evaluations and decisions
│   ├── communication/      # Email templates and correspondence
│   └── candidate_summary.md # Individual candidate overview
```

### 3. Automated Consolidation
- Script automatically moves existing files to appropriate subdirectories
- Generates individual candidate summaries
- Creates comprehensive hiring summary with all key data

## Workflow Stages

### Stage 1: Candidate Intake & Screening
**Output Location**: `{candidate_dir}/screening/`
- `screening_report.md` - Detailed screening analysis
- Automated scoring and recommendation generation

### Stage 2: Take-home Assignment (if applicable)
**Output Location**: `{candidate_dir}/takehome/`
- `takehome_assignment.md` - Customized assignment
- `takehome_evaluation.md` - Assessment results

### Stage 3: Interview Preparation
**Output Location**: `{candidate_dir}/interview/`
- `candidate_context.md` - Executive briefing
- `interview_guide.md` - Detailed interview plan
- `interview_script.md` - Verbatim script for interviewers

### Stage 4: Final Evaluation
**Output Location**: `{candidate_dir}/evaluation/`
- `final_evaluation.md` - Comprehensive assessment
- `decision_summary.md` - Hiring decision and rationale

### Stage 5: Communication
**Output Location**: `{candidate_dir}/communication/`
- Email templates for each stage
- Correspondence tracking

## Benefits

### For Hiring Managers
- Single location to find all candidate information
- Clear progress tracking through directory structure
- Comprehensive summaries for quick decision making

### For Interviewers
- All interview materials in one place
- Consistent file naming and structure
- Easy access to candidate context

### For HR Operations
- Streamlined file management
- Audit trail maintenance
- Scalable process for high-volume hiring

## Implementation Status

### ✅ Completed
- Consolidation script for existing candidates
- Standardized directory structure
- Individual candidate summaries
- Overall hiring summary generation
- Complete material generation for all candidates
- Screening reports with detailed analysis
- Take-home assignments customized by level
- Interview materials (context, guide, script)
- Evaluation frameworks for decision tracking
- Integrated workflow automation

### 🔄 In Progress
- Communication templates and tracking
- Automated email generation
- Real-time status updates

### 📋 Planned
- Integration with external communication tools
- Automated workflow triggers
- Performance analytics and reporting

## Usage

### Run Complete Workflow Integration
```bash
python scripts/complete_workflow_integration.py
```

This single command will:
- Consolidate existing results
- Generate all missing candidate materials
- Create comprehensive summaries
- Verify material completeness

### Individual Script Usage
```bash
# Consolidate existing files
python scripts/consolidate_hiring_results.py

# Generate complete materials for all candidates
python scripts/generate_complete_candidate_materials.py

# Generate overall summary
python scripts/generate_overall_summary.py
```

### Access Candidate Information
Navigate to: `artifacts/public/hiring/candidates/20250811_consolidated/{candidate_id}_{name}/`

Each directory now contains:
- **Complete screening analysis** with technical assessment
- **Customized take-home assignments** based on experience level
- **Comprehensive interview materials** ready for use
- **Evaluation frameworks** for decision tracking

## File Naming Conventions

- **Screening**: `screening_report.md`
- **Take-home**: `takehome_assignment.md`, `takehome_evaluation.md`
- **Interview**: `candidate_context.md`, `interview_guide.md`, `interview_script.md`
- **Evaluation**: `final_evaluation.md`, `decision_summary.md`
- **Summary**: `candidate_summary.md`

This enhanced workflow ensures clean, organized, and easily accessible hiring materials while maintaining the comprehensive evaluation process that Gefjon Growth requires.