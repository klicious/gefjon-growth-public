---
id: hybrid_hiring_workflow_orchestrator
type: orchestrator
domain: hiring
created_date: 2025-08-11
last_updated: 2025-09-02
author: Kiro
quality_score: 9.7/10
tags: [workflow, hiring, orchestrator, automation, ai-agent-ready, hybrid-assessment, bei-methodology]
visibility: public
version: 2.1
---

# Hybrid Hiring Workflow Orchestrator
## BEI Core Values + Enhanced Technical Assessment

**Purpose**: AI-agent-ready end-to-end hiring workflow automation implementing **Hybrid BEI + Enhanced Technical Assessment** methodology. Preserves traditional BEI core values assessment (60% weight) while adding enhanced technical evaluation for AI-assisted development and platform engineering (40% weight).

## AI Agent Execution Instructions

### Critical Pre-Execution Checklist
Before starting ANY stage, AI agents MUST:
1. ✅ **Verify Context Engineering Compliance**: Load and validate ALL required context files
2. ✅ **Check Prerequisites**: Ensure all inputs and dependencies are available
3. ✅ **Validate Data Integrity**: Confirm data formats and completeness
4. ✅ **Create Run Directory**: Establish working directory with unique run_id
5. ✅ **Initialize Tracking**: Create execution log and status tracking

### Execution Mode Detection
AI agents must determine execution context:
- **Production Mode**: Real hiring process with full contact information
- **Demo Mode**: Presentation/testing with PII masking
- **Debug Mode**: Individual stage testing and validation

## Enhanced Prerequisites

### Required Inputs (MANDATORY VALIDATION)
```yaml
inputs:
  candidates_source:
    path: "data/public/hiring/resume/{date}/candidates_{date}.json"
    format: "Single JSON file with array of candidate objects"
    validation: "Must contain at least 1 candidate in array"
    
  job_description:
    path: "data/private/hiring/job_description_kr.md"
    validation: "Must exist and contain role requirements"
    
  evaluator_github:
    value: "klicious"  # Default evaluator
    validation: "Must be valid GitHub username"
    
  run_configuration:
    processing_mode: "production|demo|debug"
    quality_threshold: 8.5
    approval_required: true
```

### Required Context Files (AUTO-VALIDATION)
```yaml
context_files:
  company_values:
    path: "context/company_info/mission_vision_values.yaml"
    required: true
    validation: "Must contain core values definition"
    
  hiring_stages:
    path: "context/hr_processes/hiring/hiring_stages.yaml"
    required: true
    validation: "Must contain stage definitions and criteria"
    
  platform_team:
    path: "data/private/platform_development_team.md"
    required: true
    validation: "Must contain team context and requirements"
```

### MCP Server Requirements (AUTO-CHECK)
```yaml
mcp_servers:
  required:
    - name: "sequential-thinking"
      purpose: "Stage planning and decomposition"
      validation: "Must be available for complex reasoning"
    - name: "fetch"
      purpose: "Asset retrieval and validation"
      validation: "Must be available for context loading"
  optional:
    - name: "exa"
      purpose: "Company/candidate research"
      fallback: "Skip research-dependent features"
    - name: "playwright"
      purpose: "Portfolio validation"
      fallback: "Manual portfolio review"
```

## Enhanced Execution Workflow

### Stage 0: Pre-Flight Validation (NEW)
**Duration**: 5-10 minutes  
**Purpose**: Comprehensive validation before workflow execution

#### Validation Steps
1. **Context Engineering Compliance**
   ```bash
   # Validate all required context files exist
   - Check context/company_info/mission_vision_values.yaml
   - Check context/hr_processes/hiring/hiring_stages.yaml
   - Check data/private/platform_development_team.md
   - Validate file formats and required sections
   ```

2. **Input Data Validation**
   ```bash
   # Validate candidate data structure
   - Check candidate files exist in source directory
   - Validate JSON schema compliance
   - Verify required fields present
   - Check for data completeness
   ```

3. **Environment Setup**
   ```bash
   # Create working directory structure (private for debugging/logs)
   mkdir -p data/private/hiring/working/{run_id}/
   mkdir -p artifacts/public/hiring/evaluation_sheets/upcoming/
   mkdir -p artifacts/public/hiring/takehome_assignment/upcoming/
   mkdir -p artifacts/public/hiring/interview_materials/upcoming/
   ```

