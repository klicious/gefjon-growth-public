
## LLM Prompt: Design a Comprehensive Interview Process for a Mid-Level Backend Engineer

**Objective:** Design a complete, multi-stage interview process for a Mid-Level Backend Engineer role, focusing on identifying candidates who are not only technically proficient but also possess strong quantitative aptitude, logical thinking, and excellent communication skills, crucial for our work in crypto currency quant/algorithm trading systems and multi-agent systems. The process should be robust, fair, and aligned with our company's mission, vision, and core values.

**Instructions for the LLM:**

1.  **Research Best Practices:** Conduct extensive research on modern, effective interview processes for software engineers, particularly those in quantitative finance, algorithmic trading, or AI/multi-agent system development. Include best practices for behavioral, technical, and system design interviews.
2.  **Design Multi-Stage Process:** Propose a detailed, multi-stage interview process (e.g., initial screen, technical phone screen, take-home assignment, onsite/virtual interviews with multiple rounds, final leadership interview). For each stage, specify:
    *   Purpose and what it aims to assess.
    *   Recommended duration.
    *   Key evaluation criteria.
    *   Who should be involved (e.g., HR, hiring manager, senior engineers).
3.  **Develop Interview Questions:**
    *   **Behavioral Questions:** Generate a bank of behavioral questions (beyond the existing BEI guide) that specifically probe for quantitative aptitude, logical reasoning, problem-solving under pressure, communication of complex ideas, and alignment with our core values.
    *   **Technical Questions:** Propose technical questions or problem types relevant to backend engineering, crypto quant/algo trading, and multi-agent systems. These could include coding challenges, system design problems, or theoretical questions.
    *   **Quantitative/Logical Questions:** Include specific questions or scenarios designed to assess numerical reasoning, mathematical intuition, and logical deduction.
4.  **Create Company/Team Overview Script:** Develop a script for interviewers to use at the beginning of interviews. This script should provide:
    *   **Company Overview:** Our mission, vision, and core values.
    *   **Team Overview:** The Platform Development Team's mission, guiding principles, core responsibilities, committed work (Q3/Q4 2025), high-leverage backlog, technology stack, and process/ways of working.
    *   **Culture:** Emphasize our culture of "Safety > Quality > Speed > Novelty," Scalable Elegance, Domain-Driven Design, continuous learning, and ownership.
    *   **Recent Achievements & Metrics:** Briefly highlight recent achievements (H1 2025) and key metrics (rolling 90 days) to showcase impact.
    *   **Challenges & Roadmap:** Briefly touch upon current challenges and the near-term/long-term roadmap to provide a realistic view of the work.
5.  **Identify Additional Skills:** Based on your research and the provided context, identify any other critical skills or competencies necessary for success in this role (crypto quant/algo trading, multi-agent systems) that might not be explicitly mentioned in the provided documents. Justify your suggestions.
6.  **Evaluation Rubric/Guidelines:** Provide guidelines for evaluating candidate responses, especially for the quantitative and logical reasoning aspects.
7.  **Candidate Experience:** Suggest ways to ensure a positive and engaging candidate experience throughout the process.

---

**Context for the LLM:**

To generate a tailored interview process, you must load and synthesize information from the following sources within the project structure. The context is not provided directly in this prompt.

1.  **Company & Team Context:**
    *   **Mission, Vision, and Values:** Load from `@context/company_info/mission_vision_values.yaml`. This defines our core identity and the principles we hire for.
    *   **Platform Development Team Details:** Load from `@context/teams/platform_development_team.yaml`. This file contains the team's mission, responsibilities, tech stack, roadmap, and ways of working, which are crucial for crafting relevant technical and design questions.
    *   **Company Goals & OKRs:** Load from `@context/company_info/goals_okrs.yaml` to understand the current business priorities that the role will support.

2.  **Role-Specific Context:**
    *   **Job Description:** Load the relevant job description from `@artifacts/public/hiring/job_descriptions/`. This provides the specific requirements and responsibilities for the role being hired.

3.  **Candidate-Specific Context (for personalization):**
    *   **Candidate Data:** When personalizing questions for a specific candidate, load their information from the relevant file under `@data/public/hiring/resume/`, such as `20250711_candidates.json`. This allows for tailoring questions to their specific experience and projects.

By combining these sources, you can design an interview process that is deeply aligned with our team's needs and effectively assesses a candidate's suitability for the role.
