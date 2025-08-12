---
id: ai_agent_execution_guide
type: guide
domain: hiring
created_date: 2025-08-11
author: Kiro
quality_score: 9.5/10
tags: [ai-agent, execution, guide, automation, error-prevention]
visibility: public
version: 1.0
---

# AI Agent Execution Guide for Hiring Workflow

**Purpose**: Comprehensive guide for AI agents to execute the hiring workflow flawlessly with error prevention, validation, and recovery procedures.

## Critical Success Factors

### 1. Context Engineering Compliance (MANDATORY)
Every AI agent MUST follow the context engineering methodology:

```markdown
BEFORE executing ANY stage:
1. ✅ Load ALL required context files using readMultipleFiles
2. ✅ Validate context completeness and accuracy
3. ✅ Check for missing or outdated information
4. ✅ Request missing context if completeness < 90%
5. ✅ Document context validation results
```

### 2. Data Integrity Validation (MANDATORY)
```markdown
BEFORE processing candidates:
1. ✅ Verify candidate data structure and format
2. ✅ Check for required fields and completeness
3. ✅ Validate contact information (production mode)
4. ✅ Ensure no data corruption or missing files
5. ✅ Generate data quality report
```

### 3. Error Prevention Checklist (MANDATORY)
```markdown
AT EACH STAGE:
1. ✅ Verify all prerequisites are met
2. ✅ Check tool availability (MCP servers)
3. ✅ Validate input data before processing
4. ✅ Monitor quality scores during generation
5. ✅ Implement retry logic for failures
6. ✅ Create checkpoint saves for recovery
```

## Pre-Execution Validation Protocol

### Step 1: Environment Assessment
```bash
# Check required directories exist
- data/public/hiring/candidates/individual/{date}/
- context/company_info/
- context/hr_processes/hiring/
- artifacts/public/hiring/

# Verify MCP server availability
- sequential-thinking (required)
- fetch (required)
- exa (optional)
- playwright (optional)
```

### Step 2: Context Engineering Validation
```markdown
Required Context Files Checklist:
□ context/company_info/mission_vision_values.yaml
□ context/hr_processes/hiring/hiring_stages.yaml
□ data/private/platform_development_team.md
□ data/private/hiring/job_description_kr.md
□ ai_docs/workflows/hiring/plans/candidate_screening_plan.md

Validation Actions:
1. Use readMultipleFiles to load all context files
2. Check each file for required sections and content
3. Validate YAML/Markdown format integrity
4. Ensure no placeholder or incomplete content
5. Generate context_completeness_report.json
```

### Step 3: Input Data Validation
```markdown
Candidate Data Validation:
1. Use listDirectory to discover all candidate files
2. Use readMultipleFiles to load candidate data
3. Validate JSON structure and required fields
4. Check for data completeness and quality
5. Verify contact information availability
6. Generate candidate_data_quality_report.json
```

## Stage-by-Stage Execution Instructions

### Stage 0: Pre-Flight Validation (CRITICAL)
```markdown
EXECUTION STEPS:
1. Create unique run_id: "{YYYYMMDD}_{HHMMSS}_hiring_run"
2. Create working directory structure
3. Initialize execution log with run_config.json
4. Validate ALL context files (stop if any missing)
5. Validate ALL candidate data (report quality issues)
6. Check MCP server availability
7. Generate pre_flight_validation_report.json

STOP CONDITIONS:
- Any required context file missing or invalid
- Candidate data completeness < 70%
- Required MCP servers unavailable
- Working directory creation fails

SUCCESS CRITERIA:
- All context files loaded and validated
- All candidate files loaded successfully
- Working directory structure created
- Execution log initialized
```

### Stage 1: Context Verification (ENHANCED)
```markdown
EXECUTION STEPS:
1. Load context files using readMultipleFiles tool
2. Parse and validate each context file structure
3. Check for required sections and completeness
4. Cross-reference context consistency
5. Generate context_validation_report.json
6. Update execution log with results

QUALITY GATES:
- Context completeness ≥ 90%
- All required sections present
- No format or structure errors
- Cross-reference validation passed

ERROR HANDLING:
- Missing files: Stop execution, request specific files
- Invalid format: Report specific errors, request corrections
- Incomplete content: Identify missing sections, request completion
```

