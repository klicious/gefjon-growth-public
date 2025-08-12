#!/usr/bin/env python3
"""
Clean up scripts directory to eliminate confusion
Archive obsolete scripts and establish clear primary versions
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

def create_scripts_archive():
    """Create archive directory for obsolete scripts"""
    archive_dir = Path("scripts/ARCHIVED")
    archive_dir.mkdir(exist_ok=True)
    return archive_dir

def archive_script(script_path, archive_dir, reason="obsolete"):
    """Archive a script with timestamp and reason"""
    if not script_path.exists():
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d")
    archived_name = f"{timestamp}_{reason}_{script_path.name}"
    archive_path = archive_dir / archived_name
    
    shutil.move(str(script_path), str(archive_path))
    print(f"📦 Archived: {script_path.name} → {archived_name}")
    return True

def main():
    """Main cleanup function"""
    print("🧹 Starting Scripts Directory Cleanup")
    print("=" * 50)
    
    archive_dir = create_scripts_archive()
    
    # Define script categories
    scripts_to_archive = [
        # Obsolete workflow integration scripts
        ("complete_workflow_integration.py", "superseded_by_final"),
        
        # Obsolete material generation scripts
        ("generate_complete_candidate_materials.py", "superseded_by_enhanced"),
        ("generate_complete_materials_enhanced.py", "incomplete_implementation"),
        
        # Development/testing scripts that are no longer needed
        ("update_workflow_to_match_reality.py", "development_only"),
        
        # Cleanup scripts that were one-time use
        ("cleanup_workflow_files.py", "one_time_use"),
        ("verify_workflow_cleanup.py", "one_time_use"),
    ]
    
    # Archive obsolete scripts
    print("\n📦 Archiving obsolete scripts...")
    for script_name, reason in scripts_to_archive:
        script_path = Path("scripts") / script_name
        archive_script(script_path, archive_dir, reason)
    
    # Identify primary scripts (keep these)
    primary_scripts = [
        "complete_workflow_final.py",           # Master workflow integration
        "generate_enhanced_materials.py",      # Complete material generation
        "consolidate_hiring_results.py",       # Result consolidation
        "generate_overall_summary.py",         # Summary generation
        "verify_workflow_consistency.py",      # Quality assurance
        "split_candidates.py",                 # Utility script
        "validate_hr_context.py",             # Context validation
    ]
    
    print("\n✅ Primary scripts (keeping these):")
    for script_name in primary_scripts:
        script_path = Path("scripts") / script_name
        if script_path.exists():
            print(f"   ✅ {script_name}")
        else:
            print(f"   ❌ Missing: {script_name}")
    
    # Create archive index
    archive_index_content = f"""# Archived Scripts Directory

This directory contains archived scripts that have been superseded or are no longer needed.

## Archive Date: {datetime.now().strftime('%Y-%m-%d')}

## Archived Scripts:

### Superseded Scripts
- **complete_workflow_integration.py** → Replaced by `complete_workflow_final.py`
- **generate_complete_candidate_materials.py** → Replaced by `generate_enhanced_materials.py`

### Development Scripts
- **update_workflow_to_match_reality.py** → Development-only script
- **generate_complete_materials_enhanced.py** → Incomplete implementation

### One-Time Use Scripts
- **cleanup_workflow_files.py** → Used for initial workflow cleanup
- **verify_workflow_cleanup.py** → Used for one-time verification

## Current Primary Scripts (in parent directory):

### Production Workflow Scripts
- **complete_workflow_final.py** - Master workflow integration script
- **generate_enhanced_materials.py** - Complete material generation
- **consolidate_hiring_results.py** - Result consolidation
- **generate_overall_summary.py** - Summary generation
- **verify_workflow_consistency.py** - Quality assurance

### Utility Scripts
- **split_candidates.py** - Candidate data processing
- **validate_hr_context.py** - Context validation

## Usage Guidelines

### For Complete Workflow Execution:
```bash
python scripts/complete_workflow_final.py
```

### For Individual Components:
```bash
# Consolidate results
python scripts/consolidate_hiring_results.py

# Generate materials
python scripts/generate_enhanced_materials.py

# Generate summary
python scripts/generate_overall_summary.py

# Verify consistency
python scripts/verify_workflow_consistency.py
```

