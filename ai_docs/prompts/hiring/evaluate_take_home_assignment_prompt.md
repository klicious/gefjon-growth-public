# Take-Home Assignment Evaluation Sheet – Entry-Level Software Engineer
Candidate: __________________  Evaluator: __________________  Date: ___________

## 0. Quick Reference
* **Time-box assumption:** Candidate spent ≤ 8 h on this task. Do **not** deduct for polish beyond scope. [oai_citation:7‡GoodTime](https://goodtime.io/blog/recruiting/why-candidates-are-dropping-out-of-your-hiring-process/)  
* **Gate criteria:** Functional Correctness, Code Quality, Testing must each score ≥ 2/5 or overall result ≤ “Lean Hire”.  
* **Pass guideline:** Weighted score ≥ 60 % (3.0 / 5) → Proceed; 60–74 % = Lean Hire, ≥ 75 % = Hire+. Professional pass-mark precedent: TOGAF Foundation 60 %. [oai_citation:8‡certification.opengroup.org](https://certification.opengroup.org/docs/datasheets/togaf-exams.pdf?utm_source=chatgpt.com)  
* **Bias check:** If you are down-scoring for missing observability, DI, or micro-services patterns, pause and verify that the rubric explicitly asks for it; otherwise strike that deduction. [oai_citation:9‡csed.acm.org](https://csed.acm.org/wp-content/uploads/2023/03/Version-Beta-v2.pdf?utm_source=chatgpt.com)  

## 1. Overall Recommendation  
- [ ] **Strong Hire** (≥ 4.5) - [ ] **Hire** (3.5–4.4) - [ ] **Lean Hire** (3.0–3.4) - [ ] **No Hire** (< 3.0)

---

## 2. Evaluation Criteria (behavioural anchors)

| # | Criterion | Weight | 5 (Excellent) | 3 (Meets) | 1 (Poor) |
|---|-----------|-------:|---------------|-----------|----------|
| 1 | **Functional Correctness & Completeness** | 25 % | All required flows work; graceful error paths & edge cases covered | Core flows work; minor bugs | Major feature missing or crashes |
| 2 | **Code Quality & Best Practices** | 20 % | Idiomatic, modular, PEP 8 compliant; secrets via env; clear separation | Readable; small functions; minor style issues | Tangled, hard-coded creds |
| 3 | **Testing Approach & Coverage** | 15 % | Unit + 1 integration; ≥ 60 % lines; mocks isolate APIs (LambdaTest norm) [oai_citation:10‡LambdaTest](https://www.lambdatest.com/learning-hub/test-coverage?utm_source=chatgpt.com) | Basic unit tests on main paths | Few or no tests |
| 4 | **Documentation** | 10 % | README + setup + usage + run instructions; diagram or flowchart | README covers install & run | Sparse or missing docs |
| 5 | **Ownership / Above & Beyond** | 10 % | Adds logging, metrics, config, or thoughtful TODOs; explains trade-offs | Minor extras or TODO list | No initiative shown |
| 6 | **Scalability & Design Patterns** | 5 % | Clear abstraction layer; Strategy/Factory used; easy extensibility | Basic interfaces; some duplication | Rigid, copy-paste across exchanges |
| 7 | **Quantitative & Logical Reasoning** | 5 % | Optimised logic; explains complexity; neat math where needed | Straightforward correct logic | Flawed reasoning |
| 8 | **Agentic Thinking & Future Potential** | 10 % | Proactively identifies automation opportunities; code is structured for future agentic integration. | Shows awareness of how the solution could be extended or automated. | Code is functional but rigid; no consideration for future automation. |

> **Scoring tip:** Use the table plus comments prompts below; cite file : line numbers for evidence (Swimm & Karat recommend code-anchored feedback). [oai_citation:11‡Medium](https://medium.com/swlh/take-home-coding-assignments-are-a-waste-of-time-8da74085749e?utm_source=chatgpt.com) [oai_citation:12‡Karat](https://karat.com/interview-engineering-how-to-create-a-structured-rubric-for-technical-interviews/?utm_source=chatgpt.com)  

### 2.1 Functional Correctness Prompts
* All API features implemented for both BitMEX & Binance?  
* SPOT, USD-M, USD-C supported?  
* Handles BTC/ETH/SOL, test vs prod envs, invalid inputs, API errors?

### 2.2 Code Quality Prompts
* Readability, modularity, PEP 8 compliance, secure key handling?

### 2.3 Testing Prompts
* Unit tests quality, coverage %, mocking of external calls?

### 2.4 Documentation Prompts
* Clear README (setup, usage, key config), diagrams useful?

### 2.5 Ownership Prompts
* Extra logging/metrics, config robustness, proactive improvements?

### 2.6 Scalability Prompts
* Abstractions for new exchanges, symbol mapping, pluggable order types?

### 2.7 Quant & Logic Prompts
* Evidence of quantitative reasoning, algorithmic soundness?

### 2.8 Agentic Thinking Prompts
* Does the documentation or code mention future automation possibilities?
* Is the code structured in a way that would make it easy to be called by an orchestrator agent?

---

## 3. Calculation
```
overall_score = Σ(weight × raw_score) / 100
```
List scores in the box below and compute the average to one decimal.

| Criterion | Weight | Raw (1-5) | Weighted |
|-----------|-------:|----------:|---------:|
| Functional Correctness | 25 | | |
| Code Quality | 20 | | |
| Testing | 15 | | |
| Documentation | 10 | | |
| Ownership | 10 | | |
| Scalability | 5 | | |
| Quant Reasoning | 5 | | |
| Agentic Thinking | 10 | | |
| **Total** | 100 | — | **/5** |

---

## 4. Detailed Feedback

### Strengths  
* …

### Areas for Improvement  
* …

### Alignment with Values  
Briefly map observed behaviours to relevant core values (e.g., Ownership, Scalable Elegance).

---

## 5. Next Steps
- [ ] Proceed to interview (justify)  
- [ ] Keep in pipeline for other role  
- [ ] Do not proceed (justify)
