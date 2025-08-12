---
id: hiring_workflow_validation_framework
type: framework
domain: hiring
created_date: 2025-08-11
author: Kiro
quality_score: 9.5/10
tags: [validation, error-prevention, quality-assurance, ai-agent]
visibility: public
version: 1.0
---

# Hiring Workflow Validation Framework

**Purpose**: Comprehensive validation framework to prevent errors and ensure consistent execution quality for AI agents running the hiring workflow.

## Pre-Execution Validation Checklist

### Context Engineering Compliance ✅
```yaml
context_files_validation:
  required_files:
    - path: "context/company_info/mission_vision_values.yaml"
      validation: "Contains core values definition with examples"
      action: "readFile and validate YAML structure"
      
    - path: "context/hr_processes/hiring/hiring_stages.yaml"
      validation: "Contains complete hiring stage definitions"
      action: "readFile and validate stage completeness"
      
    - path: "data/private/platform_development_team.md"
      validation: "Contains team context and requirements"
      action: "readFile and validate content sections"
      
    - path: "data/private/hiring/job_description_kr.md"
      validation: "Contains role requirements and specifications"
      action: "readFile and validate job requirements"

  validation_actions:
    - load_all_files: "Use readMultipleFiles for batch loading"
    - check_completeness: "Verify all required sections present"
    - validate_format: "Ensure proper YAML/Markdown structure"
    - cross_reference: "Check consistency across files"
    - generate_report: "Create context_validation_report.json"
```

### Input Data Validation ✅
```yaml
candidate_data_validation:
  source_directory: "data/public/hiring/candidates/individual/{date}/"
  validation_steps:
    - discover_files: "Use listDirectory to find all candidate files"
    - load_candidates: "Use readMultipleFiles to load all data"
    - validate_structure: "Check JSON schema compliance"
    - check_completeness: "Verify required fields present"
    - assess_quality: "Generate data quality metrics"
    
  required_fields:
    - candidate_id: "Unique identifier"
    - name_en: "English name"
    - translated_summary: "Professional summary"
    - contacts: "Email and phone information"
    - entities: "Skills, experience, projects"
    - core_values: "Value alignment evidence"
    
  quality_thresholds:
    - completeness: ">= 80% of required fields"
    - contact_info: "Email or phone present (production mode)"
    - experience_data: "Work history or projects present"
    - skills_data: "Technical skills identified"
```

### Environment Setup Validation ✅
```yaml
environment_validation:
  working_directory:
    base_path: "data/public/hiring/working/"
    run_directory: "{run_id}/"
    required_subdirs:
      - "candidates/"
      - "reports/"
      - "logs/"
      
  output_directories:
    evaluation_sheets: "artifacts/public/hiring/evaluation_sheets/upcoming/"
    takehome_assignments: "artifacts/public/hiring/takehome_assignment/upcoming/"
    interview_materials: "artifacts/public/hiring/interview_materials/upcoming/"
    
  mcp_servers:
    required:
      - name: "sequential-thinking"
        test_command: "Simple reasoning task"
        fallback: "None - critical for workflow"
      - name: "fetch"
        test_command: "URL retrieval test"
        fallback: "Manual file operations"
    optional:
      - name: "exa"
        test_command: "Search query test"
        fallback: "Skip research features"
```

## Stage-Specific Validation Rules

### Stage 1: Context Verification
```yaml
validation_rules:
  input_validation:
    - context_files_loaded: "All required files accessible"
    - format_validation: "YAML/Markdown parsing successful"
    - content_completeness: "All required sections present"
    
  output_validation:
    - validation_report: "context_validation_report.json created"
    - completeness_score: ">= 90% context completeness"
    - error_documentation: "All issues documented with solutions"
    
  error_conditions:
    - missing_files: "Stop execution, request specific files"
    - format_errors: "Stop execution, provide format guidance"
    - incomplete_content: "Stop execution, identify missing sections"
```

### Stage 2: Intake & Normalization
```yaml
validation_rules:
  input_validation:
    - candidate_files_discovered: "All files in source directory found"
    - data_loading_successful: "All JSON files parsed correctly"
    - required_fields_present: "Core candidate data available"
    
  processing_validation:
    - id_generation: "Unique candidate IDs created (atlas_001, nova_002, etc.)"
    - data_normalization: "Standard schema compliance achieved"
    - contact_preservation: "Contact info preserved (production mode)"
    
  output_validation:
    - normalized_file: "candidates.normalized.json created"
    - data_quality_report: "Quality metrics documented"
    - completeness_threshold: ">= 80% data completeness per candidate"
    
  error_conditions:
    - file_read_errors: "Log errors, continue with available data"
    - data_format_issues: "Attempt correction, flag for review"
    - id_collisions: "Regenerate IDs, ensure uniqueness"
```

