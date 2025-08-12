#!/usr/bin/env python3
"""
Clean up hiring workflow files to eliminate confusion
Archive old versions and promote enhanced versions to primary
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

def create_archive_directory():
    """Create archive directory for old files"""
    archive_dir = Path("ai_docs/workflows/hiring/ARCHIVED")
    archive_dir.mkdir(exist_ok=True)
    return archive_dir

def archive_file(file_path, archive_dir, reason="obsolete"):
    """Archive a file with timestamp and reason"""
    if not file_path.exists():
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d")
    archived_name = f"{timestamp}_{reason}_{file_path.name}"
    archive_path = archive_dir / archived_name
    
    shutil.move(str(file_path), str(archive_path))
    print(f"📦 Archived: {file_path.name} → {archived_name}")
    return True

def rename_file(old_path, new_path):
    """Rename a file to its new primary name"""
    if not old_path.exists():
        return False
    
    if new_path.exists():
        print(f"⚠️  Target exists, skipping rename: {new_path.name}")
        return False
    
    shutil.move(str(old_path), str(new_path))
    print(f"✅ Renamed: {old_path.name} → {new_path.name}")
    return True

def main():
    """Main cleanup function"""
    print("🧹 Starting Workflow Cleanup")
    print("=" * 50)
    
    archive_dir = create_archive_directory()
    
    # Files to archive (obsolete/old versions)
    files_to_archive = [
        # Old orchestrator
        ("ai_docs/workflows/hiring/orchestrator.md", "old_version"),
        
        # Old workflow config
        ("ai_docs/workflows/hiring/config/workflow_config.yaml", "old_version"),
        
        # Already archived files (move to proper archive)
        ("ai_docs/workflows/hiring_end_to_end_ARCHIVED.md", "already_archived"),
        
        # Summary files that are now obsolete
        ("ai_docs/workflows/hiring/workflow_enhancement_summary.md", "summary_obsolete"),
        
        # Old end-to-end workflow
        ("ai_docs/workflows/hiring_end_to_end.md", "old_version"),
        ("ai_docs/workflows/hiring_end_to_end.yaml", "old_version"),
    ]
    
    # Archive obsolete files
    print("\n📦 Archiving obsolete files...")
    for file_path_str, reason in files_to_archive:
        file_path = Path(file_path_str)
        archive_file(file_path, archive_dir, reason)
    
    # Files to rename (enhanced → primary)
    files_to_rename = [
        # Enhanced orchestrator becomes primary
        ("ai_docs/workflows/hiring/orchestrator_enhanced.md", "ai_docs/workflows/hiring/orchestrator.md"),
        
        # Enhanced workflow becomes primary
        ("ai_docs/workflows/hiring/enhanced_single_candidate_workflow.md", "ai_docs/workflows/hiring/single_candidate_workflow.md"),
        
        # Enhanced config becomes primary
        ("ai_docs/workflows/hiring/config/enhanced_workflow_config.yaml", "ai_docs/workflows/hiring/config/workflow_config.yaml"),
    ]
    
    print("\n✅ Promoting enhanced versions to primary...")
    for old_path_str, new_path_str in files_to_rename:
        old_path = Path(old_path_str)
        new_path = Path(new_path_str)
        rename_file(old_path, new_path)
    
    # Create new primary workflow documentation
    print("\n📝 Creating primary workflow documentation...")
    
    # Create main workflow README
    workflow_readme_content = f"""# Gefjon Growth Hiring Workflow

## Overview
This directory contains the complete, production-ready hiring workflow for Gefjon Growth. The workflow implements a single-candidate directory approach with comprehensive materials generation.

## Current Workflow Version
**Version**: 2.0 (Single Candidate Directory Approach)  
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}  
**Status**: Production Ready

## Quick Start

### Run Complete Workflow
```bash
python scripts/complete_workflow_integration.py
```

### Individual Components
```bash
# Consolidate existing results
python scripts/consolidate_hiring_results.py

# Generate complete materials
python scripts/generate_complete_candidate_materials.py

# Generate overall summary
python scripts/generate_overall_summary.py
```

## Workflow Components

### Core Files
- **orchestrator.md** - Main workflow orchestration and execution guide
- **single_candidate_workflow.md** - Detailed single-candidate approach documentation
- **validation_framework.md** - Quality assurance and validation processes
- **ai_agent_execution_guide.md** - Guide for AI agents executing the workflow

