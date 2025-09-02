---
id: hybrid_interview_kit_generation
type: task
domain: hiring
stage: 6
created_date: 2025-09-02
last_updated: 2025-09-02
author: Kiro
quality_score: 9.8/10
tags: [interview, hybrid-assessment, bei-methodology, ai-assisted-development, platform-engineering, hiring]
visibility: public
version: 2.1
---

# Task 6: Hybrid Interview Kit Generation
## BEI Core Values + Enhanced Technical Assessment

**Purpose**: Generate comprehensive hybrid interview materials implementing **60% BEI Core Values Assessment + 40% Enhanced Technical Assessment** methodology. Preserves traditional Behavioral Event Interview approach for all 10 core values while adding AI-assisted development and platform engineering evaluation.

## Prerequisites
- **Tasks 1-5 Completed**: All previous stages successful
- **Input**: `data/public/hiring/resume/{candidate_file}.json`
- **Context**: Hybrid competency framework, BEI methodology, enhanced technical assessment standards
- **Approval**: Platform Lead approval for hybrid assessment design

## Hybrid Assessment Methodology

### Core Principles
1. **BEI Foundation Preserved**: Traditional BEI methodology with STAR format for all 10 core values (60% weight)
2. **Enhanced Technical Assessment**: AI collaboration and platform engineering evaluation (40% weight) 
3. **Evidence-Based Evaluation**: PROVEN/SUGGESTED/MISSING framework for systematic assessment
4. **Cultural Alignment Priority**: Core values assessment remains primary hiring criterion
5. **Phoenix_005 Gap Resolution**: Technical capability properly assessed through AI collaboration

### Assessment Framework Structure
```yaml
hybrid_assessment:
  total_duration: 95_minutes
  total_points: 75_points
  
  bei_core_values_assessment:
    weight: 60%
    duration: 40_minutes
    points: 50_points
    methodology: "Traditional BEI with STAR format questions"
    framework: "PROVEN/SUGGESTED/MISSING evidence categorization"
    
  enhanced_technical_assessment:
    weight: 40% 
    duration: 50_minutes
    points: 25_points
    methodology: "AI-assisted development + platform engineering scenarios"
    components:
      ai_collaboration_simulation: 25_minutes
      platform_engineering_scenarios: 25_minutes
```

## Objectives
- **Primary**: Generate hybrid interview kits preserving BEI methodology while enhancing technical assessment
- **BEI Integration**: Systematic assessment of all 10 core values using PROVEN/SUGGESTED/MISSING framework
- **Technical Enhancement**: AI collaboration evaluation and platform engineering scenarios
- **Quality Assurance**: Evidence-based scoring with minimum thresholds for both components
- **Phoenix_005 Resolution**: Candidates like Phoenix_005 would now pass as LEAN HIRE (69% overall)

## Pre-Generation Analysis Requirements

### Required Inputs
```yaml
required_inputs:
  - candidate_resume_data: "Complete profile from candidates JSON"
  - screening_report: "Core values and technical competency screening analysis"  
  - takehome_materials: "AI-assisted development evidence and work samples"
  - bei_framework: "Traditional BEI methodology with STAR format"
  - hybrid_scoring_framework: "60%/40% weighted scoring system"
```

### BEI Core Values Evidence Mapping Process
For each of the 10 core values, analyze and document:

#### Core Values Assessment (60% Weight, 40 Minutes)
1. **Technical Excellence & Scalable Elegance** - Evidence: Service p95 standards, CodeClimate A rating, horizontal scale design
2. **Customer-Centric Craftsmanship** - Evidence: User story capture, trader pain resolution, usability testing
3. **Ownership & Proactivity** - Evidence: Self-paging during incidents, RCA publishing, responsibility taking
4. **Observability & Guardrails** - Evidence: 3 SLOs + burn-rate alerts, kill-switch implementation
5. **Data-Informed Iteration** - Evidence: A/B testing with +5% KPI improvement, dashboard maintenance
6. **Integrity & Reliability** - Evidence: Immutable audit logs, zero Sev-0 incidents, quality focus
7. **Security & Compliance First** - Evidence: AWS SM secrets rotation, static-analysis gates
8. **Collaboration & Knowledge-Sharing** - Evidence: ≥2 peer reviews, RFC participation, tech talks
9. **Continuous Learning & Mentorship** - Evidence: New hire +1 Dreyfus level, buddy system feedback
10. **Innovative Spirit** - Evidence: Quarterly hack-day POCs, conference attendance, creative solutions

