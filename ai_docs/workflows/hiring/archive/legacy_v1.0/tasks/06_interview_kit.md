---
id: platform_engineering_interview_kit_generation
type: task
domain: hiring
stage: 6
created_date: 2025-08-11
last_updated: 2025-09-02
author: Kiro
quality_score: 9.8/10
tags: [interview, platform-engineering, ai-orchestration, systems-thinking, competency-assessment, hiring]
visibility: public
version: 3.0
---

# Task 6: Platform Engineering Interview Kit Generation

**Purpose**: Generate comprehensive platform engineering interview materials that systematically assess 4 core competency categories through multi-tier evaluation, ensuring thorough assessment of AI-assisted development capability and platform engineering potential.

## Prerequisites
- **Tasks 1-5 Completed**: All previous stages successful
- **Input**: `data/public/hiring/resume/{candidate_file}.json`
- **Context**: Platform engineering competency framework, AI-assisted development standards, production platform requirements
- **Approval**: Platform Lead approval for platform assessment design

## Platform Engineering Assessment Methodology

### Core Principles
1. **AI Orchestration Capability**: Primary indicator of platform engineering success
2. **Systems Thinking**: Essential for platform architecture and reliability
3. **Multi-Tier Assessment**: Comprehensive evaluation across 4 competency categories
4. **Production Mindset**: Operational excellence and scalability focus
5. **Learning Agility**: Critical for AI-assisted development evolution

### Competency Evidence Categorization
- **ADVANCED**: Clear evidence of high competency (Level 4-5) - minimal assessment needed
- **DEVELOPING**: Some evidence but requires validation (Level 2-3) - focused assessment
- **MISSING**: No evidence found (Level 1-2) - comprehensive assessment required

## Objectives
- **Primary**: Systematically assess 4 platform engineering competency categories through multi-tier evaluation
- Generate personalized interview materials targeting AI orchestration and systems thinking capabilities
- Create competency analysis documents with gap identification across all categories
- Develop multi-tier assessment plans with AI-assisted development simulations
- Produce structured evaluation frameworks for platform engineering potential measurement

## Pre-Generation Analysis Requirements

### Required Inputs
```yaml
required_inputs:
  - candidate_resume_data: "Complete profile from candidates JSON"
  - screening_report: "Platform engineering competency screening analysis"
  - takehome_materials: "AI-assisted platform assessment and work samples"
  - competency_framework: "4-category platform engineering competency model"
  - platform_requirements: "Platform engineering role requirements and expectations"
```

### Competency Evidence Mapping Process
For each of the 4 platform engineering competency categories, analyze and document:

#### 1. AI Orchestration & Collaboration (35% Weight)
- **Evidence Sources**: AI-assisted project work, automation implementations, tool adoption patterns
- **Key Indicators**: Effective use of AI tools, iteration and improvement cycles, critical evaluation of outputs
- **Assessment Focus**: AI instruction capability, output validation skills, assisted iteration effectiveness

#### 2. Systems Thinking & Architecture (30% Weight)
- **Evidence Sources**: Platform projects, system design decisions, integration implementations
- **Key Indicators**: Scalable architecture design, production deployment thinking, cross-system integration
- **Assessment Focus**: Platform architecture capability, production system understanding, integration patterns

#### 3. Critical Thinking & Problem Solving (20% Weight)
- **Evidence Sources**: Complex problem resolution, technical decision-making, incident response
- **Key Indicators**: Systematic problem breakdown, data-driven decisions, risk assessment and mitigation
- **Assessment Focus**: Problem decomposition skills, technical decision quality, risk management capability

#### 4. Continuous Learning & Adaptability (15% Weight)
- **Evidence Sources**: Technology adoption, skill development, adaptation to change
- **Key Indicators**: Rapid learning capability, knowledge synthesis, feedback integration
- **Assessment Focus**: Learning velocity, adaptability to new tools, continuous improvement mindset

## Multi-Tier Assessment Framework

### Assessment Structure Template
- **Tier 1**: AI-Assisted Development Simulation (45 minutes)
- **Tier 2**: System Architecture Design Challenge (60 minutes)
- **Tier 3**: Production Platform Scenarios (30 minutes)
- **Tier 4**: Learning & Adaptation Assessment (15 minutes)

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

### 1. Candidate Context Briefing (Enhanced v2.0)
**Primary Location**: `artifacts/public/hiring/candidates/{date}_{candidate_id}/interview/candidate_context.md`
**Legacy Location**: `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/candidate_context.md`

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

### 2. Interview Guide (BEI-Enhanced v2.0)
**Primary Location**: `artifacts/public/hiring/candidates/{date}_{candidate_id}/interview/interview_guide.md`
**Legacy Location**: `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_guide.md`

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

### 3. Interview Script (BEI-Enhanced v2.0)
**Primary Location**: `artifacts/public/hiring/candidates/{date}_{candidate_id}/interview/interview_script.md`
**Legacy Location**: `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_script.md`

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

### Directory Layout (Enhanced v2.0)
```
artifacts/public/hiring/candidates/
├── 20250811_atlas_001_atlas-cand/
│   ├── interview/
│   │   ├── candidate_context.md    # PROVEN/SUGGESTED/MISSING gap analysis
│   │   ├── interview_guide.md      # BEI (40min) + Pair Programming (45min) separation
│   │   └── interview_script.md     # General behavioral STAR questions
│   ├── pair_programming_task.md    # Custom gap-targeted technical challenge
│   └── pair_programming/           # Complete working skeleton project
├── 20250811_nova_002_nova-cand/
│   ├── interview/
│   ├── pair_programming_task.md
│   └── pair_programming/
└── ...

# Legacy Structure (Deprecated)
artifacts/public/hiring/interview_materials/upcoming/
├── atlas_001_atlas-cand/          # v1.0 format maintained for backward compatibility
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

### Enhanced v3.0 Platform Engineering Single Candidate
```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt_v3_platform_engineering.md" \
  --context "data/public/hiring/resume/{candidate_file}.json"
```

### Legacy v1.0 Single Candidate (Deprecated)
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/06_interview_kit.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --context "context/company_info/mission_vision_values.yaml" \
  --filter "candidate_id=atlas_001" \
  --mode "bei_comprehensive"
```

### Enhanced v2.0 All Eligible Candidates
```bash
# Process multiple candidates with v2.0 enhancement
for candidate in data/public/hiring/resume/*.json; do
  gemini run \
    --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt_v2.md" \
    --context "$candidate"
done
```

### Legacy v1.0 With Screening Integration (Deprecated)
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