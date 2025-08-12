---
id: jd_mapping_task
type: task
domain: hiring
stage: 3
created_date: 2025-08-11
author: Kiro
quality_score: 9.0/10
tags: [jd-mapping, competency, alignment, skills]
visibility: public
version: 1.0
---

# Task 3: JD Mapping & Competency Alignment

**Purpose**: Parse job description requirements, compute skill differential analysis, and scan for company value alignment evidence to create comprehensive candidate-role fit assessment.

## Prerequisites
- **Task 2 Completed**: Intake & normalization successful
- **Input**: `data/private/hiring/working/{run_id}/candidates.normalized.json`
- **Job Description**: `artifacts/public/hiring/job_descriptions/backend_mid_level.md`

## Objectives
- Parse job description requirements and extract key competencies
- Compute skill differential analysis between candidate and role requirements
- Scan candidate materials for company value alignment evidence
- Generate competency mapping for each candidate
- Create skill gap analysis and development recommendations

## Job Description Analysis Framework

### Technical Requirements Extraction
- **Core Technologies**: Primary programming languages, frameworks, databases
- **Infrastructure Skills**: Cloud platforms, DevOps tools, monitoring systems
- **Architecture Patterns**: Microservices, distributed systems, scalability requirements
- **Domain Knowledge**: Industry-specific requirements (fintech, compliance, security)

### Experience Level Mapping
- **Years of Experience**: Required vs. candidate experience
- **Project Complexity**: Scale and complexity of required project experience
- **Leadership Requirements**: Team leadership, mentoring, technical decision-making
- **Business Impact**: Revenue impact, user scale, system criticality

### Soft Skills & Values Alignment
- **Communication**: Technical communication, documentation, presentation skills
- **Collaboration**: Team work, cross-functional collaboration, conflict resolution
- **Problem-Solving**: Analytical thinking, innovation, troubleshooting approach
- **Learning Agility**: Adaptability, continuous learning, technology adoption

## Processing Steps

### 1. Job Description Parsing
- Extract technical requirements and competencies
- Identify must-have vs. nice-to-have skills
- Parse experience level and seniority requirements
- Extract company culture and values requirements

### 2. Candidate Skill Analysis
- Map candidate skills to job requirements
- Calculate skill match percentage
- Identify skill gaps and overlaps
- Assess experience level alignment

### 3. Competency Gap Analysis
- **Technical Gaps**: Missing technical skills or experience
- **Experience Gaps**: Seniority level or domain experience differences
- **Leadership Gaps**: Management or technical leadership experience
- **Domain Gaps**: Industry-specific knowledge or compliance understanding

### 4. Value Alignment Assessment
- Map candidate experiences to company values
- Identify behavioral evidence for each core value
- Assess cultural fit indicators
- Flag potential culture misalignment risks

### 5. Development Recommendations
- Prioritize skill gaps by importance and learnability
- Suggest learning paths and development opportunities
- Identify mentoring and growth potential
- Recommend onboarding focus areas

## Output Structure

### JD Mapping Report
**Location**: `data/private/hiring/working/{run_id}/jd_mapping/{candidate_id}.json`

```json
{
  "candidate_id": "atlas_001",
  "job_description": "backend_mid_level",
  "analysis_timestamp": "2025-08-11T16:00:00Z",
  "technical_alignment": {
    "overall_match": 85,
    "core_technologies": {
      "required": ["Java", "Spring Boot", "PostgreSQL", "AWS"],
      "candidate_has": ["Java", "Spring Boot", "MySQL", "AWS"],
      "match_percentage": 75,
      "gaps": ["PostgreSQL"],
      "extras": ["MySQL", "React", "TypeScript"]
    },
    "experience_level": {
      "required_years": 3,
      "candidate_years": 1.17,
      "level_match": "junior_to_mid",
      "growth_potential": "high"
    }
  },
  "competency_analysis": {
    "technical_excellence": {
      "score": 8.5,
      "evidence": ["Infrastructure design", "Performance optimization"],
      "gaps": ["Large-scale system experience"]
    },
    "leadership_potential": {
      "score": 7.8,
      "evidence": ["Team lead experience", "Technical mentoring"],
      "development_areas": ["Cross-functional leadership"]
    }
  },
  "value_alignment": {
    "ownership": {
      "score": 9.0,
      "evidence": ["End-to-end project responsibility", "Proactive problem-solving"]
    },
    "technical_excellence": {
      "score": 8.7,
      "evidence": ["Architecture design", "Performance optimization"]
    }
  },
  "recommendations": {
    "hire_recommendation": "strong_match",
    "confidence_level": 0.87,
    "development_priorities": ["PostgreSQL training", "Large-scale systems exposure"],
    "onboarding_focus": ["Fintech domain knowledge", "Security practices"],
    "growth_trajectory": "mid_to_senior_in_18_months"
  }
}
```

### Competency Summary
**Location**: `data/private/hiring/working/{run_id}/competency_summary.json`

```json
{
  "job_requirements": {
    "technical_skills": ["Java", "Spring Boot", "PostgreSQL", "AWS"],
    "experience_level": "3-5 years",
    "leadership_required": false,
    "domain_knowledge": ["fintech", "compliance"]
  },
  "candidate_analysis": [
    {
      "candidate_id": "atlas_001",
      "overall_fit": 85,
      "technical_match": 75,
      "experience_match": 60,
      "value_alignment": 90,
      "recommendation": "strong_match"
    }
  ]
}
```

## Quality Gates
- **Requirement Coverage**: 100% of job requirements analyzed
- **Evidence-Based**: All scores backed by specific candidate examples
- **Consistency**: Standardized scoring across all candidates
- **Actionability**: Clear development recommendations provided

## Error Handling
- **Missing JD**: Request job description or use default template
- **Incomplete Candidate Data**: Flag missing information for follow-up
- **Skill Mapping Issues**: Use fuzzy matching for similar technologies
- **Value Assessment Gaps**: Request additional candidate materials

## Success Criteria
- All candidates have comprehensive JD mapping analysis
- Skill gaps and development areas clearly identified
- Company value alignment evidence documented
- Actionable recommendations for hiring decisions

## Next Stage
Upon successful completion, proceed to **Task 4: Automated Screening & Recommendation**

## MCP Integration
- **sequential-thinking**: Structure competency analysis methodology
- **exa**: Research industry standards for skill requirements

## Execution Command
```bash
gemini run \
  --prompt "ai_docs/workflows/hiring/tasks/03_jd_mapping.md" \
  --context "data/private/hiring/working/{run_id}/candidates.normalized.json" \
  --context "artifacts/public/hiring/job_descriptions/backend_mid_level.md"
```

## Validation Checklist
- [ ] Job description requirements fully parsed
- [ ] All candidates have skill differential analysis
- [ ] Company value alignment evidence documented
- [ ] Development recommendations provided
- [ ] Competency gaps clearly identified
- [ ] Hire recommendations with confidence levels