4. **Execution Log Initialization**
   ```json
   {
     "run_id": "{timestamp}_hiring_run",
     "started_at": "{iso_timestamp}",
     "processing_mode": "production|demo|debug",
     "candidates_count": 0,
     "stages_completed": [],
     "current_stage": "00_preflight_validation",
     "quality_scores": {},
     "errors": [],
     "warnings": []
   }
   ```

**Output**: `run_config.json` with validation results and execution parameters

### Stage 1: Context Load & Verification (ENHANCED)
**Task**: `ai_docs/workflows/hiring/tasks/01_context_verification.md`  
**Duration**: 10-15 minutes  
**Enhanced Features**:
- Automatic context file discovery and loading
- Schema validation with detailed error reporting
- Missing context identification and resolution guidance
- Context completeness scoring

#### AI Agent Instructions
```markdown
1. Load ALL context files using readMultipleFiles tool
2. Validate each file against expected schema
3. Generate context completeness report
4. If ANY context is missing or invalid, STOP execution and provide specific guidance
5. Create context_validation_report.json with results
```

**Guardrails**:
- ❌ **STOP if context completeness < 90%**
- ❌ **STOP if any REQUIRED context file missing**
- ❌ **STOP if schema validation fails**

### Stage 2: Intake & Normalization (ENHANCED)
**Task**: `ai_docs/workflows/hiring/tasks/02_intake_normalization.md`  
**Duration**: 20-30 minutes  
**Enhanced Features**:
- Load single consolidated JSON file with candidate array
- Transform candidate IDs from original format to codename system
- Data quality assessment and reporting
- Missing information identification
- Candidate ID collision detection

#### AI Agent Instructions
```markdown
1. Load single consolidated JSON file from candidates_source path
2. Parse candidate array and validate data structure
3. Transform candidate IDs: original → codename_ID_name format (e.g., "kim_atlas-cand" → "atlas_001_atlas-cand")
4. Generate unique candidate codenames with collision checking
5. Create normalized dataset with quality metrics and transformed IDs
6. Generate data_quality_report.json with transformation log
```

**Quality Gates**:
- ✅ Consolidated JSON file successfully loaded
- ✅ All candidates parsed from array format
- ✅ Data completeness ≥ 80% per candidate
- ✅ No candidate ID collisions after transformation
- ✅ Codename assignment successful for all candidates
- ✅ Contact information preserved (production mode)

### Stage 3: JD Mapping & Competency Alignment (ENHANCED)
**Task**: `ai_docs/workflows/hiring/tasks/03_jd_mapping.md`  
**Duration**: 30-45 minutes  
**Enhanced Features**:
- Automatic job description parsing
- Skills gap analysis with severity scoring
- Experience level matching validation
- Competency alignment confidence scoring

#### AI Agent Instructions
```markdown
1. Load job description using readFile
2. Parse requirements and create structured competency matrix
3. For each candidate, perform detailed skills mapping
4. Generate experience level assessment
5. Create competency gap analysis with training recommendations
6. Output individual mapping files with confidence scores
```

**Quality Gates**:
- ✅ JD mapping completed for all candidates
- ✅ Skills analysis confidence ≥ 75%
- ✅ Experience level classification accurate
- ✅ Gap analysis actionable and specific

### Stage 4: Automated Screening (ENHANCED)
**Task**: `ai_docs/workflows/hiring/tasks/04_screening.md`  
**Duration**: 45-60 minutes  
**Enhanced Features**:
- Multi-dimensional scoring with evidence validation
- Bias detection and mitigation
- Screening confidence assessment
- Automated quality scoring

#### AI Agent Instructions
```markdown
1. Load screening plan using readFile
2. Apply multi-dimensional analysis framework
3. Generate evidence-based scoring for each dimension
4. Perform bias check on language and recommendations
5. Create detailed screening reports with quality scores
6. Generate screening_summary.json with statistics
```

**Quality Gates**:
- ✅ Screening reports quality score ≥ 8.5/10
- ✅ Evidence provided for all assessments
- ✅ Bias check passed (neutral language)
- ✅ Recommendations align with scoring

**Decision Thresholds**:
- **Strong Hire**: ≥ 9.0/10 → Proceed to take-home
- **Hire**: ≥ 8.0/10 → Proceed to take-home
- **Lean Hire**: ≥ 6.5/10 → Additional assessment required
- **No Hire**: < 6.5/10 → Decline with feedback