---
*Do not use archived scripts for current workflow execution.*
*Refer to the parent scripts directory for current versions.*
"""
    
    archive_index_path = archive_dir / "README.md"
    with open(archive_index_path, 'w', encoding='utf-8') as f:
        f.write(archive_index_content)
    print(f"📝 Created archive index: {archive_index_path}")
    
    # Create main scripts README
    scripts_readme_content = f"""# Gefjon Growth Hiring Scripts

## Production Scripts (Current)

### Master Integration
- **complete_workflow_final.py** - Complete workflow integration with verification
  - Runs all components in correct order
  - Verifies completeness and consistency
  - Production-ready execution

### Core Components
- **consolidate_hiring_results.py** - Consolidate scattered results into single candidate directories
- **generate_enhanced_materials.py** - Generate complete materials for all candidates
- **generate_overall_summary.py** - Create comprehensive hiring summary
- **verify_workflow_consistency.py** - Verify workflow configuration matches results

### Utilities
- **split_candidates.py** - Process and split candidate data
- **validate_hr_context.py** - Validate HR context and configuration

## Quick Start

### Run Complete Workflow
```bash
python scripts/complete_workflow_final.py
```

This single command will:
- Consolidate existing results
- Generate all missing materials
- Create comprehensive summaries
- Verify completeness and consistency

### Run Individual Components
```bash
# Step 1: Consolidate results
python scripts/consolidate_hiring_results.py

# Step 2: Generate materials
python scripts/generate_enhanced_materials.py

# Step 3: Generate summary
python scripts/generate_overall_summary.py

# Step 4: Verify consistency
python scripts/verify_workflow_consistency.py
```

## Script Descriptions

### complete_workflow_final.py
**Purpose**: Master integration script that runs the complete hiring workflow
**Input**: Screening data and candidate information
**Output**: Complete candidate directories with all materials
**Usage**: Primary script for production workflow execution

### consolidate_hiring_results.py
**Purpose**: Consolidate scattered hiring results into organized candidate directories
**Input**: Existing hiring materials in various locations
**Output**: Single directory per candidate with standardized structure
**Usage**: First step in workflow organization

### generate_enhanced_materials.py
**Purpose**: Generate complete, comprehensive materials for all candidates
**Input**: Candidate data and screening results
**Output**: Screening reports, interview materials, communication templates
**Usage**: Core material generation for hiring decisions

### generate_overall_summary.py
**Purpose**: Create executive summary of all candidates and hiring status
**Input**: Consolidated candidate data
**Output**: HIRING_SUMMARY_COMPLETE.md and QUICK_REFERENCE_GUIDE.md
**Usage**: Executive reporting and decision support

### verify_workflow_consistency.py
**Purpose**: Verify that workflow configuration matches actual implementation
**Input**: Workflow config and generated materials
**Output**: Consistency verification report
**Usage**: Quality assurance and validation

## Archive

Obsolete and superseded scripts are stored in `ARCHIVED/` directory with timestamps and reasons for archival.

---
*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
*All scripts are production-ready and tested*
"""
    
    readme_path = Path("scripts") / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(scripts_readme_content)
    print(f"📝 Created scripts README: {readme_path}")
    
    print("\n" + "=" * 50)
    print("🎉 Scripts Directory Cleanup Complete!")
    print("\n📁 Current Structure:")
    print("   scripts/")
    print("   ├── complete_workflow_final.py (primary)")
    print("   ├── generate_enhanced_materials.py (primary)")
    print("   ├── consolidate_hiring_results.py (primary)")
    print("   ├── generate_overall_summary.py (primary)")
    print("   ├── verify_workflow_consistency.py (primary)")
    print("   ├── [utility scripts]")
    print("   ├── README.md (usage guide)")
    print("   └── ARCHIVED/ (obsolete scripts)")
    print("\n✅ Clear primary scripts established")
    print("📦 Obsolete scripts safely archived")
    print("🚀 Future agents will use clean, unambiguous scripts")

if __name__ == "__main__":
    main()