---
id: bei_interview_kit_generation
type: task
domain: hiring
stage: 6
created_date: 2025-08-11
last_updated: 2025-08-11
author: Kiro
quality_score: 9.8/10
tags: [interview, BEI, behavioral-assessment, core-values, hiring, personalization]
visibility: public
version: 2.0
---

# Task 6: BEI-Focused Interview Kit Generation

**Purpose**: Generate comprehensive Behavioral Event Interview (BEI) materials that systematically assess all 10 company core values through past behavioral pattern analysis, ensuring thorough evaluation of candidate-value alignment while maintaining personalized interview experience.

## Prerequisites
- **Tasks 1-5 Completed**: All previous stages successful
- **Input**: `data/private/hiring/working/{run_id}/candidates.normalized.json`
- **Context**: Company values, job requirements, candidate profiles, screening reports, take-home evaluations
- **Approval**: Platform Lead approval for take-home evaluations

## BEI Methodology Overview

### Core Principles
1. **Past Behavior Predicts Future Performance**: Focus on specific past experiences, not hypothetical scenarios
2. **STAR Format Structure**: Every question follows Situation-Task-Action-Results framework
3. **Evidence-Based Assessment**: Map concrete evidence from candidate materials to core values
4. **Gap Analysis**: Distinguish between values that need verification vs. discovery
5. **Pattern Recognition**: Multiple questions per value to confirm behavioral consistency

### Value Evidence Categorization
- **PROVEN**: Strong, clear evidence from resume/materials (verify authenticity)
- **SUGGESTED**: Weak or indirect evidence (probe deeper for confirmation)
- **MISSING**: No evidence found (comprehensive discovery needed)

## Objectives
- **Primary**: Systematically assess all 10 core values through BEI methodology
- Generate personalized interview materials for each eligible candidate
- Create executive briefings with comprehensive BEI value gap analysis
- Develop detailed interview guides with value-by-value BEI questions
- Produce verbatim scripts with STAR format questions and follow-ups

## Pre-Generation Analysis Requirements

### Required Inputs
```yaml
required_inputs:
  - candidate_resume_data: "Complete profile from candidates JSON"
  - screening_report: "Detailed screening analysis and scores"
  - takehome_materials: "Assignment and any provided work samples"
  - job_description: "Role requirements and competency expectations"
  - company_values: "10 core values with behavioral indicators"
```

### Value Evidence Mapping Process
For each of the 10 core values, analyze and document:

#### 1. Technical Excellence & Scalable Elegance
- **Evidence Sources**: Technical projects, architecture decisions, code quality practices
- **Key Indicators**: System design, performance optimization, maintainability focus
- **Red Flags**: Shortcuts without consideration for scale, poor architectural decisions

#### 2. Customer-Centric Craftsmanship
- **Evidence Sources**: User-focused projects, usability considerations, stakeholder engagement
- **Key Indicators**: User research, feedback incorporation, end-user problem solving
- **Red Flags**: Technology-first thinking, no user validation, internal-only focus

#### 3. Ownership & Proactivity
- **Evidence Sources**: Leadership examples, initiative-taking, problem resolution
- **Key Indicators**: Going beyond assigned tasks, taking responsibility for outcomes
- **Red Flags**: Blame-shifting, waiting for direction, avoiding difficult decisions

#### 4. Observability & Guardrails
- **Evidence Sources**: Monitoring implementation, testing practices, operational excellence
- **Key Indicators**: Metrics-driven development, proactive monitoring, incident response
- **Red Flags**: No testing strategy, reactive-only approach, blind deployment

#### 5. Data-Informed Iteration
- **Evidence Sources**: A/B testing, metrics analysis, decision-making processes
- **Key Indicators**: Evidence-based decisions, measurement focus, iterative improvement
- **Red Flags**: Gut-feeling decisions, no measurement, resistance to data

#### 6. Integrity & Reliability
- **Evidence Sources**: Ethical decision-making, reliability in commitments, quality focus
- **Key Indicators**: Honesty in difficult situations, consistent delivery, quality focus
- **Red Flags**: Cutting corners, unreliable commitments, ethical compromises

#### 7. Security & Compliance First
- **Evidence Sources**: Security practices, compliance awareness, risk management
- **Key Indicators**: Security-by-design thinking, compliance integration, risk awareness
- **Red Flags**: Security afterthought, compliance ignorance, unnecessary risk-taking

#### 8. Collaboration & Knowledge-Sharing
- **Evidence Sources**: Team projects, mentoring, documentation, knowledge transfer
- **Key Indicators**: Effective teamwork, teaching others, accessible documentation
- **Red Flags**: Hoarding knowledge, poor communication, team conflict

