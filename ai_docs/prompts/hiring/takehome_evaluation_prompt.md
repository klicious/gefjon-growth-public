---
id: takehome_evaluation_prompt_gefjon
type: prompt
domain: hiring
created_date: 2025-08-20
last_updated: 2025-08-20
author: Junie
quality_score: 10/10
tags: [prompt, takehome, evaluation, gefjon_standards]
visibility: public
version: 1.0
---

# Take-Home Assignment Evaluation Prompt: Gefjon Platform Engineering Standards

## OBJECTIVE
Evaluate a candidate's take-home assignment using Gefjon Platform Engineering Standards. The goal is to identify well-qualified engineering talent capable of building and operating production systems with strong reliability, scalability, and maintainability—not just producing working code.

## EVALUATION PHILOSOPHY
- Excellence over adequacy: Prefer robust, production-ready engineering over bare functionality.
- Production readiness: Assess durability under real-world conditions and failures.
- Systems thinking: Favor sound architecture, clean abstractions, and scalable design.
- Operational excellence: Expect sensible observability, testing, and reliability practices.
- Pragmatic innovation: Reward thoughtful optimizations and appropriate novel solutions.

## SCORING STANDARDS (1–5 scale)

### 5 — Exceptional
- Production-ready code with comprehensive observability and resilience patterns
- ~90%+ coverage including integration/performance/load/chaos where applicable
- Enterprise-aware architecture; clean modularization and scalability considerations
- Thorough documentation: API contracts, runbooks, ADRs, operational guidance
- Evidence of innovative, well-justified approaches and strong CS fundamentals

### 4 — Strong
- Near-production quality with meaningful observability and some resilience patterns
- ~80%+ coverage with multiple test types including integration
- Solid architecture with scalability considerations and appropriate patterns
- Good documentation including operational notes
- Clear optimization and advanced problem-solving evidence

### 3 — Competent
- Functional code with basic error handling and some production considerations
- ~60%+ coverage primarily unit tests, some integration
- Clean architecture with appropriate abstractions; limited enterprise patterns
- Adequate documentation for setup and usage
- Standard problem-solving; limited innovation

### 2 — Below Expectations
- Working code but minimal production readiness
- ~40%+ coverage; mostly unit tests only
- Basic architecture and patterns; notable gaps
- Minimal documentation
- Simple solutions; little to no optimization

### 1 — Inadequate
- Critical bugs or production-breaking issues
- <40% coverage or missing key test types
- Weak architecture and poor code quality
- Insufficient or missing documentation
- Basic programming competence only

## EVALUATION CRITERIA & WEIGHTS
1. Functional Correctness & Completeness (25%)
2. Code Quality & Best Practices (20%)
3. Testing Approach & Coverage (15%)
4. Documentation Quality (10%)
5. Ownership & Proactivity (15%)
6. Scalability & Design Patterns (15%)
7. Quantitative & Logical Problem Solving (10%)

## RECOMMENDATION THRESHOLDS
- Strong Hire: Overall 4.5+
- Hire: 3.8+
- Lean Hire: 3.0+
- No Hire: <3.0

Note: Calibrate expectations to the candidate’s level and assignment scope, while emphasizing correctness and ownership.

## EVIDENCE DISCIPLINE (CODE-FIRST POLICY)
- Primary evidence MUST come from code or test artifacts. README may be used mainly for Documentation & DX and reproducibility.
- Disallowed as sole evidence for Code Quality, Functional Correctness, Testing, Ownership, Scalability, or Quantitative reasoning:
  - README excerpts alone
  - Package manager or tool choices alone (e.g., uv, poetry, Gradle) without code quality signals
  - Architecture diagrams/docs without corresponding code
- Penalty caps if only non-code evidence is provided for a criterion:
  - Max 2/5 for Code Quality & Best Practices
  - Max 2/5 for Functional Correctness & Completeness
  - Max 2/5 for Testing Approach & Coverage
  - Max 2/5 for Ownership & Proactivity
  - Max 2.5/5 for Scalability & Design Patterns
  - Max 2/5 for Quantitative & Logical Problem Solving
- Always tie each score to at least one concrete code-level evidence reference: path:lineStart-lineEnd @ commitShort — note

## EVALUATION PROCESS
1. Comprehensive Code Review — prioritize production risks over surface polish
2. Architecture Analysis — abstractions, boundaries, extensibility
3. Testing Evaluation — coverage vs. risk, integration presence
4. Production Readiness — logging/metrics, error handling, resilience, operability
5. Innovation & Rationale — improvements and trade-offs
6. Documentation Review — completeness for users and operators

## OUTPUT FORMAT (Report Template)
- Title: Take-Home Assignment Evaluation Report: [Role/Level] (Gefjon Platform Engineering Standards)
- Candidate Name: [Name]
- Evaluator Name: [Name]
- Date of Evaluation: YYYY-MM-DD

### Overall Recommendation
- [ ] Strong Hire
- [ ] Hire
- [ ] Lean Hire
- [ ] No Hire

### Evaluation Criteria
1. Functional Correctness & Completeness (Weight: 25%)
   - Score: x/5
   - Comments: bullet points with concrete evidence and file/line references
2. Code Quality & Best Practices (20%)
   - Score: x/5
   - Comments: …
3. Testing Approach & Coverage (15%)
   - Score: x/5
   - Comments: …
4. Documentation Quality (10%)
   - Score: x/5
   - Comments: …
5. Ownership & Proactivity (15%)
   - Score: x/5
   - Comments: …
6. Scalability & Design Patterns (15%)
   - Score: x/5
   - Comments: …
7. Quantitative & Logical Problem Solving (10%)
   - Score: x/5
   - Comments: …

### Overall Score: x.x/5

### Limited Strengths
- …

### Critical Deficiencies
- … (call out any production-breaking risks explicitly)

### Alignment with Job Description & Engineering Values
- Technical Requirements Alignment: x/5 — summary
- Values Alignment: x/5 — summary by value (Ownership, Observability, Security, etc.)

### Next Steps
- [ ] Proceed to Interview
- [ ] Consider for another role
- [ ] Do not proceed (Justification: …)

### Critical Issues Preventing Hire (if applicable)
1. …
2. …

### Overall Assessment
Succinct paragraph summarizing why the recommendation was made, grounded in evidence.

## USAGE NOTES FOR AGENTS
- Calibrate expectations to seniority and timebox.
- Always tie comments to concrete code evidence (files/lines/examples).
- When identifying a critical risk (e.g., response normalization gap), propose a minimal viable remedy.
- Prefer precise, respectful, actionable language.
- Apply code-first evidence policy and penalty caps when only non-code evidence exists.
- Use agent_evaluation.json schema for machine-readable outputs when possible and run the aggregator.