**Evidence Categorization**:
- **PROVEN**: Strong evidence from resume/materials → Verification questions
- **SUGGESTED**: Weak/indirect evidence → Deep probe questions  
- **MISSING**: No evidence found → Comprehensive discovery questions

### Enhanced Technical Assessment (40% Weight, 50 Minutes)

#### AI-Assisted Development Capability (25 Minutes)
Based on proven assessment framework from AI-Assisted Technical Assessment guidance:

**Sample Assessment Tasks**:
- **API Enhancement Challenge**: Implement OAuth 2.0, structured logging, Prometheus metrics with AI assistance
- **Code Refactoring Exercise**: Improve AI-generated code for maintainability, testing, error handling
- **Prompt Engineering Mini-Challenge**: Design effective prompts for specific technical outputs

**Evaluation Criteria** (15 points total):
- **Prompt Framing & Clarity** (5 points): Context-rich questions, iterative refinement
- **Validation & Debugging** (5 points): Testing AI outputs, identifying issues, cross-referencing
- **Iteration & Learning** (5 points): Improving approach through AI collaboration cycles

#### Platform Engineering Systems Thinking (25 Minutes)
**Sample Assessment Scenarios**:
- **Scalable Architecture Design**: 10x traffic increase architecture with AI research assistance
- **Live Issue Debugging**: Latency spike root cause analysis with AI collaboration
- **Production System Enhancement**: Horizontal scaling preparation with AI-guided implementation

**Evaluation Criteria** (10 points total):
- **Integration & Code Quality** (5 points): Well-structured, secure, maintainable AI-assisted solutions
- **Communication & Collaboration** (5 points): Clear reasoning, transparent AI usage, collaborative approach

## Generated Materials

### 1. Hybrid Candidate Context Briefing
**Primary Location**: `artifacts/public/hiring/candidates/{date}_{candidate_id}/interview/candidate_context.md`

**Contents**:
```markdown
# Candidate Context & Hybrid Assessment Analysis

## Executive Briefing
- Summary combining cultural fit and technical capability assessment
- Cultural Alignment through BEI core values evidence mapping
- Technical Capability via AI-assisted development and platform engineering potential
- Overall Recommendation with hybrid scoring rationale

## BEI Core Values Mapping (PROVEN / SUGGESTED / MISSING)
### Traditional BEI Assessment (60% Weight)
- Technical Excellence & Scalable Elegance: **[STATUS]** — Evidence: [Specific evidence or gap]
- Customer-Centric Craftsmanship: **[STATUS]** — Evidence: [Specific evidence or gap]
- Ownership & Proactivity: **[STATUS]** — Evidence: [Specific evidence or gap]
[... all 10 values mapped]

## Technical Capability Assessment (40% Weight)
### AI-Assisted Development Capability
- AI Tool Usage Evidence: [Evidence of AI collaboration in projects]
- Iteration and Learning: [Evidence of improvement capability]
- Technical Problem-Solving: [Approach to complex challenges]

### Platform Engineering Potential
- Systems Thinking: [Evidence of platform/architecture thinking]
- Production Mindset: [Evidence of operational/reliability focus]
- Cross-System Integration: [Evidence of distributed systems work]

## Hybrid Interview Strategy
- BEI Priorities: [Top 3 MISSING core values requiring comprehensive assessment]
- Technical Focus: [AI collaboration and platform engineering areas to evaluate]
- Time Allocation: 40min BEI + 25min AI Assessment + 25min Platform Scenarios
- Success Criteria: 70% core values + 60% technical for overall 67% threshold
```

### 2. Hybrid Interview Guide
**Primary Location**: `artifacts/public/hiring/candidates/{date}_{candidate_id}/interview/interview_guide.md`

