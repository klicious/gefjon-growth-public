---
id: context_verification_task
type: task
domain: hiring
stage: 1
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [context, verification, validation]
visibility: public
version: 1.0
---

# Task 1: Context Load & Verification

**Purpose**: Verify all required context files and validate input data before proceeding with hiring workflow.

## Objectives
- Ensure all required context files exist and are accessible
- Validate candidate JSON schema and data integrity
- Run complete context engineering checklist
- Establish execution environment and run ID

## Required Context Files

### Company Information
- `context/company_info/mission_vision_values.yaml`
- Verify: Mission statement, core values, company culture

### HR Processes
- `context/hr_processes/hiring/hiring_stages.yaml`
- Verify: Stage definitions, approval workflows, quality gates

### Interview Process
- `artifacts/public/hiring/interview_process.md`
- Verify: Interview types, evaluation criteria, rubrics

## Input Validation

### Candidates JSON
- **Location**: `data/public/hiring/resume/candidates.json`
- **Schema Requirements**:
  - Array of candidate objects
  - Required fields: name, email, experience, skills
  - Optional fields: candidate_id, portfolio_url, github_url

### Job Description
- **Location**: `artifacts/public/hiring/job_descriptions/backend_mid_level.md`
- **Requirements**: Role requirements, technical skills, experience level

## Execution Steps

### 1. Context File Verification
```bash
# Check all required context files exist
ls -la context/company_info/mission_vision_values.yaml
ls -la context/hr_processes/hiring/hiring_stages.yaml
ls -la artifacts/public/hiring/interview_process.md
```

### 2. Input Data Validation
- Load and parse `candidates.json`
- Validate JSON schema
- Check for required fields
- Identify any data quality issues

### 3. Environment Setup
- Generate unique run ID: `{YYYYMMDD}_{HHMMSS}_{random}`
- Create working directory: `data/private/hiring/working/{run_id}/`
- Initialize execution log

### 4. Context Engineering Checklist
- [ ] All context files loaded successfully
- [ ] Candidate data validated and parsed
- [ ] Job description accessible
- [ ] Working directory created
- [ ] MCP servers available (exa, sequential-thinking, playwright, fetch)
- [ ] Execution environment ready

## Outputs

### Success
- **Execution Log**: `data/private/hiring/working/{run_id}/execution.log`
- **Validated Data**: `data/private/hiring/working/{run_id}/candidates.validated.json`
- **Context Summary**: `data/private/hiring/working/{run_id}/context_summary.md`

### Failure Conditions
- Missing required context files
- Invalid JSON schema
- Insufficient candidate data
- MCP server unavailability

## Quality Gates
- **Context Completeness**: 100% required files present
- **Data Integrity**: Valid JSON with all required fields
- **Environment Readiness**: All systems operational

## Error Handling
- **Missing Context**: Stop execution, request specific missing files
- **Invalid Data**: Report specific validation errors
- **System Issues**: Log error details and escalate

## Next Stage
Upon successful completion, proceed to **Task 2: Intake & Normalization**

## MCP Integration
- **sequential-thinking**: Plan verification steps
- **fetch**: Retrieve any missing context files if URLs provided

## Execution Command
```bash
gemini run --prompt "ai_docs/workflows/hiring/tasks/01_context_verification.md"
```