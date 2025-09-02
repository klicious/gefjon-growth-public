# Gefjon Growth Hybrid Hiring Workflow
## BEI Core Values + Enhanced Technical Assessment

## Overview
This directory contains the complete, production-ready **Hybrid BEI + Enhanced Technical Assessment** workflow for Gefjon Growth. The workflow preserves traditional Behavioral Event Interviewing for all 10 core values (60% weight) while adding enhanced technical evaluation for AI-assisted development and platform engineering (40% weight). Implements a single-candidate directory approach with comprehensive hybrid materials generation.

## Current Workflow Version
**Version**: 2.1 (Hybrid BEI + Enhanced Technical Assessment)  
**Assessment Framework**: 60% Core Values + 40% Enhanced Technical = 75-point scoring  
**Last Updated**: 2025-09-02  
**Status**: Production Ready - Addresses Phoenix_005 Assessment Gap  
**Legacy Version**: v2.0 archived in `archive/legacy_v1.0/`

## Quick Start

### Run Complete Hybrid Workflow
```bash
python scripts/complete_hybrid_workflow_integration.py
```

### Individual Hybrid Components
```bash
# Consolidate existing results with hybrid scoring
python scripts/consolidate_hybrid_hiring_results.py

# Generate complete hybrid materials
python scripts/generate_hybrid_candidate_materials.py

# Generate hybrid assessment summary
python scripts/generate_hybrid_overall_summary.py
```

### Alternative: Direct Gemini Execution
```bash
# Single candidate hybrid assessment
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt_v2.1_hybrid.md" \
  --context "data/public/hiring/resume/{candidate_file}.json"

# Complete workflow with hybrid methodology  
gemini run \
  --prompt "ai_docs/workflows/hiring/orchestrator.md" \
  --mode "hybrid_assessment"
```

## Workflow Components

### Core Hybrid Files
- **orchestrator.md** - Main hybrid workflow orchestration and execution guide
- **single_candidate_workflow.md** - Detailed hybrid single-candidate approach documentation  
- **tasks/06_interview_kit_hybrid.md** - Hybrid interview kit generation task (BEI + enhanced technical)
- **validation_framework.md** - Quality assurance and validation processes for hybrid assessment
- **ai_agent_execution_guide.md** - Guide for AI agents executing the hybrid workflow

### Configuration
- **config/workflow_config.yaml** - Primary workflow configuration
- **tasks/** - Individual task definitions and specifications

### Hybrid Scripts
- **scripts/complete_hybrid_workflow_integration.py** - Master hybrid integration script
- **scripts/consolidate_hybrid_hiring_results.py** - Hybrid result consolidation with 75-point scoring
- **scripts/generate_hybrid_candidate_materials.py** - Hybrid material generation (BEI + technical)
- **scripts/generate_hybrid_overall_summary.py** - Hybrid assessment summary generation

## Output Structure

### Hybrid Public Deliverables
```
artifacts/public/hiring/candidates/{date}_consolidated/
├── {candidate_id}_{name}/
│   ├── screening/hybrid_screening_report.md
│   ├── takehome/takehome_assignment.md (AI collaboration focus)
│   ├── interview/
│   │   ├── candidate_context.md (hybrid assessment analysis)
│   │   ├── interview_guide.md (BEI + enhanced technical)
│   │   └── interview_script.md (STAR questions + technical guidance)
│   ├── evaluation/hybrid_evaluation_framework.md (75-point scoring)
│   └── candidate_summary.md (hybrid assessment summary)
├── HYBRID_HIRING_SUMMARY_COMPLETE.md
└── HYBRID_QUICK_REFERENCE_GUIDE.md
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

## Key Hybrid Features
- **Preserved Organizational DNA**: All 10 core values assessed using traditional BEI methodology (60% weight)
- **Enhanced Technical Assessment**: AI-assisted development and platform engineering evaluation (40% weight)
- **Phoenix_005 Resolution**: Technical capability properly assessed while maintaining cultural alignment
- **75-Point Hybrid Scoring**: 50 points BEI + 25 points technical with clear decision thresholds
- **Evidence-Based Assessment**: PROVEN/SUGGESTED/MISSING framework for systematic evaluation
- **Single Version Per Candidate**: No duplicate files or confusion
- **Complete Hybrid Material Generation**: All necessary documents auto-generated with dual methodology
- **AI Collaboration Focus**: Take-home assignments emphasize AI-assisted development capability
- **Structured Hybrid Interviews**: 95-minute format (40min BEI + 50min enhanced technical)
- **Decision Support**: Hybrid evaluation frameworks and 75-point scoring matrices
- **Production Ready**: All hybrid materials ready for immediate use

## Hybrid Assessment Benefits
- **Cultural Alignment Maintained**: 60% weight ensures core values remain primary hiring criterion
- **Technical Gaps Addressed**: AI collaboration and platform engineering properly evaluated
- **False Negative Reduction**: Candidates like Phoenix_005 now properly assessed
- **Organizational DNA Preserved**: BEI methodology and STAR format maintained exactly
- **Enhanced Prediction**: Better correlation between assessment scores and job performance

## Archive
Legacy workflow v2.0 and earlier versions are stored in `archive/legacy_v1.0/` directory with complete migration documentation.

---
*This **Hybrid BEI + Enhanced Technical Assessment** workflow represents the current production version of the Gefjon Growth hiring process, addressing technical assessment gaps while preserving organizational DNA.*
