#!/usr/bin/env python3
"""
Generate complete candidate materials for all candidates
Fills in missing documents based on candidate data and status
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

def generate_screening_report(candidate_screening, candidate_data, output_path):
    """Generate detailed screening report"""
    
    content = f"""# Screening Report: {candidate_screening['candidate_name']}

## Candidate Overview
- **Candidate ID**: {candidate_screening['candidate_id']}
- **Name**: {candidate_screening['candidate_name']}
- **Email**: {candidate_data.get('email', 'Not provided')}
- **Phone**: {candidate_data.get('phone', 'Not provided')}
- **Experience**: {candidate_data.get('experience_years', 'Unknown')} years
- **Current Role**: {candidate_data.get('current_role', 'Not specified')}
- **Location**: {candidate_data.get('location', 'Not specified')}

## Screening Results
- **Overall Score**: {candidate_screening['overall_score']}/10
- **Recommendation**: {candidate_screening['recommendation']}
- **Confidence Level**: {candidate_screening['confidence']:.0%}
- **Next Step**: {candidate_screening['next_step']}

## Technical Skills Assessment
{chr(10).join(f"- {skill}" for skill in candidate_data.get('skills', [])[:15])}
{f"- ... and {len(candidate_data.get('skills', [])) - 15} more" if len(candidate_data.get('skills', [])) > 15 else ""}

## Key Strengths
{chr(10).join(f"- {strength}" for strength in candidate_screening['key_strengths'])}

## Areas of Concern
{chr(10).join(f"- {concern}" for concern in candidate_screening['areas_of_concern'])}

## Education Background
{candidate_data.get('education', 'Not provided')}

## Professional Summary
{candidate_data.get('summary', 'No summary available')}

## Links and Portfolio
- **GitHub**: {candidate_data.get('github_url', 'Not provided')}
- **LinkedIn**: {candidate_data.get('linkedin_url', 'Not provided')}
- **Portfolio**: {candidate_data.get('portfolio_url', 'Not provided')}

## Screening Decision
Based on the comprehensive evaluation, this candidate receives a **{candidate_screening['recommendation']}** recommendation with {candidate_screening['confidence']:.0%} confidence.

**Rationale**: The candidate demonstrates {', '.join(candidate_screening['key_strengths'][:2])} but requires attention to {', '.join(candidate_screening['areas_of_concern'][:2])}.

