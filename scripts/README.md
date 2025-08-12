# Gefjon Growth Hiring Scripts

## Production Scripts (Current)

### Master Integration
- **complete_workflow_final.py** - Complete workflow integration with verification
  - Runs all components in correct order
  - Verifies completeness and consistency
  - Production-ready execution

### Core Components
- **consolidate_hiring_results.py** - Consolidate scattered results into single candidate directories
- **generate_enhanced_materials.py** - Generate complete materials for all candidates
- **generate_overall_summary.py** - Create comprehensive hiring summary
- **verify_workflow_consistency.py** - Verify workflow configuration matches results

### Utilities
- **split_candidates.py** - Process and split candidate data
- **validate_hr_context.py** - Validate HR context and configuration

## Quick Start

### Run Complete Workflow
```bash
python scripts/complete_workflow_final.py
```

This single command will:
- Consolidate existing results
- Generate all missing materials
- Create comprehensive summaries
- Verify completeness and consistency

### Run Individual Components
```bash
# Step 1: Consolidate results
python scripts/consolidate_hiring_results.py

# Step 2: Generate materials
python scripts/generate_enhanced_materials.py

# Step 3: Generate summary
python scripts/generate_overall_summary.py

# Step 4: Verify consistency
python scripts/verify_workflow_consistency.py
```

## Script Descriptions

### complete_workflow_final.py
**Purpose**: Master integration script that runs the complete hiring workflow
**Input**: Screening data and candidate information
**Output**: Complete candidate directories with all materials
**Usage**: Primary script for production workflow execution

### consolidate_hiring_results.py
**Purpose**: Consolidate scattered hiring results into organized candidate directories
**Input**: Existing hiring materials in various locations
**Output**: Single directory per candidate with standardized structure
**Usage**: First step in workflow organization

### generate_enhanced_materials.py
**Purpose**: Generate complete, comprehensive materials for all candidates
**Input**: Candidate data and screening results
**Output**: Screening reports, interview materials, communication templates
**Usage**: Core material generation for hiring decisions

### generate_overall_summary.py
**Purpose**: Create executive summary of all candidates and hiring status
**Input**: Consolidated candidate data
**Output**: HIRING_SUMMARY_COMPLETE.md and QUICK_REFERENCE_GUIDE.md
**Usage**: Executive reporting and decision support

### verify_workflow_consistency.py
**Purpose**: Verify that workflow configuration matches actual implementation
**Input**: Workflow config and generated materials
**Output**: Consistency verification report
**Usage**: Quality assurance and validation

## Archive

Obsolete and superseded scripts are stored in `ARCHIVED/` directory with timestamps and reasons for archival.

---
*Last updated: 2025-08-11*
*All scripts are production-ready and tested*