### Stage 3: JD Mapping
```yaml
validation_rules:
  input_validation:
    - job_description_loaded: "JD file accessible and parsed"
    - candidate_data_available: "Normalized candidate data loaded"
    - requirements_extracted: "Job requirements identified"
    
  processing_validation:
    - skills_mapping: "Technical skills aligned with requirements"
    - experience_analysis: "Experience level assessed accurately"
    - gap_identification: "Skill gaps identified with specificity"
    
  output_validation:
    - mapping_files: "Individual jd_mapping_{candidate_id}.json created"
    - confidence_scores: ">= 75% mapping confidence"
    - actionable_gaps: "Specific training recommendations provided"
    
  error_conditions:
    - jd_parsing_errors: "Request clarification, use fallback analysis"
    - low_confidence: "Generate additional analysis, flag for review"
    - mapping_failures: "Use partial analysis, document limitations"
```

### Stage 4: Automated Screening
```yaml
validation_rules:
  input_validation:
    - screening_plan_loaded: "Screening methodology accessible"
    - candidate_mappings: "JD mapping results available"
    - evaluation_criteria: "Scoring rubrics defined"
    
  processing_validation:
    - multi_dimensional_analysis: "All scoring dimensions evaluated"
    - evidence_collection: "Specific examples provided for scores"
    - bias_checking: "Language and recommendations reviewed"
    
  output_validation:
    - screening_reports: "Individual reports for all candidates"
    - quality_scores: ">= 8.5/10 report quality"
    - decision_alignment: "Recommendations match scoring"
    - summary_statistics: "Aggregate results documented"
    
  quality_gates:
    - evidence_requirement: "All scores supported by specific examples"
    - bias_detection: "Neutral language, no demographic references"
    - consistency_check: "Similar candidates scored consistently"
    
  error_conditions:
    - low_quality_scores: "Regenerate with enhanced prompts (max 3 attempts)"
    - bias_detection: "Revise language, ensure neutrality"
    - scoring_inconsistencies: "Review evidence, adjust scores"
```

### Stage 5: Take-Home Assignment
```yaml
validation_rules:
  input_validation:
    - candidate_filtering: "Qualified candidates identified (>= 8.0 score)"
    - screening_reports: "Detailed candidate analysis available"
    - assignment_templates: "Appropriate templates accessible"
    
  processing_validation:
    - template_selection: "Appropriate difficulty level chosen"
    - personalization: "Assignment customized to candidate background"
    - evaluation_criteria: "Rubrics aligned with role requirements"
    
  output_validation:
    - assignment_packages: "Complete assignment.md and evaluation_sheet.md"
    - personalization_elements: "Candidate-specific content present"
    - clear_instructions: "Requirements and expectations explicit"
    - realistic_timeline: "Appropriate time allocation (4-6 hours)"
    
  error_conditions:
    - template_selection_errors: "Use default template, flag for review"
    - personalization_failures: "Use standard assignment, note limitations"
    - evaluation_criteria_issues: "Use baseline rubric, enhance manually"
```

### Stage 6: Interview Kit Generation
```yaml
validation_rules:
  input_validation:
    - candidate_data_complete: "All candidate information available"
    - screening_results: "Detailed analysis and recommendations"
    - company_context: "Values and culture information loaded"
    
  processing_validation:
    - context_briefing: "Executive summary with key insights"
    - question_personalization: "Behavioral questions customized"
    - technical_calibration: "Assessments appropriate to level"
    
  output_validation:
    - complete_kit: "All three files generated (context, guide, script)"
    - personalization_quality: "Candidate-specific elements relevant"
    - value_alignment: "Questions tied to company values"
    - technical_appropriateness: "Assessments match role requirements"
    
  error_conditions:
    - content_generation_failures: "Retry with enhanced context"
    - personalization_issues: "Use template questions, add manual notes"
    - quality_threshold_failures: "Regenerate specific sections"
```

## Error Prevention Mechanisms

### Proactive Validation
```yaml
pre_stage_checks:
  dependency_validation:
    - input_files_exist: "All required inputs available"
    - tool_availability: "MCP servers responsive"
    - output_directories: "Target directories writable"
    
  data_integrity_checks:
    - format_validation: "Data structure compliance"
    - completeness_assessment: "Required fields present"
    - consistency_verification: "Cross-reference accuracy"
    
  quality_preparation:
    - context_loading: "All relevant context available"
    - prompt_enhancement: "Examples and guidance included"
    - scoring_criteria: "Clear evaluation standards defined"
```

