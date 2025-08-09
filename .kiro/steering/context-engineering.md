---
inclusion: always
---

# Context Engineering Methodology

## Core Principle
**Context Engineering** is a fundamental methodology in Gefjon Growth where all AI agents must operate with complete information awareness before executing any task.

## MCP Integration
This project utilizes **Context7** and **Exa** MCP servers to enhance AI capabilities. All agents MUST leverage these servers for their tasks.
- **Context7**: Used for retrieving up-to-date documentation and library information.
- **Exa**: Used for real-time web searches, company research, and content crawling.

## Mandatory Agent Behavior

### 1. Information Collection Protocol
- **ALWAYS** check `context/` directory for relevant company information, processes, and reference materials
- **ALWAYS** check `artifacts/` directory for existing outputs, previous work, and related data
- **NEVER** proceed with incomplete information

### 2. Context Verification Checklist
Before executing any task, agents must verify:
- [ ] All relevant context files have been loaded from `context/`
- [ ] Existing artifacts have been reviewed from `artifacts/`
- [ ] Task requirements are fully understood
- [ ] All necessary information is available

### 3. Information Request Protocol
When context is insufficient, agents MUST:
- **Stop task execution immediately**
- **Identify specific missing information**
- **Request missing data from the task provider with clear specifications**
- **Wait for complete information before proceeding**

### 4. Data Storage Requirements
All agents must:
- Save all outputs to appropriate `artifacts/` subdirectories
- Update relevant `context/` files when new information is discovered
- Maintain structured organization within directories
- Follow naming conventions and metadata standards

## Directory Structure Expectations

### Context Directory (`context/`)
- Company information (mission, values, policies)
- Process definitions and workflows
- Team structures and roles
- Reference materials and standards

### Artifacts Directory (`artifacts/`)
- **Public** (`artifacts/public/`): Shareable outputs and materials
- **Private** (`artifacts/private/`): Sensitive data and evaluations
- Organized by process type, date, and subject matter

## Error Prevention
- **No assumptions**: If information is unclear, ask for clarification
- **No guessing**: If data is missing, request it explicitly
- **No shortcuts**: Always follow the complete context engineering protocol

## Quality Assurance
Agents must validate:
- Information completeness before task execution
- Output accuracy against available context
- Proper storage of all generated materials
- Adherence to context engineering principles throughout the process