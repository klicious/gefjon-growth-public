---
id: candidate_splitting_task
type: task
domain: hiring
stage: 0
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [splitting, organization, individual_files, data_management]
visibility: public
version: 1.0
---

# Task 0: Candidate Data Splitting & Organization

**Purpose**: Split bulk candidate JSON data into individual candidate files for better organization, tracking, and parallel processing throughout the hiring workflow.

## Prerequisites
- **Input Data**: Bulk candidate JSON file (e.g., `data/public/hiring/resume/20250731/candidates_20250731.json`)
- **Directory Structure**: Established hiring workflow directory structure
- **File Permissions**: Write access to candidate data directories

## Objectives
- Split bulk candidate array into individual JSON files per candidate
- Create organized directory structure for candidate tracking
- Generate candidate registry for workflow management
- Establish consistent file naming conventions
- Enable parallel processing and individual candidate tracking
- Maintain data integrity and completeness

## Input Structure Analysis

### Expected Bulk Format
```json
[
  {
    "candidate_id": "kim_atlas-cand",
    "name_local": "atlas-cand",
    "name_en": "atlas-cand",
    // ... complete candidate data
  },
  {
    "candidate_id": "kim_orion-cand", 
    "name_local": "orion-cand",
    "name_en": "orion-cand",
    // ... complete candidate data
  }
  // ... additional candidates
]
```

### Candidate Data Validation
- Verify `candidate_id` field exists and is unique
- Ensure required fields are present (name, contact info, etc.)
- Check for data completeness and consistency
- Identify any parsing errors or missing information

## Processing Steps

### 1. Data Loading & Validation
- Load bulk candidate JSON file
- Validate JSON structure and format
- Check for required fields in each candidate record
- Identify any data quality issues or inconsistencies

### 2. Directory Structure Creation
Create organized directory structure for individual candidates:
```
data/public/hiring/candidates/individual/
├── {date}/
│   ├── kim_atlas-cand.json
│   ├── kim_orion-cand.json
│   ├── kim_nova-cand.json
│   └── ...
└── registry/
    └── {date}_candidate_registry.json
```

### 3. Individual File Generation
- Extract each candidate object from the bulk array
- Create individual JSON file per candidate
- Apply consistent naming convention: `{candidate_id}.json`
- Preserve all original data fields and structure
- Add metadata for tracking and processing

### 4. Registry Creation
Generate a candidate registry file for workflow management:
```json
{
  "batch_info": {
    "source_file": "candidates_20250731.json",
    "processing_date": "2025-08-11T10:30:00Z",
    "total_candidates": 15,
    "batch_id": "batch_20250731"
  },
  "candidates": [
    {
      "candidate_id": "kim_atlas-cand",
      "file_path": "data/public/hiring/candidates/individual/20250731/kim_atlas-cand.json",
      "name_en": "atlas-cand",
      "name_local": "atlas-cand",
      "status": "ready_for_processing",
      "created_at": "2025-08-11T10:30:00Z"
    }
    // ... additional candidates
  ]
}
```

## Output Structure

### Individual Candidate Files
**Location**: `data/public/hiring/candidates/individual/{date}/{candidate_id}.json`

Each file contains the complete candidate data with added metadata:
```json
{
  "processing_metadata": {
    "source_batch": "batch_20250731",
    "split_date": "2025-08-11T10:30:00Z",
    "file_version": "1.0",
    "workflow_status": "ready_for_processing"
  },
  "candidate_data": {
    "candidate_id": "kim_atlas-cand",
    "name_local": "atlas-cand",
    "name_en": "atlas-cand",
    // ... all original candidate fields
  }
}
```

### Candidate Registry
**Location**: `data/public/hiring/candidates/registry/{date}_candidate_registry.json`

