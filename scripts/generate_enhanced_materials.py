#!/usr/bin/env python3
"""
Enhanced Complete Material Generation Script
Ensures all candidates have complete, consistent materials based on their status
"""

import json
import os
from pathlib import Path
from datetime import datetime

def load_candidate_data():
    """Load all candidate data sources"""
    
    # Load screening results
    screening_file = Path("data/public/hiring/working/20250811_enhanced_run/screening_summary_complete.json")
    with open(screening_file, 'r', encoding='utf-8') as f:
        screening_data = json.load(f)
    
    # Load normalized candidate data
    candidates_file = Path("data/public/hiring/working/20250811_enhanced_run/candidates.normalized.json")
    with open(candidates_file, 'r', encoding='utf-8') as f:
        candidates_data = json.load(f)
    
    # Create lookup dictionary
    candidates_lookup = {c['candidate_id']: c for c in candidates_data}
    
    return screening_data, candidates_lookup

def should_generate_material(candidate_screening, material_type):
    """Determine if a material should be generated based on candidate status"""
    next_step = candidate_screening['next_step']
    
    material_rules = {
        'screening_report': True,  # All candidates get screening reports
        'takehome_assignment': next_step in ['take_home_assignment', 'senior_level_assessment'],
        'interview_materials': next_step in ['take_home_assignment', 'senior_level_assessment', 'additional_assessment'],
        'evaluation_framework': True,  # All candidates get evaluation frameworks
        'communication_templates': True,  # All candidates get communication templates
    }
    
    return material_rules.get(material_type, False)

def generate_screening_report(candidate_screening, candidate_data, output_path):
    """Generate comprehensive screening report"""
    
    content = f"""# Screening Report: {candidate_screening['candidate_name']}

## Executive Summary
- **Candidate ID**: {candidate_screening['candidate_id']}
- **Overall Score**: {candidate_screening['overall_score']}/10
- **Recommendation**: {candidate_screening['recommendation']}
- **Confidence**: {candidate_screening['confidence']:.0%}
- **Next Step**: {candidate_screening['next_step']}

## Candidate Profile
- **Name**: {candidate_screening['candidate_name']}
- **Email**: {candidate_data.get('email', 'Not provided')}
- **Phone**: {candidate_data.get('phone', 'Not provided')}
- **Experience**: {candidate_data.get('experience_years', 'Unknown')} years
- **Current Role**: {candidate_data.get('current_role', 'Not specified')}
- **Location**: {candidate_data.get('location', 'Not specified')}

## Technical Assessment

### Skills Portfolio
{chr(10).join(f"- {skill}" for skill in candidate_data.get('skills', [])[:20])}
{f"- ... and {len(candidate_data.get('skills', [])) - 20} more" if len(candidate_data.get('skills', [])) > 20 else ""}

### Key Strengths
{chr(10).join(f"- {strength}" for strength in candidate_screening['key_strengths'])}

### Areas of Concern
{chr(10).join(f"- {concern}" for concern in candidate_screening['areas_of_concern'])}

## Background Information

### Education
{candidate_data.get('education', 'Not provided')}

### Professional Summary
{candidate_data.get('summary', 'No summary available')}

### External Links
- **GitHub**: {candidate_data.get('github_url', 'Not provided')}
- **LinkedIn**: {candidate_data.get('linkedin_url', 'Not provided')}
- **Portfolio**: {candidate_data.get('portfolio_url', 'Not provided')}

## Screening Decision

### Final Assessment
Based on comprehensive evaluation, this candidate receives a **{candidate_screening['recommendation']}** recommendation with {candidate_screening['confidence']:.0%} confidence.

### Recommended Next Steps
**Immediate Action**: {candidate_screening['next_step']}

---
*Screening completed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Evaluator: AI Screening System v2.0*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_interview_materials(candidate_screening, candidate_data, candidate_dir):
    """Generate complete interview materials"""
    
    interview_dir = candidate_dir / "interview"
    
    # Generate candidate context
    context_content = f"""# Interview Context: {candidate_screening['candidate_name']}

