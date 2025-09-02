# Gefjon Growth Hiring Workflow

## Overview
This directory contains the complete, production-ready hiring workflow for Gefjon Growth. The workflow implements a single-candidate directory approach with comprehensive materials generation.

## Current Workflow Version
**Version**: 2.0 (Single Candidate Directory Approach)  
**Last Updated**: 2025-08-12  
**Status**: Production Ready

## Quick Start

### Run Complete Workflow
```bash
python scripts/complete_workflow_integration.py
```

### Individual Components
```bash
# Consolidate existing results
python scripts/consolidate_hiring_results.py

# Generate complete materials
python scripts/generate_complete_candidate_materials.py

# Generate overall summary
python scripts/generate_overall_summary.py
```

## Workflow Components

### Core Files
- **orchestrator.md** - Main workflow orchestration and execution guide
- **single_candidate_workflow.md** - Detailed single-candidate approach documentation
- **validation_framework.md** - Quality assurance and validation processes
- **ai_agent_execution_guide.md** - Guide for AI agents executing the workflow

### Configuration
- **config/workflow_config.yaml** - Primary workflow configuration
- **tasks/** - Individual task definitions and specifications

### Scripts
- **scripts/complete_workflow_integration.py** - Master integration script
- **scripts/consolidate_hiring_results.py** - Result consolidation
- **scripts/generate_complete_candidate_materials.py** - Material generation
- **scripts/generate_overall_summary.py** - Summary generation

## Output Structure

### Public Deliverables
```
artifacts/public/hiring/candidates/{date}_consolidated/
├── {candidate_id}_{name}/
│   ├── screening/screening_report.md
│   ├── takehome/takehome_assignment.md
│   ├── interview/candidate_context.md, interview_guide.md, interview_script.md
│   ├── evaluation/evaluation_framework.md
│   └── candidate_summary.md
├── HIRING_SUMMARY_COMPLETE.md
└── QUICK_REFERENCE_GUIDE.md
```

### Private Working Files (Debug/Logs)
```
data/private/hiring/working/{run_id}/
├── run_config.json
├── context_validation_report.json
├── candidates_normalized.json
├── jd_mapping_{candidate_id}.md
├── screening_summary.json
└── FINAL_WORKFLOW_SUMMARY.json
```

## Key Features
- **Single Version Per Candidate**: No duplicate files or confusion
- **Complete Material Generation**: All necessary documents auto-generated
- **Customized Assignments**: Take-home assignments based on experience level
- **Structured Interviews**: Comprehensive interview guides and scripts
- **Decision Support**: Evaluation frameworks and scoring matrices
- **Production Ready**: All materials ready for immediate use

## Archive
Obsolete and old versions are stored in `ARCHIVED/` directory with timestamps.

---
*This workflow represents the current production version of the Gefjon Growth hiring process.*
