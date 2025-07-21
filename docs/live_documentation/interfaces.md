# Interfaces

The primary interface to the `gefjon-growth` system is through the Gemini CLI.

## CLI Commands

To generate an interview kit for a candidate, run the following command:

```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/20250714_candidate.json"
```

This command will generate a complete interview kit for the specified candidate, including a candidate context, interview guide, and interview script.