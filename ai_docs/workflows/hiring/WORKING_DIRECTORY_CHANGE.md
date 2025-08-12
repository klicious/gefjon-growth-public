---
id: working_directory_change
type: change_log
domain: hiring
created_date: 2025-08-12
author: Kiro
quality_score: 9.0/10
tags: [workflow, directory-structure, privacy, debugging]
visibility: public
version: 1.0
---

# Working Directory Privacy Change

## Summary
**Change Date**: August 12, 2025  
**Impact**: Directory structure modification for workflow execution logs  
**Scope**: All hiring workflow tasks and orchestrator  

## Change Details

### Previous Structure
```
data/public/hiring/working/{run_id}/
├── run_config.json
├── context_validation_report.json
├── candidates_normalized.json
├── jd_mapping_*.md
├── screening_summary.json
├── takehome_evaluations.json
└── FINAL_WORKFLOW_SUMMARY.json
```

### New Structure
```
data/private/hiring/working/{run_id}/
├── run_config.json
├── context_validation_report.json
├── candidates_normalized.json
├── jd_mapping_*.md
├── screening_summary.json
├── takehome_evaluations.json
└── FINAL_WORKFLOW_SUMMARY.json
```

## Rationale

### Privacy & Security
- **Debug Information**: Working directory contains execution logs and intermediate processing files
- **Internal Use Only**: These files are for debugging and workflow monitoring, not public consumption
- **Candidate Data**: Contains processed candidate information that should remain private
- **Execution Metadata**: Run configurations and processing logs are internal operational data

### Clear Separation
- **Public Artifacts**: Final deliverables (interview kits, screening reports) remain in `artifacts/public/`
- **Private Working**: Execution logs and intermediate files moved to `data/private/`
- **Source Data**: Input candidate data remains in `data/public/hiring/resume/`

## Files Updated

### Workflow Files
- `ai_docs/workflows/hiring/orchestrator.md`
- `ai_docs/workflows/hiring/validation_framework.md`

### Task Files
- `ai_docs/workflows/hiring/tasks/01_context_verification.md`
- `ai_docs/workflows/hiring/tasks/02_intake_normalization.md`
- `ai_docs/workflows/hiring/tasks/03_jd_mapping.md`
- `ai_docs/workflows/hiring/tasks/04_screening.md`
- `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md`
- `ai_docs/workflows/hiring/tasks/06_interview_kit.md`

### Changes Made
- Updated all directory references from `data/public/hiring/working/` to `data/private/hiring/working/`
- Modified environment setup commands in orchestrator
- Updated all task input/output specifications
- Corrected execution command examples

## Impact Assessment

### ✅ No Impact
- **Final Deliverables**: All interview kits, screening reports, and candidate materials remain in public artifacts
- **Workflow Execution**: No changes to workflow logic or processing
- **Quality Gates**: All validation and quality checks remain unchanged
- **User Experience**: No impact on end-user workflow execution

### ⚠️ Minor Impact
- **Directory Creation**: Scripts must create `data/private/hiring/working/` instead of public version
- **Debug Access**: Debugging files now in private directory (appropriate for their purpose)
- **Documentation**: Updated references in all workflow documentation

## Migration Notes

### For Existing Runs
- Previous runs in `data/public/hiring/working/` can be moved to `data/private/hiring/working/`
- Or left in place as historical records (they will not interfere with new runs)

### For Scripts and Automation
- Update any scripts that reference the working directory path
- Ensure private directory creation permissions are available
- Update monitoring or log collection that may reference old paths

## Validation

### Directory Structure Test
```bash
# Verify private directory creation
mkdir -p data/private/hiring/working/test_run_123/

# Verify public artifacts remain accessible
ls artifacts/public/hiring/candidates/
```

### Workflow Execution Test
```bash
# Test workflow with new directory structure
gemini run \
  --prompt "ai_docs/workflows/hiring/orchestrator.md" \
  --context "data/public/hiring/resume/20250812/candidates_20250812.json"
```

## Benefits

### Security
- Sensitive execution logs properly classified as private
- Clear separation between public deliverables and internal processing
- Reduced risk of accidentally exposing debug information

### Organization
- Cleaner public directory structure
- Logical separation of concerns
- Better alignment with data classification principles

### Maintenance
- Easier debugging with dedicated private working space
- Clear understanding of what should and shouldn't be shared
- Simplified cleanup and archival processes

---

**Status**: ✅ COMPLETE - All workflow files updated  
**Next Steps**: Test workflow execution with new directory structure  
**Rollback**: Revert directory references if issues encountered