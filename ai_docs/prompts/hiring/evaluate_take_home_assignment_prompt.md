# Take-Home Assignment Evaluation Prompt: Top-Tier Industry Standards

## OBJECTIVE
Evaluate a candidate's take-home assignment using Top-Tier Industry Standards. The goal is to identify well-qualified engineering talent capable of building and operating production systems with strong reliability, scalability, and maintainability—not just producing working code.

## EVALUATION PHILOSOPHY
- Excellence over adequacy: Prefer robust, production-ready engineering over bare functionality.
- Production readiness: Assess durability under real-world conditions and failures.
- Systems thinking: Favor sound architecture, clean abstractions, and scalable design.
- Operational excellence: Expect sensible observability, testing, and reliability practices.
- Pragmatic innovation: Reward thoughtful optimizations and novel, appropriate solutions.

## SCORING STANDARDS (1-5 Scale)

### 5 — Exceptional
- Production-ready code with comprehensive observability and resilience patterns
- ~90%+ test coverage including integration/performance/load/chaos where applicable
- Enterprise-aware architecture; clean modularization and scalability considerations
- Thorough documentation: API contracts, runbooks, ADRs, operational guidance
- Evidence of innovative, well-justified approaches and strong CS fundamentals

### 4 — Strong
- Near-production quality with meaningful observability and some resilience patterns
- ~80%+ test coverage with multiple test types including integration
- Solid architecture with scalability considerations and appropriate patterns
- Good documentation including operational notes
- Clear optimization and advanced problem-solving evidence

### 3 — Competent
- Functional code with basic error handling and some production considerations
- ~60%+ test coverage primarily unit tests, some integration
- Clean architecture with appropriate abstractions; limited enterprise patterns
- Adequate documentation for setup and usage
- Standard problem-solving; limited innovation

### 2 — Below Expectations
- Working code but minimal production readiness
- ~40%+ test coverage; mostly unit tests only
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
   - No critical bugs that would crash or corrupt in realistic operation
   - Graceful error handling and input validation
   - Completeness: features and edge cases in scope
   - Performance considerations for expected throughput
   - Red flags: unhandled failures, missing validation, incomplete core flows

2. Code Quality & Best Practices (20%)
   - Readable, maintainable, idiomatic code; appropriate patterns
   - Observability: logging, basic metrics/tracing where applicable
   - Type safety and validation (static and/or runtime where it adds value)
   - Sensible performance/caching where appropriate
   - Quality gates: linting, formatting, pre-commit hooks (if repo-scoped)

3. Testing Approach & Coverage (15%)
   - Coverage breadth and depth aligned to risk
   - Test types: unit, integration, and where relevant contract/performance/load/chaos
   - Edge cases and error-paths tested
   - CI/CD readiness or instructions for running tests locally

4. Documentation Quality (10%)
   - Clear setup, configuration, and usage
   - API contracts/specs or request/response examples
   - Operational guidance: troubleshooting, runbooks, known limitations
   - Design rationale (ADRs/trade-offs) where decisions matter

5. Ownership & Proactivity (15%)
   - Anticipation of integration issues; validation and normalization where needed
   - Production readiness signals: health checks, graceful shutdown, alerting hooks
   - Thoughtful improvements beyond bare minimum
   - Security/compliance awareness appropriate to scope

6. Scalability & Design Patterns (15%)
   - Appropriate modularization and separation of concerns
   - Resilience patterns (timeouts, retries, circuit breakers) when relevant
   - Horizontal scaling considerations; caching strategy when justified
   - Configuration management beyond hard-coded values

7. Quantitative & Logical Problem Solving (10%)
   - Algorithmic choices and complexity awareness
   - Data/precision handling correctness (e.g., decimals for financials)
   - Performance modeling or measurement where appropriate
   - Clear, logical decomposition of problems

## RECOMMENDATION THRESHOLDS
- Strong Hire: Overall 4.5+ — Ready for senior-level responsibilities with high autonomy
- Hire: 3.8+ — Strong engineer; minor gaps addressable with light mentorship
- Lean Hire: 3.0+ — Competent with potential; notable gaps requiring mentorship
- No Hire: <3.0 — Significant gaps relative to Top-Tier Industry Standards

Note: These thresholds reflect expectations for well-qualified talent. Adjust expectations to the candidate's level and assignment scope (e.g., entry-level candidates may be evaluated with calibrated expectations, while still emphasizing correctness and ownership).

## EVALUATION PROCESS
1. Comprehensive Code Review — prioritize production risks over surface polish
2. Architecture Analysis — review abstractions, boundaries, and extensibility
3. Testing Evaluation — assess coverage vs. risk and the presence of integration tests
4. Production Readiness — logging/metrics, error handling, resilience, operability
5. Innovation & Rationale — identify thoughtful improvements and trade-offs
6. Documentation Review — verify completeness for users and operators

## OUTPUT FORMAT (Report Template)
Provide a markdown report using the following structure:

- Title: Take-Home Assignment Evaluation Report: [Role/Level] (Top-Tier Industry Standards)
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

### Alignment with Job Description & Engineering Values (Top-Tier Industry Standards)
- Technical Requirements Alignment: x/5 — summary
- Values Alignment: x/5 — summary by value (e.g., Ownership, Observability, Security)

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
- Calibrate expectations to the candidate's seniority and the assignment scope/timebox.
- Always tie comments to concrete evidence (files/lines/examples).
- When identifying a critical risk (e.g., response normalization gap), propose a minimal viable remedy.
- Prefer precise, respectful, and actionable language.
- Use the thresholds to determine the final recommendation; include justification.