---
*Screening completed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Next step: {candidate_screening['next_step']}*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_takehome_assignment(candidate_screening, candidate_data, output_path):
    """Generate take-home assignment based on candidate level and skills"""
    
    # Determine assignment level based on experience and score
    experience = candidate_data.get('experience_years', 0)
    score = candidate_screening['overall_score']
    
    if experience >= 5 or score >= 9.0:
        level = "Senior"
        complexity = "Advanced"
    elif experience >= 2 or score >= 7.5:
        level = "Mid-Level"
        complexity = "Intermediate"
    else:
        level = "Entry-Level"
        complexity = "Basic"
    
    # Check if candidate has specific skills
    skills = candidate_data.get('skills', [])
    has_python = any('python' in skill.lower() for skill in skills)
    has_aws = any('aws' in skill.lower() for skill in skills)
    has_docker = any('docker' in skill.lower() or 'kubernetes' in skill.lower() for skill in skills)
    
    content = f"""# Take-Home Assignment: {candidate_screening['candidate_name']}

## Assignment Overview
- **Candidate**: {candidate_screening['candidate_name']} ({candidate_screening['candidate_id']})
- **Level**: {level} ({complexity} complexity)
- **Estimated Time**: {"4-6 hours" if level == "Senior" else "3-4 hours" if level == "Mid-Level" else "2-3 hours"}
- **Due Date**: 5 business days from assignment date

## Technical Requirements

### Core Task: Backend API Development
Build a RESTful API service for a simplified task management system.

#### Functional Requirements:
1. **User Management**
   - User registration and authentication
   - JWT token-based authorization

2. **Task Management**
   - Create, read, update, delete tasks
   - Task categories and priorities
   - Task assignment to users

3. **Data Persistence**
   - Use PostgreSQL or MySQL database
   - Proper database schema design
   - Database migrations

#### Technical Stack Requirements:
- **Backend**: {"Python (FastAPI/Django)" if has_python else "Java (Spring Boot) or Python (FastAPI)"}
- **Database**: PostgreSQL or MySQL
- **Authentication**: JWT tokens
- **Documentation**: API documentation (Swagger/OpenAPI)

### {level}-Specific Requirements:

"""
    
    if level == "Senior":
        content += """#### Advanced Requirements:
- **Microservices Architecture**: Split into user service and task service
- **Caching**: Implement Redis caching for frequently accessed data
- **Message Queue**: Use RabbitMQ or Kafka for async task processing
- **Monitoring**: Add health checks and metrics endpoints
- **Containerization**: Docker containers with docker-compose
- **CI/CD**: GitHub Actions or GitLab CI pipeline
- **Load Testing**: Include performance testing with results
- **Security**: Rate limiting, input validation, SQL injection prevention

"""
    elif level == "Mid-Level":
        content += """#### Intermediate Requirements:
- **API Testing**: Comprehensive unit and integration tests
- **Error Handling**: Proper HTTP status codes and error responses
- **Logging**: Structured logging with different log levels
- **Configuration**: Environment-based configuration management
- **Containerization**: Docker container with Dockerfile
- **Database Optimization**: Proper indexing and query optimization
- **Input Validation**: Request validation and sanitization

"""
    else:
        content += """#### Basic Requirements:
- **API Testing**: Basic unit tests for core functionality
- **Error Handling**: Basic error responses and validation
- **Code Quality**: Clean, readable code with comments
- **Documentation**: README with setup and usage instructions
- **Database Design**: Proper table relationships and constraints
- **Basic Security**: Password hashing and basic input validation

"""
    
    content += f"""## Evaluation Criteria

### Technical Implementation (40%)
- Code quality and organization
- Proper use of frameworks and libraries
- Database design and optimization
- API design and RESTful principles

### Functionality (30%)
- All required features implemented
- Proper error handling
- Edge case handling
- User experience considerations

### Testing & Documentation (20%)
- Test coverage and quality
- API documentation completeness
- README and setup instructions
- Code comments and clarity

### {"Advanced Features (10%)" if level == "Senior" else "Best Practices (10%)"}
- {"Architecture decisions and scalability" if level == "Senior" else "Security implementation"}
- {"Performance optimization" if level == "Senior" else "Code organization"}
- {"DevOps practices" if level == "Senior" else "Error handling"}

## Submission Requirements

### Deliverables:
1. **Source Code**: Complete project in a Git repository
2. **Documentation**: 
   - README with setup instructions
   - API documentation
   - Architecture decisions (for Senior level)
3. **Database**: 
   - Schema file or migrations
   - Sample data (optional)
4. **Tests**: 
   - Test files with instructions to run
   - Test coverage report (for Mid/Senior level)

### Submission Format:
- **GitHub Repository**: Public or private repository with access granted
- **Live Demo**: {"Required" if level == "Senior" else "Optional but preferred"}
- **Video Walkthrough**: {"Required (5-10 minutes)" if level == "Senior" else "Optional (3-5 minutes)"}

## Additional Notes

### Candidate-Specific Considerations:
Based on your background in {', '.join(skills[:3])}, feel free to leverage your expertise while meeting the core requirements.

### Questions and Clarifications:
If you have any questions about the requirements, please reach out within 24 hours of receiving this assignment.

### Evaluation Timeline:
- **Assignment Sent**: [Date]
- **Due Date**: [Date + 5 business days]
- **Evaluation Complete**: [Date + 7 business days]
- **Feedback Provided**: [Date + 8 business days]

---
*Assignment generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Customized for: {level} level candidate with {candidate_screening['overall_score']}/10 screening score*
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

{candidate_screening['candidate_name']} is a {candidate_data.get('experience_years', 'unknown')} year experienced professional currently working as {candidate_data.get('current_role', 'not specified')}. 

**Key Highlights**:
{chr(10).join(f"- {strength}" for strength in candidate_screening['key_strengths'])}

**Areas to Explore**:
{chr(10).join(f"- {concern}" for concern in candidate_screening['areas_of_concern'])}

## Technical Background
- **Primary Skills**: {', '.join(candidate_data.get('skills', [])[:8])}
- **Experience Level**: {candidate_data.get('experience_years', 'Unknown')} years
- **Education**: {candidate_data.get('education', 'Not provided')}

## Interview Focus Areas
1. **Technical Depth**: Assess expertise in {', '.join(candidate_data.get('skills', [])[:3])}
2. **Problem Solving**: Evaluate approach to complex technical challenges
3. **Cultural Fit**: Alignment with Gefjon Growth values and team dynamics
4. **Growth Potential**: Learning agility and career development goals

## Recommended Interview Structure
- **Technical Discussion**: 40 minutes
- **Behavioral Questions**: 20 minutes  
- **Culture & Values**: 15 minutes
- **Candidate Questions**: 15 minutes
"""
    
    with open(interview_dir / "candidate_context.md", 'w', encoding='utf-8') as f:
        f.write(context_content)
    
    # Generate interview guide
    guide_content = f"""# Interview Guide: {candidate_screening['candidate_name']}

## Pre-Interview Preparation
- Review candidate's screening report and take-home assignment
- Prepare technical questions based on their {', '.join(candidate_data.get('skills', [])[:3])} background
- Set up technical discussion environment (whiteboard/screen sharing)

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

**Technology-Specific** (choose based on candidate skills):
{chr(10).join(f"- Questions about {skill}" for skill in candidate_data.get('skills', [])[:5])}

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
- "What are your thoughts on work-life balance?"

### 5. Candidate Questions & Closing (15 minutes)
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline
- Thank candidate for their time

## Evaluation Criteria

### Technical Competency (40%)
- **Depth of Knowledge**: Understanding of core technologies
- **Problem-Solving**: Approach to technical challenges
- **Communication**: Ability to explain technical concepts clearly
- **Best Practices**: Knowledge of industry standards and patterns

### Experience Relevance (25%)
- **Applicable Skills**: Relevance to our tech stack
- **Project Complexity**: Scale and complexity of previous work
- **Learning Ability**: Adaptability to new technologies
- **Impact**: Measurable contributions in previous roles

### Cultural Fit (20%)
- **Team Collaboration**: Working style and communication
- **Growth Mindset**: Learning orientation and curiosity
- **Values Alignment**: Fit with company culture
- **Motivation**: Genuine interest in role and company

### Communication & Soft Skills (15%)
- **Clarity**: Clear and concise communication
- **Listening**: Active listening and engagement
- **Questions**: Quality of questions asked
- **Professionalism**: Overall interview presence

## Red Flags to Watch For
- Inability to explain previous work in detail
- Poor communication or unclear explanations
- Lack of curiosity or questions about the role
- Inconsistencies with resume or screening information
- Negative attitude toward previous employers or colleagues

## Positive Indicators
- Clear explanations of technical concepts
- Thoughtful questions about the role and company
- Examples of continuous learning and growth
- Collaborative approach to problem-solving
- Enthusiasm for the opportunity

## Post-Interview Actions
1. Complete evaluation form within 24 hours
2. Provide specific examples and feedback
3. Make clear hire/no-hire recommendation
4. Share feedback with hiring team
5. Schedule debrief if needed

---
*Interview guide prepared for: {candidate_screening['recommendation']} candidate*
*Screening score: {candidate_screening['overall_score']}/10*
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open(interview_dir / "interview_guide.md", 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    # Generate interview script
    script_content = f"""# Interview Script: {candidate_screening['candidate_name']}

