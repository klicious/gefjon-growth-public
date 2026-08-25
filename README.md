# Gefjon Growth — AI-Powered HR Automation Service

> **Public mirror notice (2026-08-25).** This is a sanitized public mirror of a production hiring-automation repository. Candidate PII (romanized and Hangul), an employee evaluation, firm-internal data (org context, financials, live assignment content), literal API credentials (replaced with redaction markers), and the business/pitch layer have been removed from the entire history — paths stripped and person references pseudonymized via `git filter-repo`; the private original is retained unmodified. Commit **dates and messages are preserved**: the config-driven, per-stage agentic workflow engine here (see `ai_docs/workflows/hiring/` — orchestrator, workflow config, stage task templates) was committed on **2025-08-12**, about two months before Anthropic launched Agent Skills (2025-10-16).

**Gefjon Growth** is an AI hiring-automation system: a production, config-driven multi-agent pipeline covering intake → screening → take-home evaluation → interview-kit generation. In its first consolidated production run it processed 13 candidates in ~6 hours (internal, self-assessed quality scoring; no external benchmark claimed).

---

## Key Features & Capabilities

| **Feature** | **Description** | **Value Delivered** |
|-------------|-----------------|-------------------|
| **Complete Hiring Pipeline Automation** | End-to-end workflow: Context loading → Data normalization → JD mapping → Screening → Assignment generation → Interview kits → Consolidation | ~6 hrs vs 40+ hrs manual for a 13-candidate batch (internal, self-assessed quality scoring) |
| **Context-Centric AI Architecture** | Multi-agent system using Claude Code, Gemini CLI, Amazon Q Developer with comprehensive context engineering | Ensures consistent, evidence-based decisions with 90%+ context completeness |
| **Production-Ready Workflow Execution** | 7-stage automated pipeline with quality gates, validation, and error handling | 13/13 candidates completed the pipeline in the first consolidated run (internal assessment; no external benchmark) |
| **BEI Interview Kit Generation** | Behavioral Event Interview materials with STAR questions mapped to company core values | Professional interview experience with personalized candidate assessment |
| **Take-Home Assignment Automation** | Personalized assignment generation and Top-Tier Industry Standards evaluation | Rigorous technical assessment focusing on production readiness and scalability |
| **Comprehensive Decision Support** | Detailed screening reports, evaluation frameworks, and consolidation summaries | Data-driven hiring decisions with confidence scoring and risk assessment |

---

## Architecture & Directory Layout

### Current Implementation (Production Ready)
- **Workflow Version**: 2.0 (Single Candidate Directory Approach)
- **Status**: operational; first consolidated production run completed end-to-end (internally assessed)
- **Last Execution**: August 11, 2025 (13 candidates, ~6 hours; internally scored)

```
gefjon-growth/
├── README.md
├── ai_docs/
│   ├── workflows/hiring/                # Production workflow implementation (the showcase)
│   ├── context_centric_multi_agent_hr_blueprint/
│   │   └── (business/pitch layers removed in this public mirror)
│   └── prompts/hiring/
├── context/                           # Generic company/HR context for AI agents
└── scripts/                           # Automation and workflow execution scripts
```

---

## Production Workflow Execution

### **1. Setup**

```bash
git clone <repository-url>
cd gefjon-growth
pip install -e .
```

*Note: Requires Python ≥3.12, UV package manager, and MCP server configuration*

### **2. Complete Hiring Pipeline Automation**

Execute the full 7-stage hiring workflow with a single command:

```bash
# Complete workflow execution
python scripts/complete_workflow_final.py
```

### **3. Proven Results (August 11, 2025 Execution)**

**Input**: 13 backend developer candidates in JSON format  
**Processing Time**: 6 hours total  
**Success Rate**: 92.3% of candidates qualified for interviews

**Outcomes**:
- **Strong Hire**: 2 candidates (15.4%) - titan-cand, atlas-cand (top internal scores)
- **Hire**: 7 candidates (53.8%) - Ready for technical interviews
- **Lean Hire**: 3 candidates (23.1%) - Additional assessment recommended
- **No Hire**: 1 candidate (7.7%) - Declined with feedback

---

## Business Focus: Freelance Service Offering

Gefjon Growth has transitioned from a platform-building initiative to a **freelance AI automation service**. The core technology is now leveraged to provide high-value, custom HR automation solutions directly to clients.

### **v2.0 Service Pitch**

(The client-facing pitch materials are not included in this public mirror.)

**Key Highlights:**
- **Target Audience**: Technology companies and growth-stage startups.
- **Value Proposition**: "Large time reduction vs the manual process (internal assessment; no external benchmark)."
- **Offering**: Custom service development with production-ready infrastructure.
- **Timeline**: 30-day delivery for pilot programs.

### **Service Tiers**
- **Pilot Program**: Risk-free trial to demonstrate value.
- **Custom Implementation**: Full-scale deployment tailored to client needs.
- **Retainer**: Ongoing support and optimization.

---

## Latest Updates (2025-08-20)

### Major Milestones
- **✅ Strategic Pivot**: Shifted from platform development to freelance service model.
- **✅ v2.0 Service Pitch**: Created new client-facing presentation materials.
- **✅ Production Workflow**: Complete 7-stage hiring pipeline; all 13 first-run candidates processed end-to-end.
- **✅ Real Results**: 13 candidates processed in ~6 hours (internal, self-assessed scoring).

### Recent Additions
- **Updated Business Focus**: README now reflects freelance service model.

## Live Documentation
For the latest features, architecture, and business model details:
- **System Overview**: `docs/live_documentation/overview.md`
- **Technical Architecture**: `ai_docs/context_centric_multi_agent_hr_blueprint/03_architecture/`

---

*Platform Status*: **Production Ready** | *Last Execution*: **August 11, 2025** | *Success Rate*: **92.3%**