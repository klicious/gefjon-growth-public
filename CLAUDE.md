# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Gefjon Growth** is a comprehensive AI-powered HR automation platform designed to automate entire HR processes from hiring to talent development. While the current implementation focuses on the complete hiring pipeline (screening → take-home assignments → Top-Tier Industry Standards evaluation → interview kits → candidate assessment), the ultimate goal is to fully automate all HR workflows including performance evaluation, OKR management, talent development, and team assessment, integrated with external tools like email, messaging platforms, and Dooray Task Management Tool.

## Core Architecture & Workflow

### Primary AI Workflow
The system operates using a **ReAct methodology** (Reason → Act → Observe → Repeat) as defined in `.gemini/GEMINI.md`. The current workflow encompasses the complete hiring pipeline: candidate screening, take-home assignment allocation and Top-Tier Industry Standards evaluation, interview kit generation, and candidate assessment. Future expansion will automate performance reviews, OKR tracking, talent development, and comprehensive team evaluation processes.

**Key Command:**
```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/[candidate_file].json"
```

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

## Company Context Integration

The system integrates structured company information for candidate evaluation:

### Core Values (10 Values)
Located in `context/company_info/mission_vision_values.yaml`:
1. Technical Excellence & Scalable Elegance
2. Customer-Centric Craftsmanship  
3. Ownership & Proactivity
4. Observability & Guardrails
5. Data-Informed Iteration
6. Integrity & Reliability
7. Security & Compliance First
8. Collaboration & Knowledge-Sharing
9. Continuous Learning & Mentorship
10. Innovative Spirit

### Interview Process Framework
- **BEI (Behavioral Event Interviewing):** Validates core values through STAR method
- **Technical Deep-Dive:** Assesses claimed skills and addresses red flags
- **Pair Programming:** Uses problems from `artifacts/public/hiring/pair_programming/` (easy/intermediate/expert levels)
- **System Design:** Custom problems tailored to candidate background

## Development Environment

### MCP Integration
This project utilizes the following MCP servers. All agents MUST leverage them as appropriate:
- **Research (Primary → Fallback)**: `exa` → `google-search` for web research, company research, and content discovery/crawling
  - **Exa (`exa`)**: AI-powered research with advanced content discovery. Requires API key via remote URL (exaApiKey).
  - **Google Search (`google-search`)**: Reliable fallback for web search and content extraction when `exa` is unavailable or budget-constrained.
- **Sequential Thinking (`sequential-thinking`)**: Structured step-by-step reasoning and planning for complex tasks.
- **Playwright (`playwright`)**: Browser automation and scripted web interactions (open page, click, fill, screenshot, scrape flows).
- **Fetch (`fetch`)**: Direct URL fetching/HTTP downloads and simple scraping. Ensure proper configuration before use.

### Research Fallback Protocol
1. **Attempt `exa`** for comprehensive AI-powered research first
2. **Fall back to `google-search`** if `exa` fails, is unavailable, or budget constraints exist
3. **Both tools support** similar research workflows with different underlying implementations

### Technology Stack
- **Language:** Python ≥3.12 (specified in pyproject.toml)
- **AI Framework:** Gemini CLI with ReAct workflows
- **Project Management:** UV package manager (uv.lock present)
- **Data Versioning:** DVC (dvc.yaml)

### Installation & Setup
```bash
git clone <repository-url>
cd gefjon-growth  
pip install -e .
```

## Key Prompts & Templates

### Primary Interview Generation Prompt
Located at `ai_docs/prompts/hiring/generate_interview_kit_prompt.md` - This is the core prompt that processes candidate JSON data and generates comprehensive interview kits.

### Context Engineering Methodology
This project implements **context engineering** principles where all agents must:

1. **Context-First Loading**: Always load all context files from `context/*.yaml` before task execution
2. **Artifact Verification**: Check `artifacts/` directories for relevant existing data and outputs
3. **Information Completeness Check**: Verify all necessary information is available before proceeding
4. **Missing Information Protocol**: When context is insufficient, explicitly request missing information from the task provider
5. **Structured Data Storage**: Save all outputs and relevant data to appropriate `artifacts/` or `context/` directories

### Context Loading Pattern
The system follows this context engineering pattern:
1. Load all context files from `context/*.yaml`
2. Verify artifact availability in `artifacts/` directories
3. Extract mission, values, and relevant processes
4. Validate information completeness before task execution
5. Request missing information if context is insufficient
6. Apply complete context to task execution

## File Organization Principles

### Artifact Management (Context Engineering)
- **Public artifacts** (`artifacts/public/`): Shareable interview materials, process outputs, and generated content
- **Private artifacts** (`artifacts/private/`): Sensitive evaluations, feedback, and confidential data
- **Context directory** (`context/`): Company information, processes, team data, and reference materials
- **Structured subdirectories:** Logical grouping by date, candidate, process type, and material category
- **Context Engineering Rules**:
  - All agents must collect information from `artifacts/` and `context/` directories before proceeding
  - When information is insufficient, agents must request specific missing data from the task provider
  - All relevant data must be saved to appropriate directories at all times

### Live Documentation Principle
The README.md file serves as a "live document" that automatically evolves to reflect current capabilities and focus areas.

## Interview Kit Generation Logic

### Candidate Analysis Process
1. **Executive Summary:** 3-4 sentence profile summary
2. **Core Value Mapping:** Match candidate achievements to company values with concrete evidence
3. **Red Flag Identification:** Gaps or concerns requiring clarification
4. **Personalized Question Generation:** BEI questions referencing specific candidate experiences

### Technical Assessment Strategy
- **Problem Selection:** Based on candidate experience level (easy/intermediate/expert)
- **Red Flag Probing:** Direct questions addressing identified concerns
- **Skill Validation:** Questions targeting claimed technical competencies
- **Project Depth:** Questions requiring explanation of technical decisions and trade-offs

## Working with the System

### Adding New Candidates
1. Place candidate JSON profiles in `data/public/hiring/resume/`
2. Run the interview kit generation command
3. Review generated materials in `artifacts/public/hiring/interview_materials/upcoming/`

### Customizing Interview Materials
- Modify core values in `context/company_info/mission_vision_values.yaml`
- Update hiring process in `context/hr_processes/hiring/hiring_stages.yaml`
- Add new technical problems to `artifacts/public/hiring/pair_programming/`

### Context File Structure
All context files follow YAML format with metadata headers including `id`, `type`, `domain`, `last_updated`, `tags`, and `visibility` fields.
## Future HR Automation Scope

### Planned Expansion Areas
- **Performance Management:** Automated performance reviews, feedback cycles, and improvement tracking
- **OKR Management:** Goal setting, progress monitoring, and achievement analysis
- **Talent Development:** Personalized learning paths, skill gap analysis, and development recommendations
- **Team Evaluation:** Platform development team assessment and optimization strategies
- **External Integration:** Seamless workflow automation with email, messaging, and Dooray Task Management

### Integration Strategy
The system will evolve to integrate with external platforms creating a comprehensive HR automation ecosystem that minimizes manual intervention while maintaining personalized, high-quality HR processes across the entire employee lifecycle.

### Current vs. Future State
- **Current:** Complete hiring pipeline automation (screening through evaluation)
- **Future:** End-to-end HR process automation including ongoing employee development, performance management, and organizational optimization