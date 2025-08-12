---
id: candidate_screening_plan
type: plan
domain: hiring
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [screening, plan, methodology, evaluation]
visibility: public
version: 1.0
---

# Candidate Screening Plan

**Purpose**: Comprehensive methodology for automated candidate screening using multi-dimensional analysis to identify top candidates for the hiring pipeline.

## Overview
This plan provides the detailed methodology for conducting thorough candidate screening that evaluates technical competency, experience relevance, cultural fit, and career trajectory to make data-driven hiring recommendations.

## Screening Framework

### Multi-Dimensional Analysis Model
The screening process evaluates candidates across four primary dimensions, each contributing to an overall screening score:

1. **Technical Competency (35%)**
2. **Experience Relevance (30%)**
3. **Company Culture Fit (20%)**
4. **Career Trajectory (15%)**

## Dimension 1: Technical Competency (35%)

### Core Technical Skills Assessment
- **Required Skills Match**: Percentage of job-required skills present in candidate profile
- **Skill Depth Indicators**: Evidence of advanced usage, certifications, project complexity
- **Technology Stack Alignment**: Familiarity with company's technology ecosystem
- **Problem-Solving Evidence**: Examples of technical challenges overcome

### Evaluation Criteria
- **Exceptional (9-10)**: 90%+ skill match, advanced proficiency evidence, leadership in technical decisions
- **Strong (7-8)**: 75%+ skill match, solid proficiency, some advanced usage examples
- **Adequate (5-6)**: 60%+ skill match, basic proficiency, limited advanced examples
- **Below Standard (3-4)**: 40%+ skill match, basic understanding, no advanced evidence
- **Poor (1-2)**: <40% skill match, minimal technical evidence

### Assessment Methods
- Parse resume/profile for technical keywords and context
- Analyze project descriptions for complexity indicators
- Evaluate GitHub/portfolio for code quality (if available)
- Cross-reference with job description requirements

## Dimension 2: Experience Relevance (30%)

### Industry & Role Experience
- **Industry Alignment**: Experience in similar industry/domain
- **Role Progression**: Career advancement pattern and trajectory
- **Project Complexity**: Scale and complexity of previous projects
- **Leadership Experience**: Team leadership, mentoring, technical leadership

### Evaluation Criteria
- **Exceptional (9-10)**: Highly relevant industry experience, clear progression, complex project leadership
- **Strong (7-8)**: Relevant experience, good progression, solid project involvement
- **Adequate (5-6)**: Some relevant experience, steady progression, moderate project complexity
- **Below Standard (3-4)**: Limited relevance, unclear progression, simple projects
- **Poor (1-2)**: Minimal relevance, no clear progression, basic project involvement

### Assessment Methods
- Analyze career progression timeline
- Evaluate project descriptions for scope and impact
- Assess leadership and mentoring indicators
- Compare experience level with role requirements

## Dimension 3: Company Culture Fit (20%)

### Value Alignment Assessment
- **Core Values Match**: Evidence of alignment with company values
- **Communication Style**: Professional communication indicators
- **Collaboration Evidence**: Teamwork and collaboration examples
- **Growth Mindset**: Learning and adaptation indicators

### Company Values Integration
Based on `context/company_info/mission_vision_values.yaml`:
- Map candidate experiences to specific company values
- Identify behavioral indicators in project descriptions
- Assess cultural contribution potential
- Evaluate team collaboration style

### Evaluation Criteria
- **Exceptional (9-10)**: Strong evidence of all core values, excellent communication, proven collaboration
- **Strong (7-8)**: Good value alignment, solid communication, team collaboration evidence
- **Adequate (5-6)**: Some value alignment, adequate communication, basic collaboration
- **Below Standard (3-4)**: Limited value evidence, poor communication indicators, minimal collaboration
- **Poor (1-2)**: No value alignment evidence, communication concerns, no collaboration indicators

## Dimension 4: Career Trajectory (15%)

### Growth & Potential Assessment
- **Career Progression**: Advancement pattern and growth rate
- **Goal Alignment**: Career goals alignment with role and company
- **Stability Indicators**: Job tenure patterns and commitment evidence
- **Learning Agility**: Continuous learning and skill development

### Evaluation Criteria
- **Exceptional (9-10)**: Rapid progression, perfect goal alignment, stable tenure, continuous learning
- **Strong (7-8)**: Good progression, strong alignment, reasonable stability, regular learning
- **Adequate (5-6)**: Steady progression, adequate alignment, acceptable stability, some learning
- **Below Standard (3-4)**: Slow progression, poor alignment, stability concerns, limited learning
- **Poor (1-2)**: No progression, misaligned goals, instability, no learning evidence

