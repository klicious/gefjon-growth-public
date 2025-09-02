---
id: takehome_assignment_task
type: task
domain: hiring
stage: 5
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [takehome, assignment, personalization, github]
visibility: public
version: 1.0
---

# Task 5: Personalized Take-Home Assessment

**Purpose**: Generate personalized take-home assignments based on candidate profile, select appropriate templates, and create evaluation frameworks for technical assessment.

## Prerequisites
- **Task 4 Completed**: Automated screening with Platform Lead approval
- **Input**: Screening reports with "Strong Hire" or "Hire" recommendations
- **Templates**: `artifacts/public/hiring/takehome_assignment/templates/`
- **Evaluator GitHub Handle**: Required for collaboration setup

## Objectives
- Select appropriate assignment template based on candidate level and strengths
- Personalize assignment content to candidate's background and experience
- Generate comprehensive evaluation criteria and rubrics
- Set up GitHub collaboration requirements
- Create clear submission guidelines and success criteria

## Assignment Template Selection

### Experience Level Mapping
- **Entry Level (0-2 years)**: Basic CRUD application with testing
- **Mid Level (2-5 years)**: System design with scalability considerations
- **Senior Level (5+ years)**: Complex architecture with multiple integration points
- **Staff Level (8+ years)**: Platform design with team leadership scenarios

### Specialization Templates
- **Backend Focus**: API design, database optimization, system architecture
- **Full-Stack**: End-to-end application with frontend and backend
- **DevOps/Infrastructure**: CI/CD, monitoring, infrastructure as code
- **Performance**: High-throughput systems, optimization, monitoring

### Domain-Specific Challenges
- **Fintech**: Trading platform, compliance, audit trails, security
- **Real-Time Systems**: WebSocket, event-driven architecture, low latency
- **Data Processing**: ETL pipelines, batch processing, data quality
- **Microservices**: Service mesh, distributed systems, observability

## Processing Steps

### 1. Candidate Assessment Review
- Load screening report and competency analysis
- Identify candidate's technical strengths and experience level
- Review company value alignment and growth areas
- Determine appropriate assignment complexity

### 2. Template Selection
- Match candidate profile to appropriate template category
- Consider specialization areas and technical interests
- Select domain-specific requirements (fintech, real-time, etc.)
- Adjust complexity based on experience level

### 3. Assignment Personalization
- Customize problem statement to candidate's background
- Adjust technical requirements to include familiar and stretch technologies
- Personalize evaluation criteria based on candidate strengths
- Include specific challenges that assess growth potential

### 4. Evaluation Framework Creation
- Generate detailed rubrics aligned with company values
- Create specific evaluation criteria for technical excellence
- Include assessment points for code quality, architecture, and documentation
- Define success criteria and decision thresholds

### 5. GitHub Collaboration Setup
- Generate repository requirements and structure
- Create collaboration instructions for evaluator access
- Define submission guidelines and deliverable requirements
- Set up evaluation timeline and feedback process

## Output Structure

### Assignment Package
**Location**: `artifacts/public/hiring/takehome_assignment/upcoming/{candidate_id}/`

#### assignment.md
```markdown
# Take-Home Assignment: {candidate_id}

## Assignment Overview
**Challenge**: [Personalized challenge description]
**Time Allocation**: 4-6 hours
**Due Date**: 72 hours from assignment

## Background Context
[Relevant context based on candidate's experience]

## Technical Requirements
[Customized requirements based on candidate level]

## Evaluation Criteria
[Specific criteria aligned with company values]

## Submission Guidelines
[GitHub setup and deliverable requirements]
```

#### evaluation_sheet.md
```markdown
# Evaluation Sheet: {candidate_id}

## Evaluation Framework
- Technical Excellence (30%)
- System Design (25%)
- Code Quality (20%)
- Documentation (15%)
- Innovation (10%)

## Assessment Rubric
[Detailed scoring criteria]

## Decision Framework
- Strong Hire: ≥4.5/5.0
- Hire: ≥3.8/5.0
- Lean Hire: ≥3.0/5.0
- No Hire: <3.0/5.0
```

## Quality Gates
- **Personalization**: Assignment reflects candidate's background and interests
- **Appropriate Complexity**: Challenge matches candidate's experience level
- **Clear Requirements**: Unambiguous technical and deliverable requirements
- **Fair Evaluation**: Rubrics aligned with company values and role requirements

## GitHub Collaboration Requirements

### Repository Setup
- Candidate creates public GitHub repository
- Adds evaluator as collaborator: `{EVALUATOR_GITHUB_HANDLE}`
- Follows specified repository structure
- Includes comprehensive README with setup instructions

### Submission Requirements
- Complete working implementation
- Comprehensive documentation
- Test coverage (where applicable)
- Architecture decisions and trade-offs explanation

## Approval Workflow
- **Platform Lead Approval**: Required before assignment distribution
- **Quality Review**: Assignment content and evaluation criteria validation
- **Timeline Confirmation**: Ensure realistic time allocation and deadlines
- **Resource Availability**: Confirm evaluator availability for review

## Success Criteria
- Assignment appropriately personalized for candidate background
- Clear technical requirements and evaluation criteria
- GitHub collaboration properly configured
- Realistic timeline and deliverable expectations
- Evaluation framework aligned with company values

## Next Stage
Upon candidate submission, proceed to **Task 5b: Take-Home Assignment Evaluation**

## MCP Integration
- **sequential-thinking**: Structure assignment personalization logic
- **exa**: Research industry-standard technical challenges

## Execution Command
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/05_takehome_assignment.md" \
  --context "artifacts/public/hiring/evaluation_sheets/upcoming/{candidate_id}/screening_report.md" \
  --evaluator-github "{EVALUATOR_GITHUB_HANDLE}"
```

## Validation Checklist
- [ ] Assignment template selected based on candidate profile
- [ ] Technical requirements personalized appropriately
- [ ] Evaluation criteria aligned with company values
- [ ] GitHub collaboration requirements specified
- [ ] Realistic timeline and deliverable expectations
- [ ] Platform Lead approval obtained
- [ ] Assignment package complete and ready for distribution