#### 9. Continuous Learning & Mentorship
- **Evidence Sources**: Skill development, teaching others, staying current
- **Key Indicators**: Learning new technologies, helping teammates grow, industry engagement
- **Red Flags**: Stagnant skills, reluctance to teach, outdated practices

#### 10. Innovative Spirit
- **Evidence Sources**: Creative problem-solving, new approaches, experimentation
- **Key Indicators**: Novel solutions, willingness to try new approaches, creative thinking
- **Red Flags**: Always status-quo, fear of new approaches, no creative solutions

## BEI Question Framework

### STAR Question Structure Template
```
"Tell me about a specific time when you [behavioral indicator]. 
- What was the SITUATION you were in?
- What was your specific TASK or challenge?
- What ACTIONS did you personally take?
- What were the RESULTS, and what did you learn?"
```

### Sample STAR Questions by Value

#### Technical Excellence & Scalable Elegance
**Verification Question** (when evidence exists):
"I see from your resume you worked on [specific project]. Tell me about a time when you had to make a technical decision that would impact the system's ability to scale. What was the situation, what options did you consider, what actions did you take, and what were the results?"

**Discovery Question** (when evidence missing):
"Describe a specific situation where you had to choose between a quick solution and a more elegant, scalable approach. Walk me through your thought process, the decision you made, and the outcome."

#### Ownership & Proactivity
**Verification Question**:
"You mentioned leading [specific initiative]. Tell me about a time when you took ownership of a problem that wasn't specifically assigned to you. What drove you to take action, what did you do, and what happened as a result?"

**Discovery Question**:
"Give me an example of when you saw something going wrong in a project or system, even though it wasn't technically your responsibility. How did you handle it?"

## Generated Materials

### 1. Candidate Context Briefing (Enhanced)
**File**: `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/candidate_context.md`

**Contents**:
- Executive summary of candidate profile
- **BEI Value Gap Analysis** (NEW):
  - Values with PROVEN Evidence: [Specific evidence] → **VERIFICATION NEEDED**
  - Values with SUGGESTED Evidence: [Weak evidence] → **DEEP PROBE REQUIRED**
  - Values with MISSING Evidence: No evidence → **COMPREHENSIVE DISCOVERY NEEDED**
- **BEI Interview Strategy** (NEW):
  - Primary Focus: [3-4 values needing most attention]
  - Verification Focus: [Values with evidence requiring validation]
  - Discovery Focus: [Values with no evidence]
- Technical competency overview
- Potential areas of concern or exploration
- Recommended interview focus areas with time allocation

### 2. Interview Guide (BEI-Enhanced)
**File**: `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_guide.md`

**Structure**:
```markdown
# BEI Interview Guide: [Candidate Name]

## Value Assessment Priority
1. **HIGH PRIORITY** (20 minutes): [List values]
2. **MEDIUM PRIORITY** (25 minutes): [List values]  
3. **STANDARD PRIORITY** (15 minutes): [List values]

## Value-by-Value BEI Questions
### [Value Name] - [PROVEN/SUGGESTED/MISSING]
**Focus**: [Verification/Discovery/Deep Probe]
**Time Allocation**: [X minutes]
**Primary Question**: [STAR format question]
**Follow-up Probes**: 
- [Specific follow-up 1]
- [Specific follow-up 2]
**What to Listen For**: [Specific behavioral indicators]
**Red Flags**: [Warning signs to note]

[Repeat for all values]

## Technical Assessment Questions
[Role-appropriate technical questions based on candidate background]

## System Design Scenarios (if applicable)
[Scalability and architecture discussions]
```

### 3. Interview Script (BEI-Enhanced)
**File**: `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_script.md`

**Contents**:
- Verbatim opening and BEI methodology explanation
- **Value introduction explanations**
- **Exact STAR format question phrasing**
- **Follow-up probe questions for incomplete responses**
- **Transition statements between values**
- **Clarification questions for incomplete STAR responses**
- Time management cues with BEI focus
- Note-taking templates for behavioral pattern tracking

## Interview Structure Requirements

### Time Allocation (120 minutes total)
```yaml
opening_introduction: 10 minutes
bei_core_values_assessment: 60 minutes  # 6 minutes per value average
technical_deep_dive: 30 minutes
cultural_fit_discussion: 15 minutes
candidate_questions_closing: 15 minutes
```

### BEI Assessment Priority Matrix
```yaml
high_priority_values: [1,3,6,9]  # Technical Excellence, Ownership, Integrity, Learning
medium_priority_values: [2,4,5,8]  # Customer-Centric, Observability, Data-Informed, Collaboration  
standard_priority_values: [7,10]  # Security, Innovation
```

## Processing Steps

### 1. BEI Context Assembly (Enhanced)
- Load normalized candidate data
- Retrieve screening reports and take-home evaluations
- Parse all candidate materials (resume, portfolio, work samples)
- Load company values with behavioral indicators
- Parse job description requirements

