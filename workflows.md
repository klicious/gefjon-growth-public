
# Gefjon-Growth Workflows

This document describes the key workflows for the Gefjon-Growth project.

## Centralized Workflow Specs
- See ai_docs\workflows for canonical, executable specs.
- Hiring Workflow: ai_docs\workflows\hiring\orchestrator.md (config: ai_docs\workflows\hiring\config\workflow_config.yaml)

## Project Initialization

1.  Initialize the Repository:
    gemini init and create context, data, and artifacts directories as needed.

## AI Agent Development

1.  Register Tools: Define external tools in your agent configuration.
2.  Run First Agent Pass: Execute Gemini CLI commands with specific prompts and context files.

## Continuous Integration

- CI Guard-rails: Integrate context validation in pre-commit hooks and automate repository status summaries.
