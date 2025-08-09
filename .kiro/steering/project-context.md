---
inclusion: always
---

# Gefjon Growth Project Context

## Project Overview
**Gefjon Growth** is a comprehensive AI-powered HR automation platform that transforms and automates entire HR processes from hiring to talent development. While initially focused on interview automation, the system aims to fully automate HR workflows including candidate screening, take-home assignment management, interview kit generation, performance evaluation, OKR setting and tracking, talent development, and team assessment - all integrated with external tools like email, messaging platforms, and Dooray Task Management Tool.

## Core Architecture & Workflow

### MCP Integration
| Capability                           | MCP Server            | Typical Trigger Words                                      |
| ------------------------------------ | --------------------- | ---------------------------------------------------------- |
| AI-powered Research                  | `exa`                 | "research", "find info on", "deep dive on", "crawl site" |
| Sequential reasoning and planning    | `sequential-thinking` | "think step-by-step", "plan steps", "break down", "reason" |
| Browser automation & web interactions| `playwright`          | "open page", "click", "fill", "screenshot", "scrape"       |
| URL fetching & scraping              | `fetch`               | "fetch", "download", "HTTP GET", "scrape"                  |

Note: Ensure MCP servers are properly configured before use. `exa` requires a valid API key in the remote URL (exaApiKey).

### Primary AI Workflow
The system operates using a **ReAct methodology** (Reason → Act → Observe → Repeat). The current implementation focuses on the complete hiring pipeline: candidate screening → take-home assignment allocation → assignment evaluation → interview kit generation → candidate evaluation. Future expansion will automate performance reviews, OKR management, talent development tracking, and team evaluation processes.

**Current Key Command (Hiring Focus):**
```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/[candidate_file].json"
```

**Future Integration Goals:**
- Email/messaging automation for candidate communication
- Dooray Task Management Tool integration for workflow tracking
- Performance evaluation and OKR management automation
- Talent development pipeline automation

### Directory Architecture & Data Flow

```
├── ai_docs/prompts/hiring/          # Core interview generation prompts
├── context/                         # Company context for AI analysis
│   ├── company_info/               # Mission, values, OKRs
│   ├── hr_processes/hiring/        # Hiring stages and processes  
│   └── teams/                      # Team-specific context
├── data/public/hiring/resume/      # INPUT: Candidate JSON profiles
├── artifacts/public/hiring/        # OUTPUT: Generated interview materials
│   ├── interview_materials/upcoming/ # Generated candidate kits
│   └── pair_programming/           # Technical problem bank (easy/intermediate/expert)
└── artifacts/private/              # Sensitive evaluations and feedback
```

### Generated Output Structure
For each candidate, the system creates a dedicated directory under `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/` containing:
- `candidate_context.md` - Executive briefing with core value alignment
- `interview_guide.md` - Detailed interview plan with personalized questions  
- `interview_script.md` - Complete verbatim script for interviewers

## Technology Stack
- **Language:** Python ≥3.12 (specified in pyproject.toml)
- **AI Framework:** Gemini CLI with ReAct workflows
- **Project Management:** UV package manager (uv.lock present)
- **Data Versioning:** DVC (dvc.yaml)

## File Organization Principles

### Artifact Management (Context Engineering)
- **Public artifacts** (`artifacts/public/`): Shareable interview materials, process outputs, and generated content
- **Private artifacts** (`artifacts/private/`): Sensitive evaluations, feedback, and confidential data
- **Context directory** (`context/`): Company information, processes, team data, and reference materials
- **Structured subdirectories:** Logical grouping by date, candidate, process type, and material category
- **Data Completeness Rule**: All agents must verify context/artifact availability before task execution
- **Information Request Protocol**: When context is insufficient, agents must explicitly request missing information from the task provider

### Context Engineering Principles
This project develops and implements **context engineering** methodology where all agents must:

1. **Context-First Approach**: Always collect necessary information from `artifacts/` and `context/` directories before proceeding
2. **Information Completeness**: When lacking sufficient information to complete any task, agents MUST ask the instructor/task-provider for the specific information needed
3. **Structured Data Storage**: All relevant data must be saved under `artifacts/` or `context/` directories at all times
4. **Context Validation**: Verify context completeness before task execution

### Live Documentation Principle
The README.md file serves as a "live document" that automatically evolves to reflect current capabilities and focus areas.
#
# Current Implementation Status

### Completed HR Automation Components
- **Candidate Screening:** Automated analysis of candidate profiles
- **Take-Home Assignment Allocation:** Intelligent assignment matching based on role requirements
- **Assignment Evaluation:** Automated assessment of candidate submissions
- **Interview Kit Generation:** Complete interview materials with personalized questions
- **Candidate Evaluation:** Structured assessment frameworks

### Planned HR Automation Expansion
- **External Tool Integration:** Email, messaging platforms, Dooray Task Management
- **Performance Management:** Automated performance reviews and feedback cycles
- **OKR Management:** Goal setting, progress tracking, and achievement analysis
- **Talent Development:** Learning path recommendations and skill gap analysis
- **Team Evaluation:** Platform development team assessment and optimization
- **Workflow Orchestration:** End-to-end process automation with minimal human intervention

## Integration Architecture (Future)
The system will integrate with external platforms to create a seamless HR automation ecosystem:
- **Communication:** Automated candidate and employee communications
- **Task Management:** Dooray integration for workflow tracking and assignment
- **Performance Tracking:** Real-time OKR and goal progress monitoring
- **Development Planning:** Personalized talent development recommendations