### Configuration
- **config/workflow_config.yaml** - Primary workflow configuration
- **tasks/** - Individual task definitions and specifications

### Scripts
- **scripts/complete_workflow_integration.py** - Master integration script
- **scripts/consolidate_hiring_results.py** - Result consolidation
- **scripts/generate_complete_candidate_materials.py** - Material generation
- **scripts/generate_overall_summary.py** - Summary generation

## Output Structure
```
artifacts/public/hiring/candidates/{{date}}_consolidated/
├── {{candidate_id}}_{{name}}/
│   ├── screening/screening_report.md
│   ├── takehome/takehome_assignment.md
│   ├── interview/candidate_context.md, interview_guide.md, interview_script.md
│   ├── evaluation/evaluation_framework.md
│   └── candidate_summary.md
├── HIRING_SUMMARY_COMPLETE.md
└── QUICK_REFERENCE_GUIDE.md
```

## Key Features
- **Single Version Per Candidate**: No duplicate files or confusion
- **Complete Material Generation**: All necessary documents auto-generated
- **Customized Assignments**: Take-home assignments based on experience level
- **Structured Interviews**: Comprehensive interview guides and scripts
- **Decision Support**: Evaluation frameworks and scoring matrices
- **Production Ready**: All materials ready for immediate use

## Archive
Obsolete and old versions are stored in `ARCHIVED/` directory with timestamps.

---
*This workflow represents the current production version of the Gefjon Growth hiring process.*
"""
    
    readme_path = Path("ai_docs/workflows/hiring/README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(workflow_readme_content)
    print(f"📝 Updated: {readme_path.name}")
    
    # Create archive index
    archive_index_content = f"""# Archived Workflow Files

This directory contains archived versions of workflow files that have been superseded by newer versions.

## Archive Date: {datetime.now().strftime('%Y-%m-%d')}

## Archived Files:
"""
    
    # List archived files
    archived_files = list(archive_dir.glob("*"))
    for archived_file in sorted(archived_files):
        if archived_file.is_file():
            archive_index_content += f"- **{archived_file.name}** - Archived on {datetime.now().strftime('%Y-%m-%d')}\n"
    
    archive_index_content += f"""
## Reason for Archival:
- **old_version**: Superseded by enhanced/updated versions
- **obsolete**: No longer needed in current workflow
- **summary_obsolete**: Summary files replaced by integrated documentation
- **already_archived**: Previously archived files moved to proper location

## Current Active Files:
- **orchestrator.md** - Main workflow orchestration (formerly orchestrator_enhanced.md)
- **single_candidate_workflow.md** - Single candidate approach (formerly enhanced_single_candidate_workflow.md)
- **config/workflow_config.yaml** - Primary configuration (formerly enhanced_workflow_config.yaml)

---
*Do not use archived files for current workflow execution. Refer to the main workflow directory for current versions.*
"""
    
    archive_index_path = archive_dir / "README.md"
    with open(archive_index_path, 'w', encoding='utf-8') as f:
        f.write(archive_index_content)
    print(f"📝 Created: {archive_index_path}")
    
    # Update main workflows README
    main_workflows_readme = Path("ai_docs/workflows/README.md")
    main_readme_content = f"""# Gefjon Growth Workflows

## Active Workflows

### Hiring Workflow
**Location**: `hiring/`  
**Status**: Production Ready  
**Version**: 2.0 (Single Candidate Directory Approach)  
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

Complete end-to-end hiring workflow with automated material generation, single-candidate directory structure, and comprehensive decision support tools.

**Quick Start**: `python scripts/complete_workflow_integration.py`

## Workflow Architecture

### Core Principles
- **Context Engineering**: All workflows follow context-first approach
- **Single Source of Truth**: No duplicate files or conflicting versions
- **Automated Generation**: Complete materials auto-generated based on candidate data
- **Production Ready**: All outputs ready for immediate use by hiring teams

### Integration Points
- **MCP Servers**: Exa, Sequential Thinking, Playwright, Fetch
- **Data Sources**: Candidate profiles, company context, job descriptions
- **Output Formats**: Markdown documents, JSON summaries, evaluation frameworks

## Development Guidelines

### Adding New Workflows
1. Follow context engineering principles
2. Implement single-version approach
3. Generate complete materials
4. Include validation frameworks
5. Provide clear documentation

### Updating Existing Workflows
1. Archive old versions with timestamps
2. Update primary files in place
3. Maintain backward compatibility where possible
4. Update integration scripts
5. Test complete workflow execution

---
*All workflows are designed for autonomous AI agent execution with human oversight.*
"""
    
    with open(main_workflows_readme, 'w', encoding='utf-8') as f:
        f.write(main_readme_content)
    print(f"📝 Updated: {main_workflows_readme.name}")
    
    print("\n" + "=" * 50)
    print("🎉 Workflow Cleanup Complete!")
    print("\n📁 Current Structure:")
    print("   ai_docs/workflows/hiring/")
    print("   ├── orchestrator.md (primary)")
    print("   ├── single_candidate_workflow.md (primary)")
    print("   ├── config/workflow_config.yaml (primary)")
    print("   ├── ARCHIVED/ (old versions)")
    print("   └── scripts/ (automation)")
    print("\n✅ All enhanced versions are now the primary versions")
    print("📦 Old versions safely archived with timestamps")
    print("🚀 Future agents will use the clean, updated workflow structure")

if __name__ == "__main__":
    main()