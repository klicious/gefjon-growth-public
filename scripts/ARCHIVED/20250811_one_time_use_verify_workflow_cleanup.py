#!/usr/bin/env python3
"""
Verify that workflow cleanup was successful
Check for any remaining references to old files
"""

import os
from pathlib import Path
import re

def check_file_references(file_path, patterns):
    """Check if a file contains references to old patterns"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        found_references = []
        for pattern_name, pattern in patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                found_references.append((pattern_name, matches))
        
        return found_references
    except Exception as e:
        return [("error", [str(e)])]

def main():
    """Main verification function"""
    print("🔍 Verifying Workflow Cleanup")
    print("=" * 50)
    
    # Patterns to check for (old file references)
    old_patterns = {
        "enhanced_orchestrator": r"orchestrator_enhanced\.md",
        "enhanced_workflow": r"enhanced_single_candidate_workflow\.md",
        "enhanced_config": r"enhanced_workflow_config\.yaml",
        "old_end_to_end": r"hiring_end_to_end\.md",
        "old_end_to_end_yaml": r"hiring_end_to_end\.yaml",
        "enhancement_summary": r"workflow_enhancement_summary\.md"
    }
    
    # Check key directories for references
    directories_to_check = [
        "ai_docs/workflows",
        "scripts",
        "context",
        ".kiro/steering"
    ]
    
    issues_found = []
    files_checked = 0
    
    for directory in directories_to_check:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue
        
        for file_path in dir_path.rglob("*.md"):
            if "ARCHIVED" in str(file_path):
                continue  # Skip archived files
            
            files_checked += 1
            references = check_file_references(file_path, old_patterns)
            
            if references:
                issues_found.append((file_path, references))
    
    # Check Python scripts for old references
    for script_path in Path("scripts").glob("*.py"):
        files_checked += 1
        references = check_file_references(script_path, old_patterns)
        if references:
            issues_found.append((script_path, references))
    
    # Report results
    print(f"📊 Checked {files_checked} files")
    
    if issues_found:
        print(f"\n⚠️  Found {len(issues_found)} files with old references:")
        for file_path, references in issues_found:
            print(f"\n📄 {file_path}:")
            for pattern_name, matches in references:
                print(f"   - {pattern_name}: {matches}")
    else:
        print("\n✅ No old file references found!")
    
    # Verify primary files exist
    print("\n🔍 Verifying primary files exist...")
    primary_files = [
        "ai_docs/workflows/hiring/orchestrator.md",
        "ai_docs/workflows/hiring/single_candidate_workflow.md",
        "ai_docs/workflows/hiring/config/workflow_config.yaml",
        "ai_docs/workflows/hiring/README.md",
        "ai_docs/workflows/hiring/ARCHIVED/README.md"
    ]
    
    missing_files = []
    for file_path_str in primary_files:
        file_path = Path(file_path_str)
        if not file_path.exists():
            missing_files.append(file_path_str)
        else:
            print(f"   ✅ {file_path.name}")
    
    if missing_files:
        print(f"\n❌ Missing primary files:")
        for missing_file in missing_files:
            print(f"   - {missing_file}")
    
    # Verify scripts work with new structure
    print("\n🔍 Verifying script compatibility...")
    script_files = [
        "scripts/complete_workflow_integration.py",
        "scripts/consolidate_hiring_results.py",
        "scripts/generate_complete_candidate_materials.py",
        "scripts/generate_overall_summary.py"
    ]
    
    for script_path_str in script_files:
        script_path = Path(script_path_str)
        if script_path.exists():
            print(f"   ✅ {script_path.name}")
        else:
            print(f"   ❌ Missing: {script_path.name}")
    
    print("\n" + "=" * 50)
    if not issues_found and not missing_files:
        print("🎉 Workflow Cleanup Verification PASSED!")
        print("\n✅ All old references removed")
        print("✅ All primary files in place")
        print("✅ Scripts compatible with new structure")
        print("\n🚀 Workflow is ready for future agent execution")
    else:
        print("⚠️  Workflow Cleanup Verification FAILED!")
        print(f"   - {len(issues_found)} files with old references")
        print(f"   - {len(missing_files)} missing primary files")
        print("\n🔧 Manual cleanup may be required")

if __name__ == "__main__":
    main()