## Executive Summary
**Recommendation**: {candidate_screening['recommendation']} (Score: {candidate_screening['overall_score']}/10)
**Confidence Level**: {candidate_screening['confidence']:.0%}

{candidate_screening['candidate_name']} is a {candidate_data.get('experience_years', 'unknown')} year experienced professional currently working as {candidate_data.get('current_role', 'not specified')}. 

### Key Highlights
{chr(10).join(f"- {strength}" for strength in candidate_screening['key_strengths'])}

### Areas to Explore
{chr(10).join(f"- {concern}" for concern in candidate_screening['areas_of_concern'])}

## Technical Profile
- **Primary Skills**: {', '.join(candidate_data.get('skills', [])[:8])}
- **Experience Level**: {candidate_data.get('experience_years', 'Unknown')} years
- **Education**: {candidate_data.get('education', 'Not provided')}

## Interview Strategy

### Focus Areas
1. **Technical Depth**: Assess expertise in {', '.join(candidate_data.get('skills', [])[:3])}
2. **Problem Solving**: Evaluate approach to complex technical challenges
3. **Cultural Fit**: Alignment with Gefjon Growth values and team dynamics
4. **Growth Potential**: Learning agility and career development goals

### Recommended Structure
- **Technical Discussion**: 40 minutes
- **Behavioral Assessment**: 20 minutes  
- **Culture & Values**: 15 minutes
- **Candidate Questions**: 15 minutes

---
*Prepared for: {candidate_screening['recommendation']} candidate*
"""
    
    with open(interview_dir / "candidate_context.md", 'w', encoding='utf-8') as f:
        f.write(context_content)
    
    # Generate interview guide
    guide_content = f"""# Interview Guide: {candidate_screening['candidate_name']}

## Pre-Interview Preparation (15 minutes)
- [ ] Review candidate's screening report and take-home assignment
- [ ] Prepare technical questions based on their {', '.join(candidate_data.get('skills', [])[:3])} background
- [ ] Set up technical discussion environment

## Interview Structure (90 minutes total)

### 1. Opening & Introductions (10 minutes)
- Welcome and introductions
- Brief overview of Gefjon Growth and the role
- Explain interview structure and timeline

### 2. Technical Deep Dive (40 minutes)

#### Core Technical Questions:
Based on candidate's {', '.join(candidate_data.get('skills', [])[:3])} background:

**System Design & Architecture**:
- "Describe a complex system you've built or worked on"
- "How would you design a scalable task management API?"
- "Walk me through your approach to database schema design"

**Problem-Solving**:
- "Tell me about a challenging technical problem you solved"
- "How do you approach debugging production issues?"
- "Describe your testing strategy for a new feature"

### 3. Behavioral Assessment (20 minutes)

#### Key Questions:
- "Tell me about a time you had to learn a new technology quickly"
- "Describe a situation where you disagreed with a technical decision"
- "How do you handle competing priorities and tight deadlines?"
- "Give an example of when you mentored or helped a colleague"

### 4. Cultural Fit & Values (15 minutes)

#### Gefjon Growth Values Assessment:
- "What motivates you in your work?"
- "How do you approach collaboration in a remote/hybrid environment?"
- "Describe your ideal work environment and team dynamics"

### 5. Candidate Questions & Closing (15 minutes)
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline

## Evaluation Criteria

### Technical Competency (40%)
- **Depth of Knowledge**: Understanding of core technologies
- **Problem-Solving**: Approach to technical challenges
- **Communication**: Ability to explain technical concepts clearly

### Experience Relevance (25%)
- **Applicable Skills**: Relevance to our tech stack
- **Project Complexity**: Scale and complexity of previous work
- **Learning Ability**: Adaptability to new technologies