## Composite Scoring Methodology

### Weighted Score Calculation
```
Overall Score = (Technical × 0.35) + (Experience × 0.30) + 
                (Culture × 0.20) + (Trajectory × 0.15)
```

### Score Interpretation
- **9.0-10.0**: Exceptional candidate - Strong Hire recommendation
- **7.5-8.9**: Strong candidate - Hire recommendation
- **6.0-7.4**: Adequate candidate - Lean Hire recommendation
- **4.0-5.9**: Below standard - Consider with reservations
- **1.0-3.9**: Poor fit - No Hire recommendation

## Evidence Collection Framework

### Data Sources
- **Resume/CV**: Primary source for experience and skills
- **Cover Letter**: Cultural fit and communication indicators
- **Portfolio/GitHub**: Technical competency evidence
- **LinkedIn Profile**: Career progression and professional network
- **Application Responses**: Specific question responses

### Evidence Documentation
For each dimension, document:
- **Specific Examples**: Concrete evidence from candidate materials
- **Quantitative Metrics**: Numbers, percentages, measurable outcomes
- **Qualitative Indicators**: Behavioral and cultural evidence
- **Gap Analysis**: Missing information or areas of concern

## Bias Mitigation Strategies

### Unconscious Bias Prevention
- **Structured Evaluation**: Consistent criteria application
- **Evidence-Based Scoring**: Require specific examples for all scores
- **Blind Review Elements**: Focus on skills and experience over demographics
- **Multiple Perspective Integration**: Consider diverse evaluation angles

### Fairness Checks
- **Language Analysis**: Ensure neutral, professional language
- **Assumption Validation**: Question and validate all assumptions
- **Consistency Verification**: Compare scoring across similar candidates
- **Bias Audit**: Regular review of screening outcomes for patterns

## Quality Assurance Process

### Report Quality Standards
- **Completeness**: All dimensions evaluated with evidence
- **Clarity**: Clear reasoning for all scores and recommendations
- **Actionability**: Specific next steps and focus areas
- **Professional Tone**: Respectful, constructive language throughout

### Validation Checklist
- [ ] All four dimensions scored with evidence
- [ ] Composite score calculated correctly
- [ ] Recommendation aligns with scoring
- [ ] Specific examples provided for all assessments
- [ ] Next steps clearly defined
- [ ] Language reviewed for bias and professionalism
- [ ] Quality score ≥8.5/10 achieved

## Output Templates

### Screening Report Structure
```markdown
# Candidate Screening Report: {candidate_id}

## Executive Summary
- **Overall Score**: X.X/10.0
- **Recommendation**: [Strong Hire/Hire/Lean Hire/No Hire]
- **Confidence Level**: XX%
- **Key Strengths**: [Top 3]
- **Areas of Concern**: [Top 3]

## Detailed Analysis

### Technical Competency (X.X/10.0) - Weight: 35%
[Evidence-based analysis with specific examples]

### Experience Relevance (X.X/10.0) - Weight: 30%
[Career progression and project analysis]

### Company Culture Fit (X.X/10.0) - Weight: 20%
[Value alignment and collaboration evidence]

### Career Trajectory (X.X/10.0) - Weight: 15%
[Growth potential and goal alignment]

## Recommendation Rationale
[Detailed reasoning for hire/no-hire decision]

## Next Steps
[Specific actions and interview focus areas]
```

## Implementation Guidelines

### Screening Process Flow
1. **Data Collection**: Gather all available candidate materials
2. **Dimension Analysis**: Evaluate each dimension systematically
3. **Evidence Documentation**: Record specific examples and metrics
4. **Score Calculation**: Apply weighted scoring methodology
5. **Recommendation Generation**: Determine hire/no-hire with rationale
6. **Quality Review**: Validate completeness and bias-free content
7. **Report Generation**: Create comprehensive screening report

### Time Allocation
- **Data Review**: 10-15 minutes per candidate
- **Analysis & Scoring**: 15-20 minutes per candidate
- **Report Writing**: 10-15 minutes per candidate
- **Quality Review**: 5 minutes per candidate
- **Total**: 40-55 minutes per candidate

## Success Metrics
- **Screening Accuracy**: ≥85% correlation with final hiring decisions
- **Quality Score**: ≥8.5/10 average for all reports
- **Processing Efficiency**: ≤60 minutes per candidate
- **Bias Metrics**: <5% variance in scoring across demographic groups
- **Approval Rate**: ≥90% reports approved without major revision