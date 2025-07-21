
# Gefjon-Growth Features

This document outlines the core features of the Gefjon-Growth project skeleton.

## Key Features

*   **Layered Context Files**: Configuration and operational guidelines are organized in a hierarchical manner (global → project → local), mirroring the Gemini CLI's resolution order. This provides a clear separation between immutable guard-rails and domain-specific overrides.
*   **ReAct Loop Integration**: The project structure and command conventions are designed to seamlessly integrate with Gemini's Reason-then-Act (ReAct) cycle, facilitating the easy addition of new tools and automated workflows.
*   **Structured Memory**: Utilizes YAML "context sheets" for role-based metadata, enabling agents to efficiently retrieve mission statements, policies, KPIs, and project states with single function calls.
*   **Context-Engineering Patterns**: Employs advanced context-engineering techniques to minimize hallucinations and maximize token efficiency, moving beyond ad-hoc prompt strings.
*   **Robust Data & Artifact Management**: Implements a clear separation between input data and generated artifacts, with dedicated public and private trees for secure and reproducible workflows.
*   **Data Hygiene and Versioning**: Adopts a robust strategy for data hygiene and large-file management, with support for Git LFS and DVC.