**Structure**:
```markdown
# Hybrid Interview Guide: BEI + Enhanced Technical Assessment

## Interview Structure (Total: 95 minutes)
- Introduction: 5 minutes
- BEI Core Values Assessment: 40 minutes (STAR format)
- AI-Assisted Technical Assessment: 25 minutes (hands-on)
- Platform Engineering Scenarios: 25 minutes (discussion)

## Part 1: BEI Core Values Assessment (40 minutes, 60% weight)
### Traditional BEI Strategy - Focus on MISSING Values
**Methodology**: Use STAR format questions targeting core values with no evidence found

### [Missing Value Name] (X minutes)
- Core Value Definition: [Exact definition from mission_vision_values.yaml]
- What to Verify: [Specific behavioral demonstration needed]
- STAR Question: [Experience-based question following STAR methodology]
- Follow-up Probes: [Deeper exploration questions for incomplete responses]
- What Good Looks Like: [Behavioral indicators of strong alignment]
- Anti-Pattern Red Flags: [Warning signs of misalignment]

## Part 2: AI-Assisted Technical Assessment (25 minutes, 20% weight)
**Objective**: Evaluate AI collaboration effectiveness following proven assessment framework
**Setup**: Provide access to Claude/ChatGPT, GitHub Copilot, documentation

**Assessment Tasks** (choose 1-2 based on candidate background):

### Option A: API Enhancement with AI Assistance
**Brief**: Provide small REST API lacking authentication and minimal logging
**Task**: Implement OAuth 2.0, structured logging, Prometheus metrics, horizontal scaling prep
**Tools**: Any AI assistant, development environment
**Evaluation Focus**: 
- Prompt quality for security best practices requests
- Critical validation of AI-generated authentication code
- Integration of AI suggestions into existing codebase

### Option B: Refactor AI-Generated Code  
**Brief**: Provide AI-generated code snippet lacking structure and error handling
**Task**: Refactor into maintainable functions, add tests, improve error handling
**Tools**: Any AI assistant for suggestions and improvements
**Evaluation Focus**:
- Identification of code quality issues
- Effective prompting for best practices
- Improvement beyond AI's initial output

### Option C: Prompt Engineering Challenge
**Brief**: Design prompts for specific technical outputs using available AI tools
**Task**: Generate Python function with specific requirements and documentation
**Evaluation Focus**:
- Systematic approach to prompt design
- Iterative refinement based on output quality
- Balance between specificity and flexibility

## Part 3: Platform Engineering Scenarios (25 minutes, 20% weight)
**Objective**: Assess systems thinking with AI-assisted research capability

### Scenario A: Scalable Architecture Design with AI Research
**Situation**: Platform expects 10x traffic increase next quarter
**Task**: Design architecture handling load, reliability, feature experimentation
**Tools**: AI assistant, whiteboard/drawing tools
**Assessment Focus**: 
- AI research of scalability patterns (microservices, queues, caching)
- Integration of AI insights with personal experience
- Justification of design decisions and fallback plans

### Scenario B: Live Issue Debugging with AI Assistance
**Situation**: Application with latency spike after recent change
**Task**: Identify root cause and propose fix using AI collaboration
**Assessment Focus**:
- Evidence gathering before AI consultation
- Effective prompting for debugging assistance  
- Validation of AI suggestions through monitoring and testing
```

### 3. Hybrid Interview Script
**Primary Location**: `artifacts/public/hiring/candidates/{date}_{candidate_id}/interview/interview_script.md`

**Contents**:
```markdown
# Hybrid Interview Script - BEI Core Values + Enhanced Technical Assessment

## Part 1: Introduction & Methodology Explanation (5 mins)
"Today's interview combines our traditional behavioral assessment with enhanced technical evaluation. 
We'll spend 40 minutes on behavioral questions using the STAR format, followed by hands-on 
AI-assisted development assessment and platform engineering scenarios."

## Part 2: BEI Core Values Assessment via STAR Questions (40 mins)
### [Missing Value Name] (X mins based on priority)
**Value Definition**: [Exact definition from company values]
**STAR Question**: "Tell me about a specific time when you [behavioral scenario]. Please walk me through:
- **Situation**: What was the context and background?
- **Task**: What was your specific responsibility or challenge?
- **Action**: What specific actions did you personally take? 
- **Results**: What were the outcomes, and what did you learn?"

**Follow-up Probes** (if response incomplete):
- "Can you give me more detail about [specific aspect]?"
- "What was your specific role in that situation?"
- "How did you measure the success of your actions?"

[Repeat for all MISSING and SUGGESTED values]

## Part 3: AI-Assisted Technical Assessment (25 mins)
"Now let's move to hands-on technical assessment. You'll have access to AI tools like Claude, ChatGPT, 
or GitHub Copilot - please use whichever you're most comfortable with. We're interested in seeing 
how you collaborate with AI to solve real engineering problems.

**For API Enhancement Challenge**: 'I'll provide you with a small REST API that needs authentication 
and better observability. Please implement OAuth 2.0 authentication, add structured logging, and 
prepare it for horizontal scaling. Feel free to use AI assistance, but please explain your prompts 
and validate the suggestions you receive.'

**Interview Observation Notes**:
- Prompt Framing & Clarity (5 points): Does candidate ask clear, context-rich questions to AI?
- Validation & Debugging (5 points): Do they test AI outputs and identify potential issues?
- Iteration & Learning (5 points): Do they improve their approach through AI collaboration?"

## Part 4: Platform Engineering Scenarios (25 mins)  
"Let's discuss platform architecture with AI research assistance available...

**For Architecture Design**: 'Our platform expects a 10x traffic increase next quarter. Using AI 
tools to research scalability patterns, design an architecture that can handle the load while 
ensuring reliability. Please walk me through your research process and design decisions.'

**Interview Observation Notes**:
- Integration & Code Quality (5 points): Well-structured, secure solutions with AI assistance?
- Communication & Collaboration (5 points): Clear explanation of AI usage and reasoning?"
```

