---
id: intake_normalization_task
type: task
domain: hiring
stage: 2
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [intake, normalization, data-processing]
visibility: public
version: 1.0
---

# Task 2: Intake & Normalization

**Purpose**: Normalize candidate data, assign IDs, and prepare standardized data structure for downstream processing.

## Prerequisites
- **Task 1 Completed**: Context verification successful
- **Input**: `data/private/hiring/working/{run_id}/candidates.validated.json`
- **Working Directory**: `data/private/hiring/working/{run_id}/`

## Objectives
- Normalize candidate fields to standard schema
- Assign unique candidate IDs using established pattern
- Create standardized data structure for workflow processing
- Apply PII masking only when creating presentation/demo samples
- Preserve actual contact information for real hiring processes

## Normalization Schema

### Standard Candidate Fields
```json
{
  "candidate_id": "string (atlas_001, nova_002 pattern)",
  "name": "string (preserved for hiring process)",
  "email": "string (preserved for hiring process)", 
  "phone": "string (preserved for hiring process)",
  "experience_years": "number",
  "skills": ["array of strings"],
  "education": "string",
  "portfolio_url": "string (optional)",
  "github_url": "string (optional)",
  "linkedin_url": "string (optional)",
  "current_role": "string",
  "location": "string",
  "availability": "string",
  "salary_expectation": "string (optional)",
  "normalized_at": "timestamp",
  "source": "string (application source)",
  "processing_mode": "string (production|demo)"
}
```

### ID Assignment Pattern
- **Format**: `{mythological_name}_{sequential_number}`
- **Examples**: `atlas_001`, `nova_002`, `orion_003`, `luna_004`
- **Sequence**: Maintain global counter across all hiring runs

## Processing Steps

### 1. Data Loading
- Load validated candidates from Task 1
- Parse existing data structure
- Identify missing or inconsistent fields

### 2. Field Normalization
- **Name**: Standardize format (First Last)
- **Email**: Validate format and domain
- **Experience**: Convert to numeric years
- **Skills**: Normalize skill names, remove duplicates
- **URLs**: Validate and standardize format

### 3. ID Assignment
- Check for existing candidate_id
- If missing, assign new ID using mythological pattern
- Maintain ID registry to prevent duplicates
- Update global counter

### 4. PII Handling (Mode-Dependent)
**Production Mode (Actual Hiring)**:
- Preserve all contact information (name, email, phone)
- Maintain actual location data for logistics
- Keep all personal details needed for hiring process

**Demo/Presentation Mode**:
- Replace actual names with candidate_id references
- Mask email domains (keep structure for validation)
- Generalize location data to city/state level
- Create sanitized versions for public presentation

### 5. Data Validation
- Verify all required fields present
- Check data type consistency
- Validate URL accessibility (optional)
- Ensure schema compliance

## Outputs

### Primary Output
- **Production Mode**: `data/private/hiring/working/{run_id}/candidates.normalized.json` (full data)
- **Demo Mode**: `data/private/hiring/working/{run_id}/candidates.normalized.json` (masked data)

### Supporting Files
- **ID Registry**: `data/private/hiring/working/{run_id}/candidate_ids.json`
- **Normalization Log**: `data/private/hiring/working/{run_id}/normalization.log`
- **Processing Mode Log**: `data/private/hiring/working/{run_id}/processing_mode.log`

### Sample Normalized Output

**Production Mode (Actual Hiring)**:
```json
[
  {
    "candidate_id": "atlas_001",
    "name": "John Smith",
    "email": "john.smith@email.com",
    "phone": "+1-555-123-4567",
    "experience_years": 5,
    "skills": ["Python", "Django", "PostgreSQL", "AWS"],
    "education": "BS Computer Science",
    "github_url": "https://github.com/johnsmith",
    "current_role": "Backend Developer",
    "location": "San Francisco, CA",
    "availability": "2 weeks notice",
    "normalized_at": "2025-08-11T10:30:00Z",
    "source": "company_website",
    "processing_mode": "production"
  }
]
```

**Demo/Presentation Mode**:
```json
[
  {
    "candidate_id": "atlas_001",
    "name": "[CANDIDATE_NAME]",
    "email": "[EMAIL]@[domain].com",
    "phone": "[PHONE_NUMBER]",
    "experience_years": 5,
    "skills": ["Python", "Django", "PostgreSQL", "AWS"],
    "education": "BS Computer Science",
    "github_url": "https://github.com/[username]",
    "current_role": "Backend Developer",
    "location": "[CITY], [STATE]",
    "availability": "2 weeks notice",
    "normalized_at": "2025-08-11T10:30:00Z",
    "source": "company_website",
    "processing_mode": "demo"
  }
]
```

## Quality Gates
- **Schema Compliance**: 100% fields match standard schema
- **ID Uniqueness**: No duplicate candidate IDs
- **Data Integrity**: All required fields populated
- **Contact Information**: Preserved in production mode for hiring communication
- **Demo Safety**: PII properly masked only in demo/presentation mode

## Error Handling
- **Missing Fields**: Use default values or mark as incomplete
- **Invalid Data**: Log issues and attempt correction
- **ID Conflicts**: Generate alternative IDs
- **Schema Violations**: Report and request manual review

## Data Handling & Compliance

### Production Mode (Actual Hiring)
- **Contact Preservation**: Maintain all contact information for candidate communication
- **GDPR Compliance**: Data used only for legitimate hiring purposes
- **Secure Storage**: Store full candidate data in private directories
- **Retention Policy**: Follow company data retention guidelines

### Demo/Presentation Mode
- **PII Protection**: Mask sensitive personal information
- **Public Safety**: Safe for presentations and documentation
- **Data Minimization**: Only show necessary information for demonstration
- **Transparency**: Clear labeling of demo vs production data

### Processing Mode Selection
- **Default**: Production mode for actual hiring processes
- **Demo Flag**: Explicitly set `--demo-mode` for presentation materials
- **Mode Logging**: Track which mode was used for each processing run

## Next Stage
Upon successful completion, proceed to **Task 3: JD Mapping & Competency Alignment**

## MCP Integration
- **sequential-thinking**: Plan normalization steps
- **exa**: Validate company domains and URLs (optional)

## Execution Command

**Production Mode (Default - Actual Hiring)**:
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/02_intake_normalization.md" \
  --context "data/public/hiring/candidates/individual/{date}/{candidate_id}.json" \
  --mode "production"
```

**Demo/Presentation Mode**:
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/02_intake_normalization.md" \
  --context "data/public/hiring/candidates/individual/{date}/{candidate_id}.json" \
  --mode "demo"
```

## Success Criteria
- All candidates have valid candidate_ids using mythological naming pattern
- Data structure matches standard schema
- **Production Mode**: Contact information preserved for hiring communication
- **Demo Mode**: PII properly masked for safe presentation
- Processing mode clearly documented and logged
- Normalization log shows 100% success rate