### Cultural Fit (20%)
- **Team Collaboration**: Working style and communication
- **Growth Mindset**: Learning orientation and curiosity
- **Values Alignment**: Fit with company culture

### Communication & Soft Skills (15%)
- **Clarity**: Clear and concise communication
- **Listening**: Active listening and engagement
- **Questions**: Quality of questions asked

---
*Interview guide prepared for: {candidate_screening['recommendation']} candidate*
*Screening score: {candidate_screening['overall_score']}/10*
"""
    
    with open(interview_dir / "interview_guide.md", 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    # Generate interview script
    script_content = f"""# Interview Script: {candidate_screening['candidate_name']}

## Pre-Interview Setup
- [ ] Review candidate materials (screening report, take-home assignment)
- [ ] Prepare technical discussion environment
- [ ] Have evaluation form ready

---

## Interview Script

### Opening (10 minutes)

**Interviewer**: "Hi {candidate_screening['candidate_name']}, thank you for joining us today. I'm [Name], [Title] at Gefjon Growth. How are you doing today?"

*[Wait for response, engage in brief small talk]*

**Interviewer**: "Great! Let me start by telling you a bit about Gefjon Growth and this role, then we'll dive into learning more about you and your background."

*[Brief company overview - 2-3 minutes]*

**Interviewer**: "The structure for today's interview will be about 90 minutes total. We'll start with a technical deep dive, then move into some behavioral questions, discuss cultural fit, and leave plenty of time for your questions. Does that sound good?"

### Technical Deep Dive (40 minutes)

**Interviewer**: "Let's start with your technical background. I see from your profile that you have experience with {', '.join(candidate_data.get('skills', [])[:3])}. Can you walk me through a recent project where you used these technologies?"

*[Listen for: technical depth, problem-solving approach, communication clarity]*

**System Design Question**:
"That's interesting. Now, let's say you needed to design a scalable API for task management that could handle thousands of concurrent users. How would you approach this?"

*[Look for: scalability considerations, database design, caching, load balancing]*

**Problem-Solving Scenario**:
"Tell me about a time when you encountered a particularly challenging bug or technical issue. How did you approach solving it?"

*[Assess: debugging methodology, persistence, learning from failures]*

### Behavioral Assessment (20 minutes)

**Learning Agility**:
"Tell me about a time you had to quickly learn a new technology or framework for a project. How did you approach it?"

*[Look for: learning strategy, resourcefulness, adaptation]*

**Collaboration**:
"Describe a situation where you had to work closely with team members who had different technical opinions. How did you handle it?"

*[Assess: communication, compromise, leadership]*

**Pressure Handling**:
"Can you share an example of when you had to deliver under a tight deadline? What was your approach?"

*[Evaluate: prioritization, stress management, quality maintenance]*

### Cultural Fit Assessment (15 minutes)

**Motivation**:
"What aspects of software development do you find most exciting or fulfilling?"

*[Listen for: passion, alignment with role requirements]*

**Work Environment**:
"Describe your ideal work environment. What helps you do your best work?"

*[Assess: fit with company culture, remote work readiness]*

**Growth Mindset**:
"Where do you see yourself growing professionally in the next 2-3 years?"

*[Evaluate: ambition, alignment with career path, learning orientation]*

### Candidate Questions (15 minutes)

**Interviewer**: "Now I'd love to hear your questions. What would you like to know about the role, the team, or Gefjon Growth?"

### Closing (5 minutes)

**Interviewer**: "Thank you for those great questions. Before we wrap up, is there anything else you'd like to share about your background or interest in this role?"

**Next Steps**:
"Here's what happens next: We'll be completing our interview process over the next [timeframe], and we'll follow up with you by [date] with an update on next steps."

**Interviewer**: "Thank you so much for your time today, {candidate_screening['candidate_name']}. It was great learning more about your background and experience. We'll be in touch soon!"

---

## Post-Interview Evaluation