### Stage 5: Take-Home Assignment (ENHANCED)
**Task**: `ai_docs/workflows/hiring/tasks/05_takehome_assignment.md`  
**Duration**: 30-45 minutes  
**Enhanced Features**:
- Automatic candidate filtering based on screening results
- Personalization engine with candidate background analysis
- Assignment difficulty calibration
- Evaluation criteria customization
- **CONDITIONAL GENERATION**: Only for qualified candidates

#### AI Agent Instructions
```markdown
1. Filter candidates based on screening results:
   - "Strong Hire" (≥9.0) → Advanced take-home assignment
   - "Hire" (≥8.0) → Standard take-home assignment
   - "Lean Hire" (6.5-7.9) → Skip take-home, additional assessment
   - "No Hire" (<6.5) → Skip take-home, decline process
2. For qualified candidates only:
   - Load candidate profiles and screening reports
   - Select appropriate assignment template based on experience level
   - Personalize assignment content using candidate background
   - Generate customized evaluation sheets with rubrics
   - Create assignment packages with clear instructions
3. Generate assignment distribution summary with candidate filtering rationale
```

**Personalization Factors**:
- Technical background and expertise areas
- Experience level and project complexity
- Identified strengths and growth areas
- Company value alignment opportunities

### Stage 5.5: Take-Home Assignment Evaluation (NEW)
**Task**: `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md`  
**Duration**: 45-90 minutes  
**Purpose**: Evaluate submitted take-home assignments with comprehensive, verifiable evidence for every score.

#### Enhanced Features
- Mandatory evidence per criterion: file paths, line ranges, and commit SHAs
- Reproducibility: commands and steps to run the project locally
- Security & Compliance checklist enforcement
- Observability review (logging/metrics/timeouts/retries)
- Bias mitigation and language neutrality checks
- Automated eligibility gating for Stage 6

#### AI Agent Instructions
```markdown
0. Agent‑First Protocol (MANDATORY)
   - Use AI agent(s) to perform the evaluation. Python scripts are support-only (clone, scaffold templates, optional aggregate). Heuristic auto-evaluation is disabled by default.

0a. Repository cloning & meta capture (MANDATORY)
   - Clone repo to: data/private/hiring/repositories/{candidate_id}/repo
   - Record default branch and HEAD short SHA in repo_meta.json and META.md
   - Command:
     python scripts/execute_05b_takehome_evaluation.py \
       --candidate-id {candidate_id} \
       --candidate-name "{candidate_name}" \
       --github-url "{github_url}" \
       --batch "{batch}"
   - This scaffolds:
     - artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/agent_evaluation_template.md
     - artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/agent_evaluation.json (stub)
     - artifacts/public/hiring/candidates/{batch}/{candidate_id}/takehome/takehome_evaluation.md (Pending status)

1. Collect inputs
   - Locate candidate repo URL from assignment package or candidate record
   - Identify default branch and recent commit SHA (short)

2. Evidence gathering (by agent)
   - README and setup instructions (reproducibility)
   - Code structure and key modules (architecture)
   - Tests and CI configs (correctness/quality)
   - Error handling and input validation (security/compliance)
   - Logging/metrics/health checks/timeouts (observability)
   - Note specific files and line ranges; capture commit SHA for references

3. Scoring per rubric criterion (1–10, 0.5 granularity)
   - For each criterion, include: Score, Evidence (path:lineStart-lineEnd @ commit), brief commentary
   - Fill agent_evaluation_template.md and/or write agent_evaluation.json conforming to ai_docs/workflows/hiring/schemas/takehome_evaluation.schema.json

4. Artifact generation
   - Preferred: agent writes agent_evaluation.json and then run aggregator:
     python scripts/aggregate_takehome_from_agent.py \
       --candidate-id {candidate_id} \
       --candidate-name "{candidate_name}" \
       --github-url "{github_url}" \
       --batch "{batch}"
   - Aggregator computes totals and renders final takehome_evaluation.md and evaluation_sheet.md

5. Decision & gating
   - Map overall score to decision: Strong Hire ≥9.0, Hire ≥8.0, Lean Hire 6.5–7.9, No Hire <6.5
   - Only candidates with ≥8.0 proceed to Stage 6 by default (or Platform Lead override)

6. Quality and bias checks
   - Ensure neutral language, evidence-backed statements only
   - Complete Security & Compliance and Observability checklists
```

