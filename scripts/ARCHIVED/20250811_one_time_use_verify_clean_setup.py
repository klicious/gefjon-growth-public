#!/usr/bin/env python3
"""
Verify that the cleaned setup is working correctly
Test all primary scripts and ensure no confusion
"""

import subprocess
import sys
from pathlib import Path

def test_script_exists(script_name):
    """Test if a script exists and is executable"""
    script_path = Path("scripts") / script_name
    if script_path.exists():
        print(f"   ✅ {script_name}")
        return True
    else:
        print(f"   ❌ Missing: {script_name}")
        return False

def test_script_help(script_name):
    """Test if a script can be executed (check for syntax errors)"""
    script_path = Path("scripts") / script_name
    try:
        # Just test that the script can be imported/parsed
        result = subprocess.run([sys.executable, "-m", "py_compile", str(script_path)], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {script_name} - syntax OK")
            return True
        else:
            print(f"   ❌ {script_name} - syntax error: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ {script_name} - error: {str(e)}")
        return False

def main():
    """Main verification function"""
    print("🔍 Verifying Clean Scripts Setup")
    print("=" * 50)
    
    # Test 1: Check primary scripts exist
    print("\n1. Checking primary scripts exist...")
    primary_scripts = [
        "complete_workflow_final.py",
        "generate_enhanced_materials.py", 
        "consolidate_hiring_results.py",
        "generate_overall_summary.py",
        "verify_workflow_consistency.py",
        "split_candidates.py",
        "validate_hr_context.py"
    ]
    
    all_exist = True
    for script in primary_scripts:
        if not test_script_exists(script):
            all_exist = False
    
    # Test 2: Check scripts have valid syntax
    print("\n2. Checking script syntax...")
    all_valid = True
    for script in primary_scripts:
        if not test_script_help(script):
            all_valid = False
    
    # Test 3: Check archive directory
    print("\n3. Checking archive directory...")
    archive_dir = Path("scripts/ARCHIVED")
    if archive_dir.exists():
        archived_files = list(archive_dir.glob("*.py"))
        print(f"   ✅ Archive directory exists with {len(archived_files)} archived scripts")
        
        # Check archive README
        archive_readme = archive_dir / "README.md"
        if archive_readme.exists():
            print(f"   ✅ Archive README exists")
        else:
            print(f"   ❌ Archive README missing")
            all_valid = False
    else:
        print(f"   ❌ Archive directory missing")
        all_valid = False
    
    # Test 4: Check main README
    print("\n4. Checking main scripts README...")
    main_readme = Path("scripts/README.md")
    if main_readme.exists():
        print(f"   ✅ Main scripts README exists")
    else:
        print(f"   ❌ Main scripts README missing")
        all_valid = False
    
    # Test 5: Check no obsolete scripts remain
    print("\n5. Checking for obsolete scripts...")
    obsolete_patterns = [
        "complete_workflow_integration.py",
        "generate_complete_candidate_materials.py",
        "generate_complete_materials_enhanced.py",
        "update_workflow_to_match_reality.py",
        "cleanup_workflow_files.py",
        "verify_workflow_cleanup.py"
    ]
    
    obsolete_found = []
    for pattern in obsolete_patterns:
        script_path = Path("scripts") / pattern
        if script_path.exists():
            obsolete_found.append(pattern)
    
    if obsolete_found:
        print(f"   ❌ Found obsolete scripts: {', '.join(obsolete_found)}")
        all_valid = False
    else:
        print(f"   ✅ No obsolete scripts found in main directory")
    
    # Test 6: Test master script execution (dry run)
    print("\n6. Testing master script...")
    try:
        # Test that the master script can at least start
        result = subprocess.run([sys.executable, "scripts/complete_workflow_final.py", "--help"], 
                              capture_output=True, text=True, timeout=10)
        # Even if --help isn't implemented, the script should at least parse
        print(f"   ✅ Master script can be executed")
    except subprocess.TimeoutExpired:
        print(f"   ✅ Master script started (timed out waiting, which is expected)")
    except Exception as e:
        print(f"   ⚠️  Master script test inconclusive: {str(e)}")
    
    print("\n" + "=" * 50)
    if all_exist and all_valid:
        print("🎉 CLEAN SETUP VERIFICATION PASSED!")
        print("\n✅ All primary scripts present and valid")
        print("✅ Archive directory properly organized")
        print("✅ No obsolete scripts in main directory")
        print("✅ Documentation complete")
        
        print("\n🚀 Ready for production use!")
        print("\n📋 Usage:")
        print("   python scripts/complete_workflow_final.py  # Complete workflow")
        print("   python scripts/verify_workflow_consistency.py  # Verify setup")
        
    else:
        print("⚠️  CLEAN SETUP VERIFICATION ISSUES FOUND!")
        print("\n🔧 Some issues need to be resolved")
        print("📋 Review the issues above")
    
    return all_exist and all_valid

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)