## Hybrid Scoring Framework

### Overall Assessment Calculation
```yaml
Core_Values_BEI_Assessment: 60% (50 points max - 1-5 per value)
Technical_Assessment: 40% (25 points max - AI collaboration + platform engineering)
Total_Points: 75 points maximum

Minimum_Requirements:
  Overall: 50+ points (67%)
  Core_Values: 35+ points (70% of BEI portion)
  Technical: 15+ points (60% of technical portion) 
  No_Value_Below: Level 2 (40%) in any core value
  
Decision_Matrix:
  Strong_Hire: 65+ points (87%)
  Hire: 55+ points (73%) 
  Lean_Hire: 50+ points (67%)
  No_Hire: <50 points (67%)
```

### Phoenix_005 Re-evaluation Example
```yaml
BEI_Core_Values: 33/50 (66% - below 70% threshold but strong learning foundation)

AI-Assisted_Technical_Assessment: 19/25 (76% breakdown):
  Prompt_Framing_Clarity: 4/5 - Good context-rich AI instructions, iterative refinement
  Validation_Debugging: 3/5 - Some critical evaluation, needs development
  Iteration_Learning: 5/5 - Exceptional improvement through AI collaboration cycles
  Integration_Code_Quality: 3/5 - Basic AI-assisted development, good adaptation
  Communication_Collaboration: 4/5 - Clear explanation of AI usage and reasoning

Overall_Score: 52/75 (69%) - LEAN HIRE
Recommendation: Hire as Junior Platform Engineer with development plan
  - Core values development through mentorship (focus on technical excellence, observability)
  - AI collaboration skills are strong foundation for modern platform engineering
  - High learning agility suggests rapid improvement potential
```

## Processing Steps

### 1. Hybrid Context Assembly
- Load normalized candidate data and all assessment materials
- Retrieve BEI core values framework and behavioral indicators
- Parse enhanced technical competency requirements
- Load hybrid scoring framework and decision matrix

### 2. BEI Core Values Evidence Mapping
- Systematically analyze candidate materials for each of the 10 values
- Categorize evidence as PROVEN/SUGGESTED/MISSING
- Document specific examples and behavioral indicators found
- Identify evidence gaps requiring STAR format exploration
- Generate targeted BEI questioning strategy

### 3. Enhanced Technical Assessment Planning
- Analyze AI-assisted development evidence from take-home/portfolio
- Assess platform engineering potential and systems thinking capability
- Design AI collaboration simulation scenarios
- Plan platform engineering discussion topics

### 4. Hybrid Interview Generation
- Create STAR format questions for each core value based on evidence analysis  
- Generate AI-assisted development challenges with tools access
- Design platform engineering scenarios for systems thinking assessment
- Integrate hybrid scoring guidance for interviewers

### 5. Quality Assurance
- Validate comprehensive core values coverage with adequate time allocation
- Ensure enhanced technical assessment addresses AI collaboration and platform thinking
- Check hybrid scoring framework integration and minimum thresholds
- Verify interviewer guidance for both behavioral and technical components

## Quality Validation Checklist

