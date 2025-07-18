
# Prompt: Enhance Ymir Root as a Universal AI Knowledge Base Template

## 1. Role and Goal

You are an AI Architect and Template Designer. Your mission is to evolve the `ymir-root` project into the definitive template for building universal, scalable, and dynamic AI knowledge bases across diverse subjects. Your goal is to bake in best practices for context management, data ingestion, and live documentation, ensuring any project forked from `ymir-root` is immediately AI-ready and highly maintainable.

---

## 2. Core Task

Your primary task is to analyze the provided `ymir-root` README (representing the current template's state) and propose concrete, actionable improvements. These improvements should focus on making the template more general, robust, and efficient for managing AI context across *multiple, arbitrary subjects*.

### **Analysis & Improvement Areas:**

1.  **Standardized `ai_docs/` Structure:** How can the `ai_docs/` directory be structured to better manage AI-generated content and the prompts that drive them?
2.  **Inclusion of Core System Prompts:** What universally useful system prompts should be part of the template to facilitate self-maintenance and intelligent data ingestion?
3.  **Explicit Secure Archiving Pattern:** How can the template demonstrate a robust and secure way to archive processed input data?
4.  **Generalized Context Organization for Multiple Subjects:** How can the `context/` directory be structured to better support multiple, distinct subject domains (e.g., HR, Finance, Engineering, Legal)?
5.  **Pattern for "Upcoming" Artifacts:** How can the template provide a clear staging area for AI-generated outputs that are awaiting review or finalization?
6.  **Emphasis on "Live Documentation" Philosophy:** How can the template ensure its `README.md` (and other key documentation) remains perpetually up-to-date through automated processes?
7.  **Demonstration of Personalized Content Generation:** How can the template showcase the pattern of generating highly personalized, multi-file outputs based on structured input?

---

## 3. Deliverables

You will generate a single, comprehensive markdown document outlining your proposed improvements. This document should be structured as follows:

### **A. Executive Summary**

*   A brief overview of the proposed enhancements and their impact.

### **B. Proposed `ymir-root` README.md (Revised Sections)**

*   Provide the full text for the sections of the `ymir-root` README.md that you propose to change or add. This includes:
    *   **Project Title & Mission:** A more general mission statement.
    *   **Key Features:** Updated to reflect new capabilities.
    *   **Directory & File Layout:** Updated ASCII tree with new/renamed directories.
    *   **Data Hygiene and Versioning:** Updated to reflect new archive practices.
    *   **Gemini CLI Execution Plan:** Updated to include new system prompts.
    *   **New Section: Core System Prompts:** Detail the standard system prompts included in the template.
    *   **New Section: Context Management Principles:** Explain the philosophy behind structuring and maintaining the knowledge base.

### **C. New Files & Directories to Add to Template**

*   List any new files or directories that should be part of the `ymir-root` template, along with their purpose.
    *   Example: `ai_docs/prompts/system/update_readme_prompt.md`
    *   Example: `ai_docs/prompts/system/integrate_new_data_prompt.md`
    *   Example: `data/private/archive/`

### **D. Modifications to Existing Files (Beyond README)**

*   Describe any changes needed in other template files (e.g., `.gemini/GEMINI.md`, `pyproject.toml`) to support the new features.

### **E. Rationale for Changes**

*   For each major proposed change, provide a clear explanation of *why* it improves the `ymir-root` template as a universal AI knowledge base.

---

## 4. Essential Context for Analysis

*You must use the following content as the current `ymir-root` README for your analysis. This content is provided directly within this prompt to ensure self-containment and avoid external dependencies.*

```markdown
# Yimir Root Project

This repository serves as the foundational skeleton for general-purpose projects, meticulously designed to leverage the capabilities of the Gemini CLI. It incorporates best practices for project structure, data management, and AI-driven development, ensuring a robust and scalable starting point for any new initiative.

## Key Features

*   **Layered Context Files**: Configuration and operational guidelines are organized in a hierarchical manner (global → project → local), mirroring the Gemini CLI's resolution order. This provides a clear separation between immutable guard-rails and domain-specific overrides.
*   **ReAct Loop Integration**: The project structure and command conventions are designed to seamlessly integrate with Gemini's Reason-then-Act (ReAct) cycle, facilitating the easy addition of new tools and automated workflows.
*   **Structured Memory**: Utilizes YAML "context sheets" for role-based metadata, enabling agents to efficiently retrieve mission statements, policies, KPIs, and project states with single function calls.
*   **Context-Engineering Patterns**: Employs advanced context-engineering techniques to minimize hallucinations and maximize token efficiency, moving beyond ad-hoc prompt strings.
*   **Robust Data & Artifact Management**: Implements a clear separation between input data and generated artifacts, with dedicated public and private trees for secure and reproducible workflows.

## Directory & File Layout

    ```
    └── ymir-root/
        ├── README.md                # Comprehensive human overview of the project
        ├── context/                 # Layered context files for various domains
        │   ├── org.yaml             # Organizational mission, values, HR policies
        │   ├── platform.yaml        # Platform Dev team glossary + live status
        │   └── ...                  # Any other domain-specific context sheets
        ├── data/                    # Input data for the project
        │   ├── public/              # Small, shareable CSV/JSON samples (tracked by Git)
        │   └── private/             # Raw dumps, CVs, PII (ignored by VCS, optionally DVC-tracked)
        ├── artifacts/               # Products generated by agents
        │   ├── public/              # Polished docs, reports, PDFs (tracked by Git, potentially LFS)
        │   └── private/             # Interim scratch, rejected outputs (ignored by VCS, optionally DVC-tracked)
        ├── scripts/                 # Helper shell/Python scripts (e.g., ETL, crawlers)
        ├── .gemini/                 # Gemini CLI configuration and resources
        │   ├── GEMINI.md            # Global instructions and guard-rails for Gemini CLI
        │   ├── examples/            # Few-shot examples per domain for AI agents
        │   ├── templates/           # Reusable output templates (JDs, task specs, etc.)
        │   ├── tools.yaml           # Declarative tool registry for ReAct
        │   └── memory/              # (Optional) Vector store or JSONL transcripts for long-term memory
        ├── .gitignore               # Specifies files and directories to be ignored by Git
        ├── dvc.yaml                 # (Optional) DVC configuration for tracking private blobs
        └── pyproject.toml           # Project metadata and dependencies (for Python projects)
    ```

## Data Hygiene and Versioning

This project adopts a robust strategy for data hygiene and large-file management:

*   **Public vs. Private Data**: `data/public` and `artifacts/public` are intended for small, shareable files that can be tracked directly by Git. `data/private` and `artifacts/private` are for sensitive or bulky data that should be ignored by Git and optionally managed with DVC (Data Version Control).
*   **Git LFS & DVC Integration**: For shareable data exceeding 10 MB, Git LFS is recommended to track pointers instead of large blobs. For private raw dumps, model checkpoints, or binary artifacts, DVC can be used to push data to external storage (e.g., S3), keeping the Git repository lean and compliant.
*   **Templated `.gitignore` and `dvc.yaml`**: Ensures consistent data hygiene and versioning practices across all forks of the project.

## Gemini CLI Execution Plan

To bootstrap and utilize this project with the Gemini CLI:

1.  **Initialize the Repository**:
    ```bash
    git init ymir-root && cd ymir-root
    gemini init        # Creates the .gemini skeleton
    mkdir -p context data/public data/private artifacts/public artifacts/private scripts
    # Copy GEMINI.md and other initial files as needed
    ```
2.  **Register Tools**: Define external tools (e.g., GitHub, Google Search) in `.gemini/tools.yaml` for use by AI agents.
3.  **Run First Agent Pass**: Execute Gemini CLI commands with specific prompts and context files.
    ```bash
    gemini run --prompt "Draft a mid-level Backend Engineer job description aligned with hiring rubric" --context "context/org.yaml"
    ```
4.  **Forking for New Domains**: Easily create new forks for specific domains, adding domain-specific context files and examples.
5.  **CI Guard-rails**: Integrate `gemini validate-context` in pre-commit hooks and set up GitHub Actions to automate tasks like summarizing repository status.

## Maintenance & Scaling Tips

*   **Vector Memory**: Mount `~/.gemini/memory` as a LiteLLM-compatible store for longer retrospectives and cross-project context deduplication.
*   **Chunk Budgets**: Keep `body:` sections in context files concise (≤ 10 KB) to optimize token usage.
*   **Iterate Prompts**: Adopt a "write-audit-rewrite" loop for prompt tuning, utilizing Gemini CLI's `--debug` option to inspect the chain-of-thought.

## Next Steps

*   **Populate `context/org.yaml`**: Add your organization's mission, values, and relevant policies.
*   **Integrate Data Sources**: Set up scripts in `scripts/` for ETL, crawling, or data conversion.
*   **Experiment with Tools**: Add and configure new tools in `.gemini/tools.yaml` to extend Gemini's capabilities.

This `README.md` is designed to be a **live document**. The Gemini CLI is configured to **continuously update this `README.m`d** whenever significant work is completed or project guidelines evolve, ensuring it always reflects the current state and best practices of the project.
```
