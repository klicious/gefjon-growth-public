# Workflows

The primary workflow of the `gefjon-growth` system is the generation of interview kits.

1.  **Candidate Data Ingestion**: A JSON file containing the candidate's information is placed in the `data/public/hiring/resume/` directory.
2.  **Interview Kit Generation**: The `gemini run` command is executed with the appropriate prompt and context file.
3.  **Artifact Generation**: The system generates the following artifacts in the `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/` directory:
    - `candidate_context.md`: An executive briefing with core value alignment.
    - `interview_guide.md`: A detailed interview plan with personalized questions.
    - `interview_script.md`: A complete verbatim script for interviewers.

## Guard-rails

- **ReAct Methodology**: Follows Reason → Act → Observe → Repeat loops as defined in `.gemini/GEMINI.md` for consistent AI-powered analysis
- **Structured Context Engineering**: Leverages organized `context/` directory with company values, hiring processes, and team information for accurate candidate alignment
- **Live Documentation Principle**: README.md and project documentation automatically evolve to reflect current capabilities and focus areas
- **Organized Artifact Management**: Clean separation between public (shareable) and private (sensitive) interview materials with logical subdirectory structure