#### Quality Gates
- ✅ Evidence present for EACH rubric criterion (path, lines, commit SHA)
- ✅ Reproducibility steps validated (README or provided commands)
- ✅ Security & Compliance checklist completed
- ✅ Observability items assessed
- ✅ Scores ↔ Decision consistent with thresholds
- ✅ Platform Lead approval recorded for decisions ≥ Hire

#### Outputs
- Completed takehome_evaluation.md per candidate with evidence
- Updated evaluation_sheet.md summaries with final scores
- evaluation_summary.json with per-criterion breakdown and decision

### Stage 6: Hybrid Interview Kit Generation - BEI + Enhanced Technical Assessment
**Task**: `ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md`  
**Duration**: 75-90 minutes (extended for comprehensive hybrid analysis)  
**Hybrid Assessment Features**:
- **BEI Core Values Assessment (60% Weight, 40 minutes)**: Traditional BEI methodology with STAR format for all 10 core values
- **Enhanced Technical Assessment (40% Weight, 50 minutes)**: AI-assisted development evaluation + platform engineering scenarios
- **PROVEN/SUGGESTED/MISSING Framework**: Evidence categorization for systematic value assessment
- **AI Collaboration Evaluation**: Hands-on assessment of AI instruction, validation, and iteration capabilities
- **Platform Engineering Scenarios**: Systems thinking and production mindset evaluation
- **Hybrid Scoring Integration**: 75-point scoring system (50 BEI + 25 technical)
- **CONDITIONAL GENERATION**: Only for interview-eligible candidates (≥6.5/10 screening)

#### AI Agent Instructions - Hybrid Assessment Integration
```markdown
1. Filter candidates for interview eligibility:
   - "Strong Hire" + "Hire" (≥8.0) → Full hybrid interview kit (BEI + technical)
   - "Lean Hire" (6.5-7.9) → Assessment-focused hybrid interview kit
   - "No Hire" (<6.5) → Skip interview materials

2. **HYBRID ASSESSMENT ANALYSIS** - Dual Framework Integration:
   
   **BEI Core Values Assessment (60% Weight)**:
   - Analyze resume, screening report, and take-home materials for core values evidence
   - Map evidence for each of the 10 core values from provided materials
   - Categorize values as: PROVEN (strong evidence), SUGGESTED (weak evidence), MISSING (no evidence)
   - Generate targeted STAR format questions for systematic behavioral assessment
   
   **Enhanced Technical Assessment (40% Weight)**:
   - AI-assisted development capability analysis from take-home and portfolio
   - Platform engineering potential assessment from systems thinking evidence
   - Technical collaboration and learning agility indicators
   - Production mindset and scalability understanding evaluation

3. **Core Values Assessment Strategy (Traditional BEI)**:
   For each of the 10 core values, create STAR format questions:
   - Technical Excellence & Scalable Elegance
   - Customer-Centric Craftsmanship  
   - Ownership & Proactivity
   - Observability & Guardrails
   - Data-Informed Iteration
   - Integrity & Reliability
   - Security & Compliance First
   - Collaboration & Knowledge-Sharing
   - Continuous Learning & Mentorship
   - Innovative Spirit

4. **Enhanced Technical Assessment Strategy**:
   - **AI Collaboration Simulation (25 minutes)**: Hands-on evaluation with AI tools available
   - **Platform Engineering Scenarios (25 minutes)**: Architecture design and production problem-solving
   - Assessment criteria: AI instruction effectiveness, output validation, systems thinking
   
5. **Hybrid Interview Structure Requirements**:
   - 95 minute total interview time
   - **Introduction**: 5 minutes
   - **BEI Core Values Assessment**: 40 minutes (systematic coverage of all 10 values)
   - **AI-Assisted Technical Assessment**: 25 minutes (hands-on AI collaboration)
   - **Platform Engineering Scenarios**: 25 minutes (systems thinking evaluation)
   
6. Generate three required files per eligible candidate:
   - candidate_context.md (executive briefing + hybrid assessment analysis)
   - interview_guide.md (hybrid structure: BEI + enhanced technical)
   - interview_script.md (BEI STAR questions + technical assessment guidance)
```

