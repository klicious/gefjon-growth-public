# Gefjon Growth - AI-Powered HR Automation Platform

## Project Overview

Gefjon Growth is a production-ready AI-powered HR automation service that transforms talent acquisition for technology companies. The platform delivers complete hiring pipeline automation with proven results: 13 candidates processed in 6 hours, achieving 9.2/10 quality scores and a 92% success rate.

### Business Model
- **Service Type**: Freelance AI automation service (transitioned from platform development)
- **Target Market**: Technology companies and growth-stage startups
- **Value Proposition**: 92% success rate with massive time reduction and superior quality
- **Delivery**: 30-day pilot programs with production-ready infrastructure

### Proven Results (August 11, 2025 Execution)
- **Input**: 13 backend developer candidates
- **Processing Time**: 6 hours total
- **Success Rate**: 92.3% qualification rate
- **Quality Scores**: 9.2/10 average (Strong Hire: titan-cand 9.2/10, atlas-cand 9.1/10)

## Architecture & Technology Stack

### Core Technology
- **Language**: Python ≥3.12
- **AI Framework**: Context-centric multi-agent system (Claude Code, Gemini CLI, Amazon Q Developer)
- **Package Management**: UV package manager
- **Methodology**: ReAct (Reason → Act → Observe → Repeat)

### Production Workflow
```bash
# Complete 7-stage hiring workflow execution
python scripts/complete_workflow_final.py
```

### Key Components
1. **Context Loading** → Data normalization → JD mapping
2. **Screening** → Assignment generation → Interview kits
3. **Consolidation** → Quality validation → Results delivery

## Directory Structure

```
gefjon-growth/
├── .amazonq/                        # Amazon Q Developer configuration
├── README.md                        # Live documentation (production status)
├── ai_docs/
│   ├── workflows/hiring/            # Production workflow implementation
│   ├── context_centric_multi_agent_hr_blueprint/
│   │   └── 07_presentation/v2.0_service_pitch/ # Client materials
│   └── prompts/hiring/              # Core automation prompts
├── artifacts/public/hiring/candidates/
│   └── 20250811_consolidated/       # Real execution results
├── context/                         # Company context for AI agents
│   ├── company_info/               # Mission, values, OKRs
│   ├── hr_processes/hiring/        # Hiring stages and processes
│   └── teams/                      # Team-specific context
├── data/public/hiring/resume/      # Input candidate data (JSON)
└── scripts/                        # Automation and workflow scripts
```

## Context Engineering Protocol

### Mandatory Behavior
Amazon Q Developer must follow this context engineering methodology:

1. **Context Collection**: Always examine `context/` directory first
2. **Artifact Verification**: Check `artifacts/` for existing outputs
3. **Information Completeness**: Verify all necessary data is available
4. **Missing Data Protocol**: Request specific missing information from user
5. **Structured Storage**: Save outputs to appropriate directories

### Verification Checklist
- [ ] Context files loaded from `context/`
- [ ] Existing artifacts reviewed from `artifacts/`
- [ ] Task requirements understood
- [ ] All necessary information available

## Company Context

### Core Values (10 Values)
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

### Interview Framework
- **BEI (Behavioral Event Interviewing)**: STAR method validation
- **Technical Deep-Dive**: Skill assessment and red flag addressing
- **Pair Programming**: Tiered problems (easy/intermediate/expert)
- **System Design**: Customized to candidate background

## File Organization

### Artifact Management
- **Public** (`artifacts/public/`): Shareable materials and outputs
- **Private** (`artifacts/private/`): Sensitive evaluations and feedback
- **Context** (`context/`): Company information and processes
- **Structured Organization**: By date, candidate, process type

### Quality Standards
- Maintain 9.2/10+ quality scores
- Ensure 90%+ success rates
- Follow context engineering principles
- Implement comprehensive error handling

## Development Guidelines

### Code Quality
- Python ≥3.12 best practices
- Comprehensive error handling
- Structured logging for debugging
- Clean, documented code
- Context engineering compliance

### Security & Compliance
- Appropriate handling of sensitive candidate data
- Proper access controls implementation
- Data privacy regulation compliance
- Audit trail maintenance

## Service Delivery

### Client Engagement
- **Pilot Programs**: Risk-free value demonstration
- **Custom Implementation**: Full-scale tailored deployment
- **Retainer Services**: Ongoing support and optimization

### Future Expansion
- Performance Management automation
- OKR Management and tracking
- Talent Development personalization
- Team Evaluation optimization
- External Tool Integration (email, messaging, Dooray)

## Working Guidelines

### Best Practices
1. Load context before starting tasks
2. Verify artifact availability and relevance
3. Request missing information explicitly
4. Save outputs to appropriate directories
5. Follow established naming conventions
6. Maintain quality standards
7. Document significant changes

### Error Prevention
- No assumptions about missing information
- No guessing when data is unclear
- Always follow complete context engineering protocol
- Validate information completeness before execution
