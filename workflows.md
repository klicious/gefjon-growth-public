
# Gefjon-Growth Workflows

This document describes the key workflows for the Gefjon-Growth project.

## Project Initialization

1.  **Initialize the Repository**:
    ```bash
    git init yimir-root && cd yimir-root
    gemini init        # Creates the .gemini skeleton
    mkdir -p context data/public data/private artifacts/public artifacts/private scripts
    # Copy GEMINI.md and other initial files as needed
    ```

## AI Agent Development

1.  **Register Tools**: Define external tools (e.g., GitHub, Google Search) in `.gemini/tools.yaml` for use by AI agents.
2.  **Run First Agent Pass**: Execute Gemini CLI commands with specific prompts and context files.
    ```bash
    gemini run --prompt "Generate onboarding policy draft for interns" --context "context/org.yaml"
    ```

## Continuous Integration

*   **CI Guard-rails**: Integrate `gemini validate-context` in pre-commit hooks and set up GitHub Actions to automate tasks like summarizing repository status.
