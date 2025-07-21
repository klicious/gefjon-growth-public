# Architecture

The `gefjon-growth` system is designed with a clear separation of concerns, organized into the following key directories:

- **`ai_docs/`**: Contains the core prompts and plans that drive the AI-powered generation of interview materials.
- **`artifacts/`**: Stores the generated interview kits, with a clear separation between public and private materials.
- **`context/`**: Holds the contextual information about the company, HR processes, and teams, which is used to tailor the interview kits.
- **`data/`**: Contains the raw candidate data that is used as input for the system.
- **`.gemini/`**: Defines the AI workflow principles and tool registry.

## Data Flow

The system follows a simple data flow:

1.  Candidate data is ingested from the `data/` directory.
2.  The AI, guided by the prompts in `ai_docs/`, processes the candidate data in the context of the information stored in the `context/` directory.
3.  The generated interview materials are saved in the `artifacts/` directory.