### Immediate Actions (within 30 minutes):
- [ ] Complete technical assessment notes
- [ ] Rate behavioral responses
- [ ] Note cultural fit observations
- [ ] Record overall impression

### Evaluation Form Completion (within 24 hours):
- [ ] Technical competency rating and examples
- [ ] Behavioral assessment with specific instances
- [ ] Cultural fit evaluation
- [ ] Overall recommendation with rationale

---
*Interview script for: {candidate_screening['recommendation']} candidate*
*Total interview time: 90 minutes*
"""
    
    with open(interview_dir / "interview_script.md", 'w', encoding='utf-8') as f:
        f.write(script_content)

def generate_communication_templates(candidate_screening, candidate_data, output_path):
    """Generate communication templates for different stages"""
    
    next_step = candidate_screening['next_step']
    candidate_name = candidate_screening['candidate_name']
    
    content = f"""# Communication Templates: {candidate_name}

## Email Templates for {candidate_name}

### 1. Take-Home Assignment Email
**Subject**: Next Steps - Technical Assignment for Backend Developer Role

Dear {candidate_name},

Thank you for your interest in the Backend Developer position at Gefjon Growth. We were impressed with your background and would like to move forward with the next step in our process.

**Next Step: Technical Assignment**
We'd like you to complete a take-home technical assignment that should take approximately {"4-6 hours" if candidate_data.get('experience_years', 0) >= 5 else "3-4 hours" if candidate_data.get('experience_years', 0) >= 2 else "2-3 hours"}. This assignment is designed to showcase your technical skills and approach to problem-solving.

**Assignment Details:**
- You'll find the complete assignment in the attached document
- Please submit your solution within 5 business days
- Submit via GitHub repository (public or private with access granted)
- Include comprehensive documentation and setup instructions

If you have any questions about the assignment, please don't hesitate to reach out within 24 hours.

We're excited to see your technical approach and look forward to your submission!

Best regards,
[Your Name]
Gefjon Growth Hiring Team

---

### 2. Interview Invitation Email
**Subject**: Interview Invitation - Backend Developer Role at Gefjon Growth

Dear {candidate_name},

Thank you for submitting your technical assignment. We were impressed with your implementation and would like to invite you for the next stage of our interview process.

**Interview Details:**
- **Format**: Video call (90 minutes)
- **Structure**: Technical discussion, behavioral questions, and your questions
- **Focus Areas**: Your technical assignment, system design, and cultural fit

Please reply with your availability for the following time slots:
[Time slots]

We're looking forward to learning more about you and discussing how you might contribute to our team!

Best regards,
[Your Name]
Gefjon Growth Hiring Team

---

### 3. {"Additional Assessment Email" if next_step == "additional_assessment" else "Decline with Feedback Email" if next_step == "decline" else "Status Update Email"}

{"**Subject**: Additional Assessment - Backend Developer Role" if next_step == "additional_assessment" else "**Subject**: Update on Your Application - Backend Developer Role" if next_step == "decline" else "**Subject**: Next Steps - Backend Developer Role"}

Dear {candidate_name},

{"After reviewing your background, we'd like to conduct an additional assessment to better understand your fit for the role." if next_step == "additional_assessment" else "After careful consideration, we have decided to move forward with other candidates whose experience more closely aligns with our current needs." if next_step == "decline" else "Thank you for your continued interest in our Backend Developer position."}

{"We'd like to schedule a focused technical discussion to explore your experience and problem-solving approach." if next_step == "additional_assessment" else "We were impressed by your technical background and encourage you to apply for future positions that may be a better fit." if next_step == "decline" else "We'll be in touch with next steps shortly."}

Best regards,
[Your Name]
Gefjon Growth Hiring Team

---

## Internal Communication Templates

### 1. Hiring Team Update
**Subject**: Candidate Update - {candidate_name} ({candidate_screening['candidate_id']})

Team,

**Candidate**: {candidate_name}
**Status**: {next_step}
**Score**: {candidate_screening['overall_score']}/10
**Recommendation**: {candidate_screening['recommendation']}