**Quality Gates**:
- ✅ All three files generated per eligible candidate
- ✅ **Hybrid Assessment Integration** completed for each candidate
- ✅ **BEI Value Gap Analysis** completed (PROVEN/SUGGESTED/MISSING for all 10 values)
- ✅ **STAR format questions** generated for comprehensive core values assessment
- ✅ **Enhanced Technical Assessment** scenarios designed (AI collaboration + platform engineering)
- ✅ **Hybrid scoring framework** applied (60% BEI + 40% technical = 75 points total)
- ✅ **Interview time allocation** structured for 95-minute hybrid assessment
- ✅ **AI-assisted development evaluation** criteria established
- ✅ **Platform engineering scenarios** appropriate for systems thinking assessment
- ✅ Clear interviewer guidance for both behavioral and technical evaluation
- ✅ Conditional generation logic properly applied

### Stage 7: Consolidation & Final Organization (NEW)
**Task**: `scripts/consolidate_hiring_results.py`  
**Duration**: 15-20 minutes  
**Purpose**: Organize all generated materials into single candidate directories

#### AI Agent Instructions
```markdown
1. Create standardized directory structure for each candidate:
   - {candidate_id}_{normalized_name}/
     - screening/screening_report.md
     - takehome/takehome_assignment.md (if applicable)
     - interview/candidate_context.md, interview_guide.md, interview_script.md (if applicable)
     - evaluation/evaluation_framework.md
     - communication/communication_templates.md
     - candidate_summary.md
2. Consolidate all scattered materials into appropriate candidate directories
3. Generate master summaries:
   - HIRING_SUMMARY_COMPLETE.md (executive overview)
   - QUICK_REFERENCE_GUIDE.md (decision support)
   - FINAL_WORKFLOW_SUMMARY.json (metrics and statistics)
4. Create audit trail and completion logs
5. Verify completeness and file consistency
```

**Quality Gates**:
- ✅ All candidates have complete directory structure
- ✅ All generated materials properly organized
- ✅ No duplicate or scattered files
- ✅ Master summary documents generated
- ✅ File consistency verification passed

## Error Handling & Recovery

### Common Error Scenarios
```yaml
context_missing:
  error: "Required context file not found"
  action: "Stop execution, provide specific file path and requirements"
  recovery: "Request user to provide missing context"

data_validation_failure:
  error: "Candidate data format invalid"
  action: "Log specific validation errors, continue with valid candidates"
  recovery: "Generate data quality report with specific issues"

quality_threshold_failure:
  error: "Generated content quality below threshold"
  action: "Regenerate with enhanced prompts, up to 3 attempts"
  recovery: "Escalate to manual review if repeated failures"

mcp_server_unavailable:
  error: "Required MCP server not responding"
  action: "Check server status, attempt reconnection"
  recovery: "Use fallback methods or skip optional features"
```

### Recovery Procedures
1. **Graceful Degradation**: Continue with available data/services
2. **Retry Logic**: Automatic retry with exponential backoff
3. **Fallback Methods**: Alternative approaches when primary methods fail
4. **User Notification**: Clear error messages with resolution steps

## AI Agent Execution Commands

### Complete Hybrid Workflow (Recommended)
```bash
# Execute complete hybrid workflow with BEI + enhanced technical assessment
gemini run \
  --prompt "ai_docs/workflows/hiring/orchestrator.md" \
  --context "data/public/hiring/resume/{date}/candidates_{date}.json" \
  --mode "hybrid_assessment" \
  --evaluator "klicious"

# Alternative: Use integrated hybrid automation script
python scripts/complete_hybrid_workflow.py
```

### Stage-by-Stage Execution (Debug Mode)
```bash
# Pre-flight validation
gemini run \
  --prompt "ai_docs/workflows/hiring/orchestrator.md" \
  --stage "00_preflight_validation"

# Individual stage execution
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/04_screening.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --plan "ai_docs/workflows/hiring/plans/candidate_screening_plan.md"
```

### Resume from Checkpoint
```bash
# Resume from specific stage
gemini run \
  --prompt "ai_docs/workflows/hiring/orchestrator.md" \
  --resume-from "stage_4" \
  --run-id "{existing_run_id}"
```

## Quality Assurance Framework

### Automated Quality Checks
```yaml
content_quality:
  threshold: 8.5
  criteria: [completeness, accuracy, relevance, clarity]
  validation: automated_scoring_system

bias_detection:
  language_analysis: neutral_tone_required
  recommendation_consistency: evidence_based_only
  demographic_blindness: no_identifying_characteristics

completeness_validation:
  required_sections: all_present
  evidence_support: specific_examples_required
  actionable_recommendations: clear_next_steps
```

