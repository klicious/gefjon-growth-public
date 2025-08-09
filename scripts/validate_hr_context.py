#!/usr/bin/env python3
"""
HR Context validation script for Gefjon Growth
Validates HR automation context completeness and integrity
"""

import yaml
import json
import sys
from pathlib import Path
from typing import List, Dict, Any

class HRContextValidator:
    def __init__(self, project_root: Path = None):
        self.project_root = project_root or Path.cwd()
        self.errors = []
        self.warnings = []
        
    def validate_company_context(self) -> bool:
        """Validate company mission, vision, and values"""
        context_file = self.project_root / "context/company_info/mission_vision_values.yaml"
        
        if not context_file.exists():
            self.errors.append(f"Missing {context_file}")
            return False
        
        try:
            with open(context_file) as f:
                data = yaml.safe_load(f)
            
            # Check required metadata fields
            required_fields = ['id', 'type', 'domain', 'last_updated', 'body']
            missing = [field for field in required_fields if field not in data]
            if missing:
                self.errors.append(f"Missing required fields in {context_file}: {missing}")
            
            # Verify 10 core values are present
            if 'body' in data:
                body = data['body']
                value_count = body.count('| ')
                if value_count < 10:
                    self.warnings.append(f"Only {value_count} core values found in {context_file}, expected 10")
                elif '| 10 |' not in body:
                    self.warnings.append(f"Core value #10 not found in {context_file}")
            
            return len(missing) == 0
            
        except yaml.YAMLError as e:
            self.errors.append(f"YAML syntax error in {context_file}: {e}")
            return False
    
    def validate_team_context(self) -> bool:
        """Validate team composition and requirements"""
        team_file = self.project_root / "context/teams/platform_development_team.yaml"
        
        if not team_file.exists():
            self.errors.append(f"Missing {team_file}")
            return False
        
        try:
            with open(team_file) as f:
                data = yaml.safe_load(f)
            
            # Check for essential team information
            required_sections = ['mission', 'team_composition', 'technology_stack']
            missing = [section for section in required_sections if section not in data]
            if missing:
                self.errors.append(f"Missing required sections in {team_file}: {missing}")
            
            return len(missing) == 0
            
        except yaml.YAMLError as e:
            self.errors.append(f"YAML syntax error in {team_file}: {e}")
            return False
    
    def validate_hiring_process(self) -> bool:
        """Validate hiring process context"""
        hiring_file = self.project_root / "context/hr_processes/hiring/hiring_stages.yaml"
        
        if not hiring_file.exists():
            self.errors.append(f"Missing {hiring_file}")
            return False
        
        try:
            with open(hiring_file) as f:
                data = yaml.safe_load(f)
            
            # Basic validation - file exists and is valid YAML
            if not data:
                self.warnings.append(f"Empty or invalid content in {hiring_file}")
            
            return True
            
        except yaml.YAMLError as e:
            self.errors.append(f"YAML syntax error in {hiring_file}: {e}")
            return False
    
    def validate_candidate_data(self) -> bool:
        """Validate candidate JSON profiles"""
        resume_dir = self.project_root / "data/public/hiring/resume"
        
        if not resume_dir.exists():
            self.warnings.append(f"Resume directory {resume_dir} does not exist")
            return True  # Not required, just a warning
        
        json_files = list(resume_dir.glob("*.json"))
        if not json_files:
            self.warnings.append(f"No candidate JSON files found in {resume_dir}")
            return True
        
        valid_count = 0
        for json_file in json_files:
            try:
                with open(json_file) as f:
                    candidate = json.load(f)
                
                # Check basic required fields
                required_fields = ['candidate_id', 'name']
                missing = [field for field in required_fields if field not in candidate]
                if missing:
                    self.warnings.append(f"Missing fields in {json_file}: {missing}")
                else:
                    valid_count += 1
                    
            except json.JSONDecodeError as e:
                self.errors.append(f"JSON syntax error in {json_file}: {e}")
        
        if json_files:
            self.warnings.append(f"Validated {valid_count}/{len(json_files)} candidate profiles")
        
        return True
    
    def validate_technical_problems(self) -> bool:
        """Validate technical problem bank"""
        problems_dir = self.project_root / "artifacts/public/hiring/pair_programming"
        
        if not problems_dir.exists():
            self.errors.append(f"Missing {problems_dir}")
            return False
        
        required_levels = ['easy.md', 'intermediate.md', 'expert.md']
        missing_levels = []
        
        for level in required_levels:
            level_file = problems_dir / level
            if not level_file.exists():
                missing_levels.append(str(level_file))
            elif level_file.stat().st_size == 0:
                self.warnings.append(f"Empty technical problem file: {level_file}")
        
        if missing_levels:
            self.errors.append(f"Missing technical problem files: {missing_levels}")
            return False
        
        return True
    
    def validate_interview_materials(self) -> bool:
        """Validate interview materials and templates"""
        materials_dir = self.project_root / "artifacts/public/hiring/interview_materials"
        
        if not materials_dir.exists():
            self.errors.append(f"Missing {materials_dir}")
            return False
        
        # Check for BEI guides
        bei_guide = materials_dir / "bei_interview_guide.md"
        bei_questions = materials_dir / "bei_question_bank.md"
        
        if not bei_guide.exists():
            self.warnings.append(f"Missing {bei_guide}")
        
        if not bei_questions.exists():
            self.warnings.append(f"Missing {bei_questions}")
        
        # Check upcoming directory
        upcoming_dir = materials_dir / "upcoming"
        if not upcoming_dir.exists():
            self.warnings.append(f"Missing {upcoming_dir}")
        
        return True
    
    def validate_directory_structure(self) -> bool:
        """Validate overall directory structure"""
        required_dirs = [
            "context/company_info",
            "context/hr_processes/hiring",
            "context/teams",
            "artifacts/public/hiring",
            "artifacts/private",
            "data/public/hiring",
        ]
        
        missing_dirs = []
        for dir_path in required_dirs:
            full_path = self.project_root / dir_path
            if not full_path.exists():
                missing_dirs.append(str(full_path))
        
        if missing_dirs:
            self.errors.append(f"Missing required directories: {missing_dirs}")
            return False
        
        return True
    
    def validate_all(self) -> bool:
        """Run all validation checks"""
        print("🔍 Validating Gefjon Growth HR Context...")
        print("=" * 50)
        
        validations = [
            ("Directory Structure", self.validate_directory_structure),
            ("Company Context", self.validate_company_context),
            ("Team Context", self.validate_team_context),
            ("Hiring Process", self.validate_hiring_process),
            ("Technical Problems", self.validate_technical_problems),
            ("Interview Materials", self.validate_interview_materials),
            ("Candidate Data", self.validate_candidate_data),
        ]
        
        all_passed = True
        for name, validator in validations:
            print(f"Validating {name}...", end=" ")
            try:
                result = validator()
                if result:
                    print("✅ PASS")
                else:
                    print("❌ FAIL")
                    all_passed = False
            except Exception as e:
                print(f"❌ ERROR: {e}")
                all_passed = False
        
        print("=" * 50)
        
        # Report errors and warnings
        if self.errors:
            print("❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
            print()
        
        if all_passed and not self.errors:
            print("✅ All HR context validation checks passed!")
            if self.warnings:
                print(f"⚠️  {len(self.warnings)} warnings noted - consider addressing them.")
        else:
            print("❌ HR context validation failed!")
            print("Please address the errors above before proceeding.")
        
        return all_passed and not self.errors

def main():
    """Main validation function"""
    validator = HRContextValidator()
    success = validator.validate_all()
    
    if success:
        print("\n🎉 Ready for HR automation workflows!")
        sys.exit(0)
    else:
        print("\n🛠️  Please fix the issues and run validation again.")
        sys.exit(1)

if __name__ == "__main__":
    main()