### Stage 2: Intake & Normalization (ENHANCED)
```markdown
EXECUTION STEPS:
1. Load all candidate files from source directory
2. Validate data structure and completeness
3. Generate unique candidate IDs (atlas_001, nova_002, etc.)
4. Normalize data structure to standard schema
5. Preserve contact information (production mode)
6. Create candidates.normalized.json
7. Generate normalization_quality_report.json

QUALITY GATES:
- All candidate files processed successfully
- Data completeness ≥ 80% per candidate
- No candidate ID collisions
- Standard schema compliance 100%

ERROR HANDLING:
- File read errors: Log specific files, continue with available data
- Data format issues: Report validation errors, attempt correction
- Missing required fields: Flag for manual review, continue processing
```

### Stage 3: JD Mapping (ENHANCED)
```markdown
EXECUTION STEPS:
1. Load job description using readFile
2. Parse requirements and create competency matrix
3. For each candidate, perform skills mapping analysis
4. Generate experience level assessment
5. Create skill gap analysis with recommendations
6. Output jd_mapping_{candidate_id}.json for each candidate
7. Generate jd_mapping_summary.json

QUALITY GATES:
- JD mapping completed for all candidates
- Skills analysis confidence ≥ 75%
- Experience level classification accurate
- Gap analysis specific and actionable

ERROR HANDLING:
- JD parsing errors: Request clarification, use fallback analysis
- Skills mapping failures: Use partial analysis, flag for review
- Low confidence scores: Generate additional analysis, request validation
```

### Stage 4: Automated Screening (ENHANCED)
```markdown
EXECUTION STEPS:
1. Load screening plan using readFile
2. Apply multi-dimensional analysis framework
3. Generate evidence-based scoring for each dimension
4. Perform automated bias check on content
5. Create detailed screening reports
6. Generate screening_summary.json with statistics
7. Filter candidates based on decision thresholds

QUALITY GATES:
- Screening reports quality score ≥ 8.5/10
- Evidence provided for all assessments
- Bias check passed (neutral language)
- Recommendations align with scoring

DECISION THRESHOLDS:
- Strong Hire (≥9.0): Proceed to take-home assignment
- Hire (≥8.0): Proceed to take-home assignment
- Lean Hire (≥6.5): Additional assessment required
- No Hire (<6.5): Decline with constructive feedback

ERROR HANDLING:
- Low quality scores: Regenerate with enhanced prompts (max 3 attempts)
- Bias detection: Revise language, ensure neutrality
- Scoring inconsistencies: Review evidence, adjust scores
```

### Stage 5: Take-Home Assignment (ENHANCED)
```markdown
EXECUTION STEPS:
1. Filter candidates based on screening results (≥8.0 threshold)
2. Load candidate profiles and screening reports
3. Select appropriate assignment template
4. Personalize assignment based on candidate background
5. Generate customized evaluation sheets
6. Create assignment packages with instructions
7. Generate takehome_assignment_summary.json

PERSONALIZATION FACTORS:
- Technical background and expertise
- Experience level and complexity
- Identified strengths and growth areas
- Company value alignment opportunities

QUALITY GATES:
- Assignment appropriately personalized
- Evaluation criteria aligned with role requirements
- Clear instructions and expectations
- Realistic timeline and deliverables

ERROR HANDLING:
- Template selection errors: Use default template, flag for review
- Personalization failures: Use standard assignment, note limitations
- Evaluation criteria issues: Use baseline rubric, enhance manually
```

### Stage 6: Interview Kit Generation (ENHANCED)
```markdown
EXECUTION STEPS:
1. Load all candidate data and screening results
2. Generate candidate context briefing
3. Create personalized interview guide
4. Generate complete interview script
5. Create evaluation rubrics and scoring criteria
6. Generate interview_kit_summary.json

QUALITY GATES:
- All three files generated per candidate
- Personalization elements present and relevant
- Questions aligned with company values
- Technical assessments appropriate for role level

ERROR HANDLING:
- Content generation failures: Retry with enhanced context
- Personalization issues: Use template questions, add manual notes
- Quality threshold failures: Regenerate specific sections
```

## Error Prevention Strategies

### 1. Proactive Validation
```markdown
BEFORE each stage:
- Validate all inputs and dependencies
- Check tool availability and functionality
- Verify data integrity and completeness
- Confirm output directory structure exists
```

