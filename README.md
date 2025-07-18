# Gefjon Growth — Automated Interview Kit Generator

**Gefjon Growth** has evolved from a generic HR framework into a specialized **interview automation system** that transforms raw candidate data into comprehensive, personalized interview kits. Powered by Gemini AI and structured workflows, the system generates complete interview materials including candidate contexts, detailed interview guides, and full verbatim scripts—enabling consistent, thorough, and personalized candidate evaluation.

---

## Key Features & Capabilities

| **Feature** | **Description** | **Value Delivered** |
|-------------|-----------------|-------------------|
| **Automated Candidate Analysis** | Processes JSON candidate profiles to extract key insights, experience highlights, and core value alignment | Eliminates manual resume screening and ensures consistent candidate evaluation |
| **Personalized Interview Plan Generation** | Creates tailored interview guides with specific BEI questions, technical problems, and assessment strategies | Provides structured, candidate-specific interview roadmaps for interviewers |
| **Full Interview Scripting** | Generates complete, verbatim scripts including introductions, transitions, and closing statements | Ensures professional, consistent interview experience across all candidates |
| **Live Documentation** | Automatically updates project documentation to reflect current capabilities and focus | Maintains accurate, up-to-date project information as the system evolves |

---

## Directory Layout

```
gefjon-growth/
├── README.md
├── ai_docs/
│   ├── plans/                    # Interview execution and process plans
│   └── prompts/
│       └── hiring/               # Core interview kit generation prompts
├── artifacts/
│   ├── public/
│   │   └── hiring/
│   │       ├── interview_materials/
│   │       │   └── upcoming/     # Generated candidate interview kits
│   │       ├── pair_programming/ # Technical problem bank (easy/intermediate/expert)
│   │       └── interview_process.md
│   └── private/                  # Sensitive interview materials and evaluations
├── context/
│   ├── company_info/             # Mission, values, OKRs for candidate alignment
│   ├── hr_processes/             # Hiring stages and evaluation processes
│   └── teams/                    # Team-specific context for role matching
├── data/
│   ├── public/
│   │   └── hiring/
│   │       └── resume/           # Candidate JSON profiles for processing
│   └── private/                  # Sensitive candidate and evaluation data
├── .gemini/
│   ├── GEMINI.md                 # AI workflow principles and guidelines
│   └── tools.yaml                # Tool registry for ReAct workflows
└── pyproject.toml
```

---

## Quick-Start & Example Workflow

### **1. Setup**

```bash
git clone <repository-url>
cd gefjon-growth
pip install -e .
```

*Note: Project requires Python >=3.12*

### **2. Generate Interview Kit for Candidates**

The primary workflow demonstrates the system's core capability: transforming candidate data into complete interview materials.

```bash
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/20250714_candidate.json"
```

**Result:** For each candidate in the JSON file, the system creates:
- `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/candidate_context.md` - Executive briefing with core value alignment
- `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_guide.md` - Detailed interview plan with personalized questions
- `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/interview_script.md` - Complete verbatim script for interviewers

### **3. Example Generated Output**

For a candidate like Park Ji-Hyuk, the system automatically:
- Analyzes their background (AI competition winner, Django/AWS experience)
- Maps their achievements to company core values (Innovation, Ownership, Versatility)
- Generates specific BEI questions referencing their projects
- Selects appropriate technical problems based on their skill level
- Creates red flag clarification points (e.g., depth of AWS knowledge)

---

## Workflows & Guard-rails

1. **ReAct Methodology**: Follows Reason → Act → Observe → Repeat loops as defined in `.gemini/GEMINI.md` for consistent AI-powered analysis
2. **Structured Context Engineering**: Leverages organized `context/` directory with company values, hiring processes, and team information for accurate candidate alignment
3. **Live Documentation Principle**: README.md and project documentation automatically evolve to reflect current capabilities and focus areas
4. **Organized Artifact Management**: Clean separation between public (shareable) and private (sensitive) interview materials with logical subdirectory structure

---

## Current Focus & Next Steps

**Current State**: The system is actively being used to generate interview materials for specific candidates (Park Ji-Hyuk, Lee Im-Hyung, Seo Chae-Eun) as part of ongoing hiring processes. The focus has shifted from generic HR automation to specialized interview kit generation with deep personalization capabilities.

**Active Development Areas**:
- Refining interview script generation for better interviewer experience
- Expanding technical problem bank with role-specific challenges
- Enhancing core value alignment detection and evidence mapping
- Streamlining the candidate-to-interview-kit pipeline for faster turnaround

**Integration Points**: The system integrates company mission, values, and hiring processes directly into the interview generation workflow, ensuring every interview reflects organizational culture and assessment standards.

---

<!-- README.md last updated from commit: 4f9dcb4d4632c891b7e0e0745d15dc4fc2bae0af -->
