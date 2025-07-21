# Gefjon Growth: API & External Interfaces

## API Endpoints

Gefjon Growth primarily interacts with internal components and the Gemini AI API. There are no external API endpoints exposed by Gefjon Growth itself.

## Data Formats

*   **Input Data**: Candidate profiles are provided as JSON files, containing structured information about the candidate's background, experience, and skills.
*   **Output Data**: Generated interview materials are in Markdown format, including:
    *   `candidate_context.md`: Markdown file with executive briefing.
    *   `interview_guide.md`: Markdown file with detailed interview plan.
    *   `interview_script.md`: Markdown file with complete verbatim script.

## Integration Points

Gefjon Growth integrates with the following key components:

*   **Gemini AI**: The core AI engine for natural language understanding and generation. Interaction is via the Gemini CLI, which abstracts the underlying API calls.
*   **Internal Context Management**: Leverages structured data within the `context/` directory (company values, HR processes, team information) to enrich AI processing.
*   **File System**: Reads input candidate data from `data/` and writes generated interview materials to `artifacts/`.

<!-- interfaces.md last updated from commit: 64fb3086b3a467d041068352872f75484f2d2a47 -->