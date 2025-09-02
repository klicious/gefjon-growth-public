# Single Candidate Hybrid Workflow
## BEI Core Values + Enhanced Technical Assessment

## Overview
This workflow implements the **Hybrid BEI + Enhanced Technical Assessment** methodology, maintaining a single version of results for each candidate with comprehensive evaluation combining traditional behavioral assessment (60% weight) and enhanced technical evaluation (40% weight). Provides a clean, organized structure for the complete hiring process while preserving organizational DNA and addressing technical assessment gaps.

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

### Stage 3: Hybrid Interview Preparation  
**Output Location**: `{candidate_dir}/interview/`
- `candidate_context.md` - Executive briefing with hybrid assessment analysis
- `interview_guide.md` - Hybrid interview plan (BEI + enhanced technical)
- `interview_script.md` - BEI STAR questions + technical assessment guidance

**Hybrid Assessment Components**:
- **BEI Core Values Assessment**: 40 minutes, STAR format questions for all 10 values
- **AI-Assisted Technical Assessment**: 25 minutes, hands-on AI collaboration evaluation
- **Platform Engineering Scenarios**: 25 minutes, systems thinking and production mindset

### Stage 4: Hybrid Final Evaluation
**Output Location**: `{candidate_dir}/evaluation/`
- `final_evaluation.md` - Comprehensive hybrid assessment (75-point scoring)
- `decision_summary.md` - Hiring decision with hybrid scoring rationale

**Hybrid Scoring Framework**:
- **BEI Core Values**: 50 points (60% weight) - minimum 35 points required
- **Enhanced Technical**: 25 points (40% weight) - minimum 15 points required  
- **Overall Minimum**: 50/75 points (67%) for hire recommendation
- **Decision Matrix**: Strong Hire (87%), Hire (73%), Lean Hire (67%), No Hire (<67%)

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

### Run Complete Hybrid Workflow Integration
```bash
python scripts/complete_hybrid_workflow_integration.py
```

This single command will:
- Execute hybrid BEI + enhanced technical assessment methodology
- Consolidate existing results with hybrid scoring framework
- Generate all missing candidate materials using 60%/40% weighting
- Create comprehensive hybrid assessment summaries
- Verify material completeness with both behavioral and technical components

### Individual Hybrid Script Usage
```bash
# Consolidate existing files with hybrid scoring
python scripts/consolidate_hybrid_hiring_results.py

# Generate complete hybrid materials for all candidates
python scripts/generate_hybrid_candidate_materials.py

# Generate overall hybrid assessment summary  
python scripts/generate_hybrid_overall_summary.py
```

### Access Candidate Information
Navigate to: `artifacts/public/hiring/candidates/20250811_consolidated/{candidate_id}_{name}/`

Each directory now contains:
- **Complete hybrid screening analysis** with core values and technical assessment
- **Customized take-home assignments** based on experience level with AI collaboration focus
- **Comprehensive hybrid interview materials** ready for BEI + enhanced technical evaluation
- **Hybrid evaluation frameworks** for 75-point decision tracking (50 BEI + 25 technical)

## File Naming Conventions

- **Screening**: `screening_report.md`
- **Take-home**: `takehome_assignment.md`, `takehome_evaluation.md`
- **Interview**: `candidate_context.md`, `interview_guide.md`, `interview_script.md`
- **Evaluation**: `final_evaluation.md`, `decision_summary.md`
- **Summary**: `candidate_summary.md`

This enhanced **Hybrid BEI + Enhanced Technical Assessment** workflow ensures clean, organized, and easily accessible hiring materials while preserving organizational DNA through traditional core values assessment and addressing technical evaluation gaps through AI-assisted development focus. The hybrid approach maintains cultural alignment as the primary criterion while properly evaluating platform engineering and AI collaboration capabilities.

## Phoenix_005 Resolution
Under this hybrid framework, candidates like Phoenix_005 would now:
- **BEI Core Values**: 33/50 points (66%) - Strong learning foundation with development areas identified
- **Enhanced Technical**: 19/25 points (76%) - AI collaboration capability properly assessed
- **Overall Score**: 52/75 points (69%) - **LEAN HIRE** recommendation
- **Outcome**: Hire as Junior Platform Engineer with structured development plan

The hybrid methodology ensures no qualified candidates are missed due to technical assessment gaps while maintaining the cultural alignment that defines Gefjon Growth's organizational success.