Master registry tracking all candidates in the batch:
```json
{
  "batch_info": {
    "source_file": "data/public/hiring/resume/20250731/candidates_20250731.json",
    "processing_date": "2025-08-11T10:30:00Z",
    "processor": "Kiro AI Assistant",
    "total_candidates": 15,
    "batch_id": "batch_20250731",
    "workflow_version": "2.0"
  },
  "candidates": [
    {
      "candidate_id": "kim_atlas-cand",
      "file_path": "data/public/hiring/candidates/individual/20250731/kim_atlas-cand.json",
      "name_en": "atlas-cand",
      "name_local": "atlas-cand",
      "experience_years": 1.17,
      "primary_skills": ["Python", "Java", "AWS", "Docker"],
      "status": "ready_for_processing",
      "created_at": "2025-08-11T10:30:00Z",
      "last_updated": "2025-08-11T10:30:00Z"
    },
    {
      "candidate_id": "kim_orion-cand",
      "file_path": "data/public/hiring/candidates/individual/20250731/kim_orion-cand.json", 
      "name_en": "orion-cand",
      "name_local": "orion-cand",
      "experience_years": 4.83,
      "primary_skills": ["Java", "Spring", "Oracle", "EDI"],
      "status": "ready_for_processing",
      "created_at": "2025-08-11T10:30:00Z",
      "last_updated": "2025-08-11T10:30:00Z"
    }
    // ... additional candidates
  ],
  "statistics": {
    "experience_distribution": {
      "entry_level": 3,
      "mid_level": 8,
      "senior_level": 4
    },
    "skill_distribution": {
      "Java": 12,
      "Python": 8,
      "Spring": 10,
      "AWS": 6
    },
    "language_distribution": {
      "ko": 15,
      "en": 2
    }
  }
}
```

### Processing Summary
**Location**: `data/public/hiring/candidates/processing/{date}_splitting_summary.md`

```markdown
# Candidate Splitting Summary

**Date**: 2025-08-11
**Batch ID**: batch_20250731
**Source File**: data/public/hiring/resume/20250731/candidates_20250731.json

## Processing Results
- **Total Candidates**: 15
- **Successfully Split**: 15
- **Errors**: 0
- **Processing Time**: 2.3 seconds

## Candidate Overview
| Candidate ID | Name | Experience | Primary Skills |
|--------------|------|------------|----------------|
| kim_atlas-cand | atlas-cand | 1.2 years | Python, AWS, Docker |
| kim_orion-cand | orion-cand | 4.8 years | Java, Spring, Oracle |
| ... | ... | ... | ... |

## Quality Checks
- [x] All candidates have unique IDs
- [x] Required fields present in all records
- [x] No data corruption detected
- [x] File naming conventions applied
- [x] Registry generated successfully

## Next Steps
1. Proceed to Task 1: Context Verification
2. Individual candidates ready for parallel processing
3. Registry available for workflow orchestration
```

## Data Quality Validation

### Required Field Checks
- `candidate_id`: Must be unique and non-empty
- `name_en` or `name_local`: At least one name field required
- `contacts`: Email or phone contact information
- `sections`: Resume sections with experience/education data
- `entities`: Extracted skills and competencies

### Data Integrity Verification
- JSON structure validity for each candidate
- No duplicate candidate IDs within batch
- Consistent field naming and data types
- Complete data preservation from source to individual files

### Error Handling
- **Missing candidate_id**: Generate ID from name or sequence
- **Duplicate IDs**: Append sequence number (e.g., `kim_atlas-cand_2`)
- **Incomplete data**: Flag for manual review but include in processing
- **JSON parsing errors**: Log error and skip malformed records

## Quality Gates
- **Complete Data Preservation**: All original data maintained in individual files
- **Unique Identification**: Each candidate has unique, consistent ID
- **File Organization**: Proper directory structure and naming conventions
- **Registry Accuracy**: Registry matches individual files exactly
- **Processing Efficiency**: Splitting completed within reasonable time

## Success Criteria
- All candidates from bulk file successfully split into individual files
- Candidate registry generated with complete metadata
- Directory structure properly organized for workflow processing
- No data loss or corruption during splitting process
- Individual files ready for subsequent workflow stages

## Integration with Workflow

### Updated Workflow Sequence
1. **Task 0**: Candidate Splitting & Organization ← **NEW**
2. **Task 1**: Context Verification (uses individual files)
3. **Task 2**: Intake & Normalization (processes individual files)
4. **Subsequent Tasks**: Continue with individual candidate processing

### Parallel Processing Enablement
- Individual files allow parallel processing of candidates
- Registry enables batch tracking and status management
- Consistent file structure supports automated workflow orchestration

## MCP Integration
- **sequential-thinking**: Structure splitting logic and validation steps
- **exa**: Research best practices for candidate data organization

## Execution Command
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/00_candidate_splitting.md" \
  --source-file "data/public/hiring/resume/20250731/candidates_20250731.json" \
  --output-date "20250731"
```

## Validation Checklist
- [ ] Source file loaded and validated successfully
- [ ] Directory structure created for individual candidates
- [ ] All candidates split into individual JSON files
- [ ] Candidate registry generated with complete metadata
- [ ] Data integrity verified (no loss or corruption)
- [ ] File naming conventions applied consistently
- [ ] Processing summary documentation created
- [ ] Individual files ready for subsequent workflow stages