## Pre-Interview Setup
- [ ] Review candidate materials (screening report, take-home assignment)
- [ ] Prepare technical discussion environment
- [ ] Have evaluation form ready
- [ ] Test video/audio setup

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

**Follow-up questions based on response:**

**System Design Question**:
"That's interesting. Now, let's say you needed to design a scalable API for task management that could handle thousands of concurrent users. How would you approach this?"

*[Look for: scalability considerations, database design, caching, load balancing]*

**Problem-Solving Scenario**:
"Tell me about a time when you encountered a particularly challenging bug or technical issue. How did you approach solving it?"

*[Assess: debugging methodology, persistence, learning from failures]*

**Technology Deep Dive** (choose based on candidate's strongest skills):
{chr(10).join(f"- 'I see you have experience with {skill}. Can you describe a specific challenge you solved using this technology?'" for skill in candidate_data.get('skills', [])[:3])}

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

*[Common topics candidates ask about:]*
- Team structure and collaboration
- Technology stack and development practices
- Growth opportunities and career development
- Company culture and values
- Work-life balance and remote work policies
- Next steps in the process

### Closing (5 minutes)

**Interviewer**: "Thank you for those great questions. Before we wrap up, is there anything else you'd like to share about your background or interest in this role?"

**Next Steps**:
"Here's what happens next: We'll be completing our interview process over the next [timeframe], and we'll follow up with you by [date] with an update on next steps. Do you have any questions about the timeline or process?"

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
- [ ] Feedback for candidate development

### Key Evaluation Questions:
1. Can this candidate succeed in our technical environment?
2. Will they collaborate effectively with our team?
3. Do they demonstrate growth potential?
4. Are they genuinely interested in this opportunity?
5. What are the biggest strengths and concerns?

---
*Interview script for: {candidate_screening['recommendation']} candidate*
*Preparation time: 15-20 minutes*
*Total interview time: 90 minutes*
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open(interview_dir / "interview_script.md", 'w', encoding='utf-8') as f:
        f.write(script_content)

def generate_evaluation_framework(candidate_screening, candidate_data, output_path):
    """Generate evaluation framework for final decision"""
    
    content = f"""# Evaluation Framework: {candidate_screening['candidate_name']}

## Candidate Summary
- **Name**: {candidate_screening['candidate_name']} ({candidate_screening['candidate_id']})
- **Screening Score**: {candidate_screening['overall_score']}/10
- **Screening Recommendation**: {candidate_screening['recommendation']}
- **Experience Level**: {candidate_data.get('experience_years', 'Unknown')} years

## Evaluation Stages Completed

### ✅ Stage 1: Initial Screening
- **Score**: {candidate_screening['overall_score']}/10
- **Recommendation**: {candidate_screening['recommendation']}
- **Key Strengths**: {'; '.join(candidate_screening['key_strengths'])}
- **Areas of Concern**: {'; '.join(candidate_screening['areas_of_concern'])}

### 📋 Stage 2: Take-Home Assignment
- **Status**: {"Assigned" if candidate_screening['next_step'] == 'take_home_assignment' else "Not Required"}
- **Assignment Level**: {"Senior" if candidate_data.get('experience_years', 0) >= 5 else "Mid-Level" if candidate_data.get('experience_years', 0) >= 2 else "Entry-Level"}
- **Evaluation Score**: _[To be completed]_
- **Technical Assessment**: _[To be completed]_
- **Code Quality**: _[To be completed]_
- **Documentation**: _[To be completed]_

### 📋 Stage 3: Technical Interview
- **Status**: {"Scheduled" if candidate_screening['next_step'] in ['take_home_assignment', 'senior_level_assessment'] else "Pending"}
- **Technical Competency**: _[To be completed]_
- **Problem-Solving**: _[To be completed]_
- **Communication**: _[To be completed]_
- **Cultural Fit**: _[To be completed]_

## Final Decision Framework

### Scoring Matrix (Total: 100 points)

#### Technical Competency (40 points)
- **Screening Assessment**: {candidate_screening['overall_score'] * 4:.1f}/40
- **Take-Home Assignment**: _[0-40 points]_
- **Interview Performance**: _[0-40 points]_
- **Average Technical Score**: _[To be calculated]_

#### Experience & Skills Relevance (25 points)
- **Years of Experience**: {min(candidate_data.get('experience_years', 0) * 5, 25):.1f}/25
- **Skill Stack Match**: _[To be assessed]_
- **Project Complexity**: _[To be assessed]_

#### Cultural Fit & Soft Skills (20 points)
- **Team Collaboration**: _[To be assessed]_
- **Communication Skills**: _[To be assessed]_
- **Growth Mindset**: _[To be assessed]_
- **Values Alignment**: _[To be assessed]_

#### Potential & Motivation (15 points)
- **Learning Agility**: _[To be assessed]_
- **Career Goals Alignment**: _[To be assessed]_
- **Enthusiasm for Role**: _[To be assessed]_

### Decision Thresholds
- **Strong Hire**: 85+ points
- **Hire**: 70-84 points
- **Lean Hire**: 60-69 points (requires additional assessment)
- **No Hire**: <60 points

## Risk Assessment

### Potential Risks
{chr(10).join(f"- {concern}" for concern in candidate_screening['areas_of_concern'])}

### Mitigation Strategies
- _[To be defined based on interview results]_
- _[Training and development plans]_
- _[Mentorship and support structures]_

## Recommendation Rationale

### Current Status: {candidate_screening['recommendation']}
Based on initial screening, this candidate shows {candidate_screening['recommendation'].lower()} potential due to:

**Strengths**:
{chr(10).join(f"- {strength}" for strength in candidate_screening['key_strengths'])}

**Development Areas**:
{chr(10).join(f"- {concern}" for concern in candidate_screening['areas_of_concern'])}

### Final Recommendation: _[To be completed after all stages]_

## Next Steps
1. **Immediate**: {"Complete take-home assignment evaluation" if candidate_screening['next_step'] == 'take_home_assignment' else "Schedule additional assessment" if candidate_screening['next_step'] == 'additional_assessment' else "Proceed with senior-level evaluation" if candidate_screening['next_step'] == 'senior_level_assessment' else "Provide decline feedback"}
2. **Short-term**: {"Schedule technical interview" if candidate_screening['next_step'] in ['take_home_assignment', 'senior_level_assessment'] else "Complete evaluation process"}
3. **Final**: Make hiring decision and provide feedback

## Decision Timeline
- **Target Decision Date**: _[To be set]_
- **Feedback Delivery**: _[To be set]_
- **Start Date (if hired)**: _[To be negotiated]_

---
*Evaluation framework prepared on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Current stage: Post-screening, {"awaiting take-home completion" if candidate_screening['next_step'] == 'take_home_assignment' else "awaiting next assessment"}*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Generate complete materials for all candidates"""
    
    print("🚀 Generating complete candidate materials...")
    
    # Load data
    screening_data, candidates_lookup = load_candidate_data()
    
    base_path = Path("artifacts/public/hiring/candidates/20250811_consolidated")
    
    generation_log = {
        "generation_date": datetime.now().isoformat(),
        "total_candidates": len(screening_data['screening_results']),
        "materials_generated": [],
        "errors": []
    }
    
    for candidate_screening in screening_data['screening_results']:
        try:
            candidate_id = candidate_screening['candidate_id']
            candidate_name = candidate_screening['candidate_name']
            
            print(f"📝 Generating materials for: {candidate_name} ({candidate_id})")
            
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
            
            # Generate screening report if missing
            screening_path = candidate_dir / "screening" / "screening_report.md"
            if not screening_path.exists():
                generate_screening_report(candidate_screening, candidate_data, screening_path)
                materials_generated.append("screening_report.md")
            
            # Generate take-home assignment for qualified candidates
            if candidate_screening['next_step'] in ['take_home_assignment', 'senior_level_assessment']:
                takehome_path = candidate_dir / "takehome" / "takehome_assignment.md"
                if not takehome_path.exists():
                    generate_takehome_assignment(candidate_screening, candidate_data, takehome_path)
                    materials_generated.append("takehome_assignment.md")
            
            # Generate interview materials for qualified candidates
            if candidate_screening['next_step'] in ['take_home_assignment', 'senior_level_assessment', 'additional_assessment']:
                interview_dir = candidate_dir / "interview"
                
                # Generate missing interview materials
                if not (interview_dir / "candidate_context.md").exists():
                    generate_interview_materials(candidate_screening, candidate_data, candidate_dir)
                    materials_generated.extend(["candidate_context.md", "interview_guide.md", "interview_script.md"])
            
            # Generate evaluation framework
            evaluation_path = candidate_dir / "evaluation" / "evaluation_framework.md"
            if not evaluation_path.exists():
                generate_evaluation_framework(candidate_screening, candidate_data, evaluation_path)
                materials_generated.append("evaluation_framework.md")
            
            generation_log["materials_generated"].append({
                "candidate_id": candidate_id,
                "candidate_name": candidate_name,
                "materials": materials_generated,
                "total_files": len(materials_generated)
            })
            
            print(f"  ✅ Generated {len(materials_generated)} materials")
            
        except Exception as e:
            error_msg = f"Error processing {candidate_id}: {str(e)}"
            print(f"  ❌ {error_msg}")
            generation_log["errors"].append(error_msg)
    
    # Save generation log
    log_path = base_path / "materials_generation_log.json"
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(generation_log, f, indent=2, ensure_ascii=False)
    
    total_materials = sum(len(c["materials"]) for c in generation_log["materials_generated"])
    
    print(f"\n✅ Material generation complete!")
    print(f"📊 Processed {generation_log['total_candidates']} candidates")
    print(f"📄 Generated {total_materials} new materials")
    print(f"📋 Log saved to: {log_path}")
    
    if generation_log["errors"]:
        print(f"⚠️  {len(generation_log['errors'])} errors occurred - check log for details")

if __name__ == "__main__":
    main()