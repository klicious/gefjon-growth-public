# Gefjon Growth: Operational Workflows

## Setup Guide

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd gefjon-growth
    ```
2.  **Install dependencies**:
    ```bash
    pip install -e .
    ```
    *Note: Project requires Python >=3.12*

## Primary Workflows

### Generate Interview Kit for Candidates

The primary workflow demonstrates the system's core capability: transforming candidate data into complete interview materials.

```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/20250714_candidate.json"
```

**Result:** For each candidate in the JSON file, the system creates:

*   `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/candidate_context.md` - Executive briefing with core value alignment
*   `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_guide.md` - Detailed interview plan with personalized questions
*   `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_script.md` - Complete verbatim script for interviewers

## Development Workflows

### Example Generated Output

For a candidate like Park Ji-Hyuk, the system automatically:

*   Analyzes their background (AI competition winner, Django/AWS experience)
*   Maps their achievements to company core values (Innovation, Ownership, Versatility)
*   Generates specific BEI questions referencing their projects
*   Selects appropriate technical problems based on their skill level
*   Creates red flag clarification points (e.g., depth of AWS knowledge)

<!-- workflows.md last updated from commit: 64fb3086b3a467d041068352872f75484f2d2a47 -->
