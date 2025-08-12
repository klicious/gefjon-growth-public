---
id: automated_screening_task
type: task
domain: hiring
stage: 4
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [screening, evaluation, recommendation]
visibility: public
version: 1.0
---

# Task 4: Automated Screening & Recommendation

**Purpose**: Conduct automated candidate screening using AI-powered analysis to generate screening reports and recommendations.

## Prerequisites
- **Task 3 Completed**: JD mapping and competency alignment
- **Input**: `data/public/hiring/working/{run_id}/jd_mapping.json` per candidate
- **Plan**: `ai_docs/plans/candidate_screening_plan.md`

## Objectives
- Apply comprehensive candidate screening methodology
- Generate detailed screening reports for each candidate
- Provide hiring recommendations with confidence scores
- Identify top candidates for take-home assignments

## Core Plan Integration
- **Primary Plan**: `ai_docs/plans/candidate_screening_plan.md`
- **Methodology**: Multi-dimensional candidate evaluation
- **Quality Standard**: ≥8.5/10 for all screening reports

## Screening Dimensions

### 1. Technical Competency
- Skills alignment with job requirements
- Experience depth and breadth
- Technology stack familiarity
- Problem-solving capability indicators

### 2. Experience Relevance
- Industry experience alignment
- Role progression analysis
- Project complexity assessment
- Leadership and mentorship experience

### 3. Company Culture Fit
- Value alignment indicators
- Communication style assessment
- Collaboration and teamwork evidence
- Growth mindset indicators

### 4. Career Trajectory
- Professional growth pattern
- Goal alignment with role
- Long-term potential assessment
- Stability and commitment indicators

## Processing Steps

### 1. Data Assembly
- Load JD mapping results for each candidate
- Retrieve normalized candidate profiles
- Access company context and values
- Gather job description requirements

### 2. Multi-Dimensional Analysis
- **Technical Scoring**: Skills match, experience depth
- **Cultural Scoring**: Value alignment, communication style
- **Experience Scoring**: Relevance, progression, achievements
- **Potential Scoring**: Growth trajectory, adaptability

### 3. Recommendation Generation
- Calculate composite screening score
- Generate recommendation category
- Identify key strengths and concerns
- Suggest next steps in hiring process

### 4. Report Generation
- Create detailed screening report per candidate
- Include evidence-based analysis
- Provide actionable recommendations
- Generate executive summary

## Output Structure

### Screening Reports
**Location**: `artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/screening_report.md`

**Contents**:
- **Executive Summary**: Overall recommendation and key insights
- **Technical Assessment**: Skills analysis and competency scoring
- **Experience Evaluation**: Relevance and depth analysis
- **Culture Fit Analysis**: Value alignment and team fit assessment
- **Recommendation**: Hire/No Hire with confidence level
- **Next Steps**: Suggested interview focus areas or concerns to address

### Screening Summary
**Location**: `data/public/hiring/working/{run_id}/screening_summary.json`

**Contents**:
```json
{
  "run_id": "20250811_103000_abc123",
  "total_candidates": 5,
  "screening_results": [
    {
      "candidate_id": "atlas_001",
      "overall_score": 8.7,
      "recommendation": "Strong Hire",
      "confidence": 0.92,
      "next_step": "take_home_assignment"
    }
  ],
  "top_candidates": ["atlas_001", "nova_002"],
  "screening_completed_at": "2025-08-11T11:45:00Z"
}
```

## Recommendation Categories

### Strong Hire (Score: 8.5-10.0)
- Exceptional alignment with role requirements
- Strong cultural fit indicators
- Proceed to take-home assignment immediately
- High confidence in success potential

### Hire (Score: 7.0-8.4)
- Good alignment with most requirements
- Solid cultural fit with minor gaps
- Proceed to take-home assignment
- Address specific areas in interview

### Lean Hire (Score: 6.0-6.9)
- Adequate alignment with some gaps
- Cultural fit requires deeper assessment
- Consider for take-home with reservations
- Focus interview on gap areas

### No Hire (Score: <6.0)
- Significant gaps in requirements
- Poor cultural fit indicators
- Do not proceed to take-home
- Provide constructive feedback

## Quality Gates
- **Report Completeness**: All sections populated with analysis
- **Evidence-Based**: Recommendations supported by specific examples
- **Bias Check**: Language and analysis reviewed for fairness
- **Scoring Consistency**: Scores align with written analysis

## Approval Workflow
- **Auto-Generation**: Screening reports generated automatically
- **Platform Lead Review**: Required before take-home assignment allocation
- **Quality Validation**: Automated quality scoring ≥8.5/10
- **Bias Audit**: Automated bias detection and flagging

## Error Handling
- **Insufficient Data**: Request additional candidate information
- **Quality Failures**: Regenerate with enhanced analysis prompts
- **Scoring Inconsistencies**: Manual review and adjustment
- **Bias Detection**: Flag for human review and correction

## Success Metrics
- **Screening Accuracy**: ≥85% correlation with final hiring decisions
- **Quality Score**: ≥8.5/10 average across all reports
- **Processing Time**: <15 minutes per candidate
- **Approval Rate**: ≥90% reports approved without revision

## Next Stage
Upon successful completion and Platform Lead approval, proceed to **Task 5: Personalized Take-Home Assessment**

## MCP Integration
- **sequential-thinking**: Structure multi-dimensional analysis
- **exa**: Research candidate background and industry context
- **fetch**: Retrieve additional candidate materials

## Execution Commands

### Single Candidate Screening
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/04_screening.md" \
  --context "data/public/hiring/working/{run_id}/jd_mapping.json" \
  --filter "candidate_id=atlas_001"
```

### Batch Screening (All Candidates)
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/04_screening.md" \
  --context "data/public/hiring/working/{run_id}/" \
  --plan "ai_docs/plans/candidate_screening_plan.md"
```

## Validation Checklist
- [ ] Screening report generated for each candidate
- [ ] All scoring dimensions completed
- [ ] Recommendations clearly stated with confidence levels
- [ ] Evidence provided for all assessments
- [ ] Quality score ≥8.5/10 achieved
- [ ] Platform Lead approval obtained
- [ ] Top candidates identified for next stage