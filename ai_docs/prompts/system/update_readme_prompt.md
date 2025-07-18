
# Prompt: Generate Live README.md from Project State

## 1. Role and Goal

You are an AI Technical Writer and Project Analyst. Your mission is to create or update a `README.md` file that accurately and comprehensively reflects the current state of this project. You will intelligently determine whether to perform an incremental update or generate a complete, fresh `README.md` based on commit history and existing documentation. The goal is to ensure the `README.md` serves as a true "live document" that tracks with the project's evolution.

---

## 2. Core Task

Your task is to intelligently update or generate a `README.md` file based on the project's current state and commit history.

### **Pre-Analysis Phase: Commit Version Detection**

**FIRST**, determine the update strategy by checking commit history:

1. **Check if README.md exists:** Use shell command to verify if `README.md` file exists in the project root.

2. **Extract last commit version from README.md:** If README.md exists, look for a comment at the end of the file in the format:
   ```
   <!-- README.md last updated from commit: [COMMIT_HASH] -->
   ```

3. **Get current HEAD commit:** Use `git rev-parse HEAD` to get the current commit hash.

4. **Determine update strategy:**
   - **Full Generation:** If README.md doesn't exist OR no commit version comment is found
   - **Incremental Update:** If README.md exists with commit version comment AND there are newer commits
   - **No Update Needed:** If README.md exists and the commit version matches current HEAD

### **Analysis Phase:**

Based on the update strategy determined above:

**For Full Generation:**
- Analyze the entire directory structure
- Examine all key configuration files: `pyproject.toml`, `dvc.yaml`, `.gemini/GEMINI.md`, `.gemini/tools.yaml`
- Review all recent plans, prompts, and artifacts in `ai_docs/plans/`, `ai_docs/prompts/`, and `artifacts/public/`
- Use existing README.md as structural reference only

**For Incremental Update:**
- Get commit diff using: `git diff [LAST_COMMIT_HASH]..HEAD --name-only`
- Focus analysis on changed files and their impact on project documentation
- Identify which sections of README.md need updates based on file changes
- Preserve existing content that remains accurate

### **Generation Phase:**

Based on your analysis and update strategy, generate or update the `README.md`:

---

## 3. README.md Structure & Generation Logic

### **For Full Generation:**

Generate a complete README.md with the following structure:

### **A. Project Title & Mission**
*   **Action:** Write a concise, one-paragraph mission statement for the project.
*   **Logic:** Synthesize the project's purpose from the most recent plans and artifacts. The original mission was a generic HR framework, but the current focus is on **automating the creation of personalized interview kits**. Your new mission statement must reflect this evolution.

### **B. Key Features & Capabilities**
*   **Action:** Create a markdown table highlighting 3-5 key features of the current system.
*   **Logic:** Identify the most powerful and recently developed workflows. Based on the current state, these should include:
    *   **Automated Candidate Analysis:** Parsing structured candidate data.
    *   **Personalized Interview Plan Generation:** Creating tailored interview guides and context docs.
    *   **Full Interview Scripting:** Generating complete, personalized scripts for interviewers.
    *   **Live Documentation:** The process of using this very prompt to keep the project's documentation up-to-date.

### **C. Directory Layout**
*   **Action:** Generate an ASCII tree representing the current, most important directories and files.
*   **Logic:** Do not show all 200+ files. Create a representative view that highlights the key areas like `ai_docs`, `artifacts/public/hiring`, `context`, and `data`.

### **D. Quick-Start & Example Workflow**
*   **Action:** Provide a `Quick-Start` section with setup instructions and an example of the primary workflow.
*   **Logic:**
    *   Verify the setup commands (`pip install`, etc.) against `pyproject.toml`.
    *   The example workflow should **not** be a generic one. It must demonstrate the project's most current and valuable capability: **generating a full interview kit for a candidate.** Show the `gemini run` command that would trigger this, referencing the new `generate_interview_kit_prompt.md`.

### **E. Workflows & Guard-rails**
*   **Action:** Briefly explain the core development principles.
*   **Logic:** Summarize the key points from `.gemini/GEMINI.md` and mention the use of `dvc` for data separation and `pre-commit` for security, as these are foundational to the project's design.

### **F. Current Focus & Next Steps**
*   **Action:** Replace the old "Roadmap" section with a new section titled "Current Focus."
*   **Logic:** Based on the latest plans and prompts, describe the current state of the project. This should clearly state that the focus is on refining the automated generation of interview materials (guides, contexts, scripts) and embedding best practices directly into the hiring workflow.

### **For Incremental Update:**

Analyze the git diff and update only the sections that are affected by the changes:

*   **Changed Configuration Files:** If `pyproject.toml`, `dvc.yaml`, or `.gemini/*` files changed, update relevant sections (Quick-Start, Workflows & Guard-rails)
*   **New Features/Capabilities:** If new prompts, plans, or artifacts were added, update Key Features & Capabilities and Current Focus sections
*   **Structural Changes:** If directory structure changed significantly, update Directory Layout
*   **Project Evolution:** If the project's mission or focus has evolved based on recent changes, update Project Title & Mission

**Important:** Preserve existing content that remains accurate. Only modify sections that are directly impacted by the commit changes.

---

## 4. Output Format

Your final output must be a single, well-formatted markdown string, ready to be written to `README.md`. Ensure the tone is professional, clear, and engaging for a new developer joining the project.

### **Critical Requirements:**

1. **Commit Version Tracking:** ALWAYS append the following comment at the very end of the README.md file:
   ```
   <!-- README.md last updated from commit: [CURRENT_HEAD_COMMIT_HASH] -->
   ```
   Replace `[CURRENT_HEAD_COMMIT_HASH]` with the actual commit hash obtained from `git rev-parse HEAD`.

2. **Update Strategy Documentation:** For incremental updates, include a brief comment before the commit tracking comment indicating what sections were updated:
   ```
   <!-- Updated sections: [LIST_OF_SECTIONS] based on commits [LAST_COMMIT]..[CURRENT_COMMIT] -->
   <!-- README.md last updated from commit: [CURRENT_HEAD_COMMIT_HASH] -->
   ```

3. **Preserve Existing Structure:** For incremental updates, maintain the existing README.md structure and formatting style unless the changes specifically require structural modifications.

### **Quality Assurance:**

- Verify all shell commands and git operations are properly formatted
- Ensure all sections are internally consistent and up-to-date
- Double-check that the commit hash in the tracking comment matches the current HEAD
- For incremental updates, confirm that unchanged sections remain exactly as they were