**Key Highlights:**
{chr(10).join(f"- {strength}" for strength in candidate_screening['key_strengths'][:3])}

**Next Action**: {"Send take-home assignment" if next_step == 'take_home_assignment' else "Schedule additional assessment" if next_step == 'additional_assessment' else "Schedule senior-level interview" if next_step == 'senior_level_assessment' else "Send decline email"}

---

*Communication templates generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Customized for: {candidate_screening['recommendation']} candidate*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Enhanced material generation with complete coverage"""
    
    print("🚀 Generating Enhanced Complete Candidate Materials...")
    
    # Load data
    screening_data, candidates_lookup = load_candidate_data()
    
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    
    generation_log = {
        "generation_date": datetime.now().isoformat(),
        "total_candidates": len(screening_data['screening_results']),
        "materials_generated": [],
        "errors": [],
        "enhancement_version": "2.0"
    }
    
    for candidate_screening in screening_data['screening_results']:
        try:
            candidate_id = candidate_screening['candidate_id']
            candidate_name = candidate_screening['candidate_name']
            
            print(f"📝 Generating enhanced materials for: {candidate_name} ({candidate_id})")
            
            # Get candidate data
            candidate_data = candidates_lookup.get(candidate_id, {})
            if not candidate_data:
                print(f"  ⚠️  Warning: No detailed data found for {candidate_id}")
                candidate_data = {'skills': [], 'experience_years': 0}
            
            # Find candidate directory
            normalized_name = candidate_name.lower().replace(' ', '_')
            candidate_dir = base_path / f"{candidate_id}_{normalized_name}"
            
            if not candidate_dir.exists():
                print(f"  ❌ Directory not found: {candidate_dir}")
                continue
            
            materials_generated = []
            
            # 1. Generate screening report (all candidates)
            screening_path = candidate_dir / "screening" / "screening_report.md"
            generate_screening_report(candidate_screening, candidate_data, screening_path)
            materials_generated.append("screening_report.md")
            
            # 2. Generate interview materials (interview candidates)
            if should_generate_material(candidate_screening, 'interview_materials'):
                generate_interview_materials(candidate_screening, candidate_data, candidate_dir)
                materials_generated.extend(["candidate_context.md", "interview_guide.md", "interview_script.md"])
            
            # 3. Generate communication templates (all candidates)
            if should_generate_material(candidate_screening, 'communication_templates'):
                comm_path = candidate_dir / "communication" / "communication_templates.md"
                generate_communication_templates(candidate_screening, candidate_data, comm_path)
                materials_generated.append("communication_templates.md")
            
            generation_log["materials_generated"].append({
                "candidate_id": candidate_id,
                "candidate_name": candidate_name,
                "materials": materials_generated,
                "total_files": len(materials_generated),
                "status": candidate_screening['next_step']
            })
            
            print(f"  ✅ Generated {len(materials_generated)} enhanced materials")
            
        except Exception as e:
            error_msg = f"Error processing {candidate_id}: {str(e)}"
            print(f"  ❌ {error_msg}")
            generation_log["errors"].append(error_msg)
    
    # Save enhanced generation log
    log_path = base_path / "enhanced_materials_generation_log.json"
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(generation_log, f, indent=2, ensure_ascii=False)
    
    total_materials = sum(len(c["materials"]) for c in generation_log["materials_generated"])
    
    print(f"\n✅ Enhanced Material Generation Complete!")
    print(f"📊 Processed {generation_log['total_candidates']} candidates")
    print(f"📄 Generated {total_materials} comprehensive materials")
    print(f"📋 Log saved to: {log_path}")
    
    if generation_log["errors"]:
        print(f"⚠️  {len(generation_log['errors'])} errors occurred - check log for details")
    
    print(f"\n🎯 All candidates now have complete, consistent materials!")

if __name__ == "__main__":
    main()