### Human Approval Gates
```yaml
platform_lead_approval:
  required_stages: [4, 5, 6]  # Screening, Take-home, Interview Kit
  approval_criteria: quality_threshold_met
  escalation_path: engineering_manager

quality_review:
  automated_scoring: continuous
  human_validation: approval_gates_only
  feedback_loop: post_execution_review
```

## Success Metrics & KPIs

### Process Efficiency
- **Total Execution Time**: Target < 6 hours for 13 candidates (demonstrated achievement)
- **Stage Completion Rate**: Target ≥ 95% (achieved 100%)
- **Quality Score Average**: Target ≥ 8.5/10 (first-run average 9.2/10, internal scoring)
- **Error Rate**: Target < 5% (first run: no pipeline errors recorded, internal log)
- **Material Completeness**: Target 100% for eligible candidates

### Candidate Experience
- **Time to Feedback**: Target < 24 hours post-submission
- **Process Transparency**: Clear communication at each stage
- **Quality of Materials**: Professional, personalized, relevant

### Hiring Outcomes
- **Strong Candidate Identification**: Target 25-50% of pipeline (achieved 69.2% hire/strong hire rate)
- **Candidate Distribution (Demonstrated)**:
  - Strong Hire: 2 candidates (15.4%)
  - Hire: 7 candidates (53.8%)
  - Lean Hire: 3 candidates (23.1%)
  - No Hire: 1 candidate (7.7%)
- **Material Generation Success**:
  - Take-home assignments: 9/13 candidates (69.2%)
  - Interview materials: 12/13 candidates (92.3%)
  - Complete evaluation frameworks: 13/13 candidates (100%)
- **Interview-to-Offer Conversion**: Target ≥ 60%
- **New Hire Success Rate**: Target ≥ 90% (6-month retention)

## Troubleshooting Guide

### Common Issues & Solutions
```markdown
Issue: "Context files not found"
Solution: Verify file paths, check context engineering compliance

Issue: "Candidate data incomplete"
Solution: Review data quality report, request additional information

Issue: "Quality scores below threshold"
Solution: Review prompts, enhance context, regenerate content

Issue: "MCP server timeout"
Solution: Check server status, use fallback methods, retry operation

Issue: "Approval delays"
Solution: Prepare comprehensive materials, schedule review sessions
```

### Debug Mode Features
- **Step-by-step execution** with pause points
- **Detailed logging** of all operations
- **Intermediate file inspection** capabilities
- **Quality score breakdown** analysis
- **Error reproduction** and testing

## Version Control & Audit Trail

### Execution Logging
```json
{
  "run_id": "20250811_143000_enhanced",
  "workflow_version": "2.0",
  "execution_log": [
    {
      "stage": "00_preflight_validation",
      "started_at": "2025-08-11T14:30:00Z",
      "completed_at": "2025-08-11T14:35:00Z",
      "status": "success",
      "quality_score": 9.5,
      "outputs": ["run_config.json", "context_validation_report.json"]
    }
  ],
  "quality_metrics": {
    "average_score": 9.2,
    "completion_rate": 100,
    "error_count": 0
  }
}
```

### Artifact Versioning
- **Timestamp-based versioning** for all generated content
- **Quality score tracking** across versions
- **Change log maintenance** for iterative improvements
- **Rollback capabilities** for error recovery

---
**Hybrid Orchestrator Version**: 2.1  
**Assessment Framework**: BEI Core Values (60%) + Enhanced Technical Assessment (40%)  
**AI Agent Compatibility**: Optimized for autonomous hybrid assessment execution  
**Quality Assurance**: Comprehensive validation and error handling for dual methodology  
**Phoenix_005 Resolution**: Candidates with AI collaboration skills now properly assessed  
**Last Updated**: 2025-09-02T08:00:00Z

### Agent Prompt Reference & Code-First Policy (Stage 5.5)
- Prompt to use: ai_docs/prompts/hiring/takehome_evaluation_prompt.md
- Code-First Evidence Policy:
  - Primary evidence MUST come from code/tests; README mainly for Documentation & DX and reproducibility.
  - Forbidden as sole evidence for engineering criteria: README excerpts, package manager/tool choice alone (e.g., uv/poetry/Gradle), architecture docs without code references.
  - Penalty caps if only non-code evidence is present:
    - Code Quality, Functional Correctness, Testing, Ownership: max 2/5
    - Scalability & Design Patterns: max 2.5/5
    - Quantitative & Logical Problem Solving: max 2/5
- Every score must include at least one code reference in the format: path:lineStart-lineEnd @ commitShort — note.