### 2. Comprehensive Value Evidence Mapping (NEW)
- Systematically analyze candidate materials for each of the 10 values
- Categorize evidence as PROVEN/SUGGESTED/MISSING
- Document specific examples and behavioral indicators found
- Identify evidence gaps requiring exploration
- Generate targeted questioning strategy

### 3. BEI Question Generation (NEW)
- Create STAR format questions for each value based on evidence analysis
- Generate verification questions for PROVEN values
- Generate discovery questions for MISSING values
- Develop follow-up probes for incomplete responses
- Plan behavioral pattern recognition strategy

### 4. Technical Assessment Planning
- Analyze candidate's technical background
- Select appropriate technical questions
- Design system design scenarios
- Plan pair programming exercises (if applicable)

### 5. Personalization Engine
- Customize BEI questions based on candidate experience
- Adapt difficulty level to candidate seniority
- Include industry-specific scenarios
- Reference candidate's portfolio/projects in STAR questions

### 6. Quality Assurance (Enhanced)
- Validate STAR question clarity and behavioral focus
- Ensure all 10 values covered with adequate time allocation
- Check for bias-free language
- Verify behavioral pattern recognition guidance
- Confirm evidence-based questioning approach

## Output Structure

### Directory Layout
```
artifacts/public/hiring/interview_materials/upcoming/
├── atlas_001_atlas-cand/
│   ├── candidate_context.md    # Includes BEI Value Gap Analysis
│   ├── interview_guide.md      # Value-by-value BEI structure
│   └── interview_script.md     # Verbatim STAR questions
├── nova_002_nova-cand/
│   ├── candidate_context.md
│   ├── interview_guide.md
│   └── interview_script.md
└── ...
```

## Quality Validation Checklist

### BEI-Specific Requirements
- [ ] All 10 values mapped with evidence categorization
- [ ] STAR format questions for each value requiring assessment
- [ ] Verification questions for PROVEN values from materials
- [ ] Discovery questions for MISSING values needing exploration
- [ ] 60+ minutes allocated specifically for BEI assessment
- [ ] Clear behavioral pattern recognition guidance for interviewers
- [ ] Follow-up probes prepared for incomplete responses
- [ ] Red flag indicators documented for each value
- [ ] Transition scripts between interview sections
- [ ] Value assessment priority matrix applied

### Standard Requirements
- [ ] All three files generated per candidate
- [ ] Candidate-specific personalization present
- [ ] Technical assessment appropriate for role level
- [ ] Bias-free language throughout
- [ ] Quality score ≥8.5/10
- [ ] Platform Lead approval obtained

## Success Metrics

### BEI Coverage Metrics
- **Coverage**: All 10 values assessed with at least one comprehensive STAR question
- **Depth**: Multiple behavioral examples gathered per high-priority value
- **Validation**: Evidence from materials verified through specific questioning
- **Discovery**: Missing values explored through comprehensive behavioral probing
- **Consistency**: Behavioral patterns confirmed across multiple questions

### Standard Metrics
- **Generation Success Rate**: ≥95% successful kit generation
- **Quality Score**: ≥8.5/10 average across all materials
- **Interviewer Satisfaction**: ≥90% positive feedback
- **Time Efficiency**: <60 minutes per candidate kit (extended for BEI analysis)

## Error Handling
- **Missing Context**: Request additional candidate information
- **Incomplete Value Mapping**: Flag for manual analysis
- **Quality Failures**: Regenerate with enhanced BEI prompts
- **Approval Delays**: Queue for expedited review
- **Template Issues**: Fall back to standard BEI templates

## Next Stage
Upon successful completion and approval, proceed to **Task 7: Structured Interview Loop** with BEI-trained interviewers

## MCP Integration
- **sequential-thinking**: Plan BEI structure and value assessment flow
- **exa**: Research candidate background and company behavioral examples
- **fetch**: Retrieve additional context materials and value frameworks

## Execution Commands

### Single Candidate with BEI Focus
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/06_interview_kit.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --context "context/company_info/mission_vision_values.yaml" \
  --filter "candidate_id=atlas_001" \
  --mode "bei_comprehensive"
```

### All Eligible Candidates
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/06_interview_kit.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --context "context/company_info/mission_vision_values.yaml" \
  --mode "bei_batch"
```

### With Screening Results Integration
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/06_interview_kit.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --context "data/private/hiring/working/{run_id}/screening_summary_complete.json" \
  --context "context/company_info/mission_vision_values.yaml"
```

---
**Version**: 2.0 - BEI Methodology Integration  
**Last Updated**: 2025-08-11  
**Compliance**: Aligned with Power of Process BEI requirements