### BEI-Specific Requirements
- [ ] All 10 core values mapped with evidence categorization (PROVEN/SUGGESTED/MISSING)
- [ ] STAR format questions generated for comprehensive behavioral assessment
- [ ] Verification questions created for PROVEN values from materials
- [ ] Discovery questions created for MISSING values needing exploration
- [ ] 40+ minutes allocated specifically for BEI core values assessment
- [ ] Clear behavioral pattern recognition guidance for interviewers
- [ ] Follow-up probes prepared for incomplete STAR responses
- [ ] Traditional BEI methodology preserved exactly

### Enhanced Technical Assessment Requirements
- [ ] AI-assisted development simulation designed with tools access
- [ ] Platform engineering scenarios created for systems thinking evaluation
- [ ] Assessment criteria established for AI collaboration effectiveness
- [ ] Technical assessment integrated with hybrid scoring framework
- [ ] 50 minutes allocated for enhanced technical evaluation (25min each component)

### Hybrid Integration Requirements  
- [ ] Hybrid scoring framework applied (60% BEI + 40% technical = 75 points)
- [ ] Minimum thresholds established for both components
- [ ] Decision matrix integrated with hybrid scoring system
- [ ] Interviewer guidance provided for both behavioral and technical evaluation
- [ ] Quality score ≥8.5/10 across all generated materials
- [ ] Platform Lead approval obtained for hybrid assessment design

## Success Metrics

### BEI Coverage Metrics (Preserved)
- **Coverage**: All 10 values assessed with comprehensive STAR questions
- **Depth**: Multiple behavioral examples gathered per high-priority value
- **Validation**: Evidence from materials verified through targeted questioning
- **Discovery**: Missing values explored through systematic behavioral probing
- **Consistency**: Behavioral patterns confirmed across multiple questions

### Enhanced Technical Metrics (Added)
- **AI Collaboration**: Effective instruction, validation, and iteration capability assessed
- **Platform Engineering**: Systems thinking and production mindset evaluated
- **Technical Integration**: Hybrid scoring properly balances cultural and technical dimensions
- **Phoenix_005 Resolution**: Similar candidates would now achieve 67%+ overall scores

### Hybrid Assessment Metrics (New)
- **Cultural Alignment Maintained**: 60% weight ensures core values remain primary
- **Technical Capability Enhanced**: 40% weight properly evaluates AI collaboration
- **Overall Quality**: ≥90% interviewer satisfaction with hybrid materials
- **Decision Accuracy**: Improved correlation between assessment scores and job performance

## Error Handling
- **Missing BEI Context**: Request core values framework and behavioral indicators
- **Incomplete Evidence Mapping**: Flag for manual analysis with PROVEN/SUGGESTED/MISSING categorization
- **Technical Assessment Gaps**: Generate standard AI collaboration and platform scenarios
- **Hybrid Scoring Issues**: Validate 60%/40% weighting and minimum thresholds
- **Quality Failures**: Regenerate with enhanced hybrid assessment prompts

## Next Stage
Upon successful completion and approval, proceed to **Task 7: Hybrid Interview Loop** with BEI-trained interviewers and enhanced technical evaluation capability

## MCP Integration
- **sequential-thinking**: Plan hybrid assessment structure and component integration
- **exa**: Research candidate background and behavioral/technical examples
- **fetch**: Retrieve BEI methodology materials and enhanced technical frameworks

## Execution Commands

### Hybrid Assessment Single Candidate (Recommended)
```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt_v2.1_hybrid.md" \
  --context "data/public/hiring/resume/{candidate_file}.json"
```

### Legacy Workflow Integration
```bash 
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --context "context/company_info/mission_vision_values.yaml" \
  --context "context/hr_processes/evaluation/hybrid_scoring_framework.yaml" \
  --filter "candidate_id={candidate_id}" \
  --mode "hybrid_assessment"
```

### Multiple Candidates Processing
```bash
# Process all eligible candidates with hybrid assessment
for candidate in data/public/hiring/resume/*.json; do
  gemini run \
    --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt_v2.1_hybrid.md" \
    --context "$candidate"
done
```

---
**Version**: 2.1 - Hybrid BEI + Enhanced Technical Assessment
**Last Updated**: 2025-09-02
**Compliance**: Preserves BEI methodology while addressing Phoenix_005 technical assessment gap
**Framework**: Implements 60% Core Values + 40% Enhanced Technical = 75-point hybrid scoring system