### 2. Graceful Error Handling
```markdown
DURING execution:
- Implement try-catch logic for all operations
- Use retry mechanisms with exponential backoff
- Provide fallback methods for critical failures
- Log all errors with specific context
```

### 3. Recovery Procedures
```markdown
AFTER errors:
- Generate detailed error reports
- Provide specific resolution guidance
- Create checkpoint saves for resumption
- Escalate to human review when needed
```

## Quality Assurance Framework

### Automated Quality Checks
```yaml
content_quality:
  threshold: 8.5
  validation_points:
    - completeness: all_sections_present
    - accuracy: evidence_based_claims
    - relevance: candidate_specific_content
    - clarity: professional_language

bias_detection:
  language_analysis: neutral_tone_required
  demographic_blindness: no_identifying_characteristics
  recommendation_consistency: evidence_based_only

data_integrity:
  format_validation: schema_compliance
  completeness_check: required_fields_present
  consistency_validation: cross_reference_accuracy
```

### Human Approval Integration
```yaml
approval_gates:
  stage_4_screening:
    approver: platform_lead
    criteria: quality_threshold_met
    timeout: 24_hours
    
  stage_5_takehome:
    approver: platform_lead
    criteria: assignment_appropriateness
    timeout: 12_hours
    
  stage_6_interview_kit:
    approver: platform_lead
    criteria: material_completeness
    timeout: 12_hours
```

## Execution Monitoring & Logging

### Real-Time Monitoring
```json
{
  "run_id": "20250811_143000_enhanced",
  "current_stage": "04_screening",
  "progress": {
    "total_candidates": 4,
    "processed_candidates": 2,
    "completion_percentage": 50
  },
  "quality_metrics": {
    "average_score": 8.9,
    "min_score": 8.5,
    "max_score": 9.3
  },
  "errors": [],
  "warnings": ["candidate_contact_missing: nova_002"]
}
```

### Comprehensive Logging
```markdown
LOG REQUIREMENTS:
- Timestamp all operations
- Record input/output file paths
- Track quality scores and metrics
- Log all errors and warnings
- Document decision rationale
- Record execution duration
```

## Troubleshooting Quick Reference

### Common Issues & Solutions
```markdown
Issue: "Context file not found"
Solution: Check file path, verify context engineering compliance
Command: readFile with exact path from context checklist

Issue: "Candidate data format invalid"
Solution: Validate JSON structure, check required fields
Command: Use data validation schema, report specific errors

Issue: "Quality score below threshold"
Solution: Enhance prompts, add more context, regenerate
Command: Retry with additional context and examples

Issue: "MCP server unavailable"
Solution: Check server status, use fallback methods
Command: Test server connectivity, implement graceful degradation

Issue: "Output directory creation failed"
Solution: Check permissions, verify path structure
Command: Use fsWrite to create directory structure
```

### Emergency Recovery Procedures
```markdown
CRITICAL FAILURE RECOVERY:
1. Save current state to checkpoint file
2. Generate detailed error report
3. Identify last successful stage
4. Provide resumption instructions
5. Escalate to human operator

PARTIAL FAILURE RECOVERY:
1. Continue with available data
2. Flag incomplete sections
3. Generate quality warnings
4. Provide manual completion guidance
5. Update execution log with issues
```

## Best Practices for AI Agents

### 1. Always Use Context Engineering
- Load ALL required context files before starting
- Validate context completeness and accuracy
- Request missing information explicitly
- Document context validation results

### 2. Implement Robust Error Handling
- Use try-catch logic for all operations
- Implement retry mechanisms with backoff
- Provide specific error messages and solutions
- Create recovery checkpoints

### 3. Maintain Quality Standards
- Monitor quality scores continuously
- Regenerate content below threshold
- Perform bias checks on all content
- Validate output completeness

### 4. Ensure Data Integrity
- Validate all input data before processing
- Check for required fields and completeness
- Preserve data relationships and references
- Generate data quality reports

### 5. Provide Clear Communication
- Generate comprehensive execution logs
- Create detailed error reports
- Provide specific resolution guidance
- Update status regularly

---
**Guide Version**: 1.0  
**Target Audience**: AI Agents executing hiring workflow  
**Compliance Level**: Mandatory for all executions  
**Last Updated**: 2025-08-11T14:00:00Z