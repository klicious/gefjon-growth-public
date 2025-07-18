# Candidate Screening Plan: Entry-Level Software Engineer

## 1. Objective
To efficiently screen entry-level software engineer candidates based on their resumes and application materials against the job description and company values, identifying candidates who best fit the role requirements and our engineering culture.

## 2. Inputs
- **Job Description:** `data/temp/entry_level_job_description.md` (translated to English)
- **Candidate Application Materials:**
    - Resume (may be in Korean)
    - Brief introduction
    - Description of a challenging problem solved and lessons learned
    - Project links (GitHub, papers, demos)

## 3. Screening Process (Human & LLM)

### 3.1. Pre-processing & Translation
- **Human/LLM:** If the resume or other application materials are in Korean, translate them to English. Ensure accuracy and context preservation.

### 3.2. Initial Qualification Check
- **Human/LLM:**
    - **Education/Experience:** Verify computer science degree (or related field) or full-time experience of 2 years or less.
    - **Python Fundamentals:** Look for explicit mention of Python proficiency, relevant coursework, or projects.
    - **Required Application Materials:** Confirm all required materials (introduction, resume/LinkedIn, project links, challenging problem description) are submitted. *Candidates missing required materials should be flagged for immediate rejection.*

### 3.3. Keyword & Skill Matching
- **LLM (Primary) & Human (Review):** Scan resumes and project descriptions for keywords and skills from the Job Description:
    - **Core Skills:** Python, API design, AWS deployment, data pipelines, portfolio analytics, low-latency trading systems, testing, CI/CD, GitLab.
    - **Backend Patterns:** RDBMS, caching, cloud.
    - **Preferred Skills:** Docker, FastAPI, Flask, React, crypto/equities/derivatives/modern portfolio theory.
- **Scoring:** Assign a preliminary score based on the density and relevance of matched keywords.

### 3.4. Project/Portfolio Assessment
- **Human (Primary) & LLM (Assisted):**
    - **Relevance:** Evaluate project links (GitHub repos, demos) for relevance to the role (fintech, trading, backend, data).
    - **Code Quality Indicators (LLM-assisted):** For GitHub projects, LLM can quickly analyze:
        - Presence of tests.
        - Readability (e.g., clear variable names, comments where necessary).
        - Basic architectural patterns (e.g., separation of concerns).
        - Use of Python best practices.
    - **Impact/Complexity:** Assess the complexity and impact of the projects. Look for evidence of problem-solving and practical application of skills.

### 3.5. Problem-Solving & Learning Assessment
- **Human (Primary) & LLM (Assisted):** Analyze the candidate's description of a challenging problem solved:
    - **Problem-Solving Approach:** Does the candidate demonstrate a "why before how" mindset?
    - **Learning Orientation:** Is there clear evidence of lessons learned and application of new knowledge?
    - **Depth of Understanding:** Does the candidate articulate the problem and solution clearly and comprehensively?

### 3.6. Communication & Collaboration Indicators
- **Human (Primary) & LLM (Assisted):**
    - **English Proficiency:** Assess the ability to read English technical documents and pose thoughtful questions (can be inferred from project documentation, communication style in introduction).
    - **Collaboration:** Look for evidence of teamwork in project descriptions or extracurricular activities.
    - **Code Naming/Clarity:** Inferred from project code quality (LLM can assist here).

### 3.7. Quantitative & Logical Reasoning
- **Human (Primary) & LLM (Assisted):**
    - **Quantitative Aptitude:** Look for evidence of strong numerical, mathematical, or algebraic skills in project descriptions, academic background, or problem-solving narratives.
    - **Logical Thinking:** Assess the clarity and coherence of logical arguments in written responses and project structures.
    - **Relevance to Trading/Multi-Agent Systems:** Identify any experience or interest in quantitative finance, algorithmic trading, or complex system design.

### 3.8. Alignment with Engineering Values
- **Human (Primary) & LLM (Assisted):** While subjective, look for any explicit or implicit alignment with our 11 Engineering Values:
    - Technical Excellence & Pragmatism
    - Customer-Centric Craftsmanship
    - Ownership & Proactivity
    - Observability & Guardrails First
    - Scalable Architecture over Quick Hacks
    - Data-Driven Decision-Making
    - Integrity & Reliability
    - Security & Compliance by Default
    - Collaboration & Knowledge-Sharing
    - Continuous Learning & Mentorship
    - Innovative Spirit
- **LLM Prompting:** LLM can be prompted to identify phrases or experiences that resonate with these values.

### 3.8. Red Flag Identification
- **Human/LLM:**
    - Incomplete applications.
    - Significant discrepancies or exaggerations.
    - Generic applications not tailored to the role.
    - Plagiarism in written responses.

## 4. Output
- **Screening Score/Recommendation:** (e.g., "Strong Match," "Moderate Match," "Weak Match," "Reject")
- **Justification:** A concise summary of strengths and weaknesses, referencing specific findings from the application materials.
- **Key Discussion Points:** Highlight areas for further probing during interviews (e.g., specific project details, problem-solving approaches, value alignment).
- **Next Steps:** Recommend for interview, hold for future roles, or reject.

## 5. LLM Usage Guidelines
- **Translation:** Use `google_web_search` or similar translation tools for Korean content.
- **Keyword Extraction:** Use pattern matching and NLP techniques to extract relevant skills and technologies.
- **Code Snippet Analysis:** For GitHub projects, LLM can analyze code snippets for quality, testing practices, and adherence to requirements.
- **Summarization:** Summarize long text fields (e.g., problem descriptions) for quick human review.
- **Bias Detection:** LLM can be trained to flag potentially biased language in resumes (e.g., age, gender, non-relevant personal information).
- **Structured Output:** LLM should output screening results in a structured format (e.g., JSON, YAML) for easy integration into HR systems.