### Real-Time Monitoring
```yaml
execution_monitoring:
  progress_tracking:
    - stage_completion: "Track progress through workflow"
    - candidate_processing: "Monitor individual candidate status"
    - quality_metrics: "Real-time quality score monitoring"
    
  error_detection:
    - quality_threshold_monitoring: "Alert on scores below 8.5"
    - bias_detection: "Flag potentially biased content"
    - completeness_checking: "Identify missing sections"
    
  performance_metrics:
    - execution_time: "Track stage duration"
    - resource_utilization: "Monitor tool usage"
    - success_rates: "Track completion percentages"
```

### Recovery Procedures
```yaml
error_recovery:
  graceful_degradation:
    - partial_processing: "Continue with available data"
    - fallback_methods: "Alternative approaches when tools fail"
    - quality_warnings: "Document limitations and gaps"
    
  retry_mechanisms:
    - exponential_backoff: "Increasing delays between retries"
    - enhanced_prompts: "Additional context on retry attempts"
    - maximum_attempts: "Limit retries to prevent infinite loops"
    
  escalation_procedures:
    - human_review: "Flag complex issues for manual intervention"
    - checkpoint_saves: "Enable resumption from failure points"
    - detailed_reporting: "Comprehensive error documentation"
```

## Quality Assurance Framework

### Automated Quality Checks
```yaml
content_quality_validation:
  completeness_check:
    - required_sections: "All mandatory sections present"
    - field_population: "No empty required fields"
    - reference_integrity: "All references valid and accessible"
    
  accuracy_validation:
    - evidence_support: "All claims supported by specific examples"
    - consistency_check: "Information consistent across documents"
    - factual_verification: "Claims align with source data"
    
  relevance_assessment:
    - candidate_specificity: "Content tailored to individual candidates"
    - role_alignment: "Materials appropriate for target position"
    - company_alignment: "Content reflects company values and culture"
    
  clarity_evaluation:
    - language_quality: "Professional, clear, and grammatically correct"
    - structure_organization: "Logical flow and clear organization"
    - actionability: "Clear next steps and recommendations"
```

### Bias Detection and Mitigation
```yaml
bias_prevention:
  language_analysis:
    - neutral_tone: "Professional, objective language throughout"
    - demographic_blindness: "No references to protected characteristics"
    - consistent_standards: "Same evaluation criteria for all candidates"
    
  recommendation_consistency:
    - evidence_based: "All recommendations supported by specific evidence"
    - standardized_criteria: "Consistent evaluation framework applied"
    - objective_scoring: "Quantitative metrics where possible"
    
  fairness_validation:
    - equal_opportunity: "All candidates evaluated fairly"
    - accommodation_consideration: "Accessibility and inclusion factors"
    - cultural_sensitivity: "Respectful of diverse backgrounds"
```

## Validation Reporting

### Execution Reports
```json
{
  "validation_report": {
    "run_id": "20250811_143000_enhanced",
    "validation_timestamp": "2025-08-11T14:30:00Z",
    "overall_status": "success|warning|failure",
    "validation_results": {
      "context_engineering": {
        "status": "success",
        "completeness_score": 95,
        "missing_files": [],
        "format_errors": []
      },
      "data_integrity": {
        "status": "success",
        "candidates_processed": 4,
        "data_quality_score": 87,
        "completeness_issues": ["contact_info_missing: nova_002"]
      },
      "stage_validation": {
        "stages_completed": 6,
        "quality_scores": [9.5, 9.0, 8.8, 8.9, 9.1, 9.0],
        "average_quality": 9.05,
        "threshold_violations": []
      }
    },
    "recommendations": [
      "Obtain complete contact information for nova_002",
      "Consider additional technical assessment for orion_003"
    ]
  }
}
```

### Quality Metrics Dashboard
```yaml
quality_metrics:
  execution_efficiency:
    - total_duration: "3.5 hours for 4 candidates"
    - stage_completion_rate: "100%"
    - error_rate: "0%"
    - retry_count: "2 (quality threshold retries)"
    
  content_quality:
    - average_quality_score: "9.05/10"
    - minimum_quality_score: "8.8/10"
    - threshold_compliance: "100%"
    - bias_detection_alerts: "0"
    
  candidate_outcomes:
    - strong_hire_rate: "25% (1/4)"
    - hire_rate: "50% (2/4)"
    - pass_rate: "75% (3/4)"
    - quality_differentiation: "Clear scoring separation"
```

---
**Framework Version**: 1.0  
**Compliance Level**: Mandatory for all AI agent executions  
**Quality Standard**: ≥8.5/10 for all generated content  
**Last Updated**: 2025-08-11T14:15:00Z