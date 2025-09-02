# Project-Specific Guidelines for Amazon Q Developer

## Context Engineering Methodology

### Information Collection Protocol
Before executing any task, Amazon Q Developer must:

1. **Load Company Context**
   - Read all files in `context/company_info/` for mission, values, and OKRs
   - Review `context/hr_processes/hiring/` for process definitions
   - Check `context/teams/` for team-specific information

2. **Review Existing Artifacts**
   - Examine `artifacts/public/hiring/` for previous outputs
   - Check `artifacts/private/` for sensitive evaluations (if accessible)
   - Look for patterns and quality standards in existing work

3. **Validate Information Completeness**
   - Ensure all required context is available
   - Identify any missing information needed for task completion
   - Request specific missing data from user if insufficient

### Data Storage Requirements

#### Public Artifacts (`artifacts/public/`)
- Interview materials and candidate kits
- Process outputs and generated content
- Shareable documentation and reports
- Quality metrics and success measurements

#### Private Artifacts (`artifacts/private/`)
- Sensitive candidate evaluations
- Internal feedback and assessments
- Confidential scoring and rankings
- Private communication records

#### Context Updates (`context/`)
- New company information discoveries
- Process improvements and refinements
- Updated team structures or roles
- Enhanced reference materials

## Quality Assurance Standards

### Output Quality Metrics
- **Target Quality Score**: 9.2/10 or higher
- **Success Rate**: 90%+ candidate qualification
- **Processing Efficiency**: Maintain 6-hour processing for 13 candidates
- **Consistency**: Follow established patterns and formats

### Validation Checklist
- [ ] Output accuracy verified against context
- [ ] Proper file storage in designated directories
- [ ] Naming conventions followed
- [ ] Quality standards maintained
- [ ] Context engineering principles applied

## Workflow Integration

### Primary Execution Command
```bash
python scripts/complete_workflow_final.py
```

### Key Workflow Stages
1. **Context Loading** - Load all company and process context
2. **Data Normalization** - Standardize candidate information
3. **JD Mapping** - Match candidates to job requirements
4. **Screening** - Automated candidate evaluation
5. **Assignment Generation** - Create personalized take-home tasks
6. **Interview Kit Creation** - Generate comprehensive interview materials
7. **Consolidation** - Compile results and recommendations

### Integration Points
- Work seamlessly with Claude Code and Gemini CLI agents
- Maintain consistency across multi-agent outputs
- Follow established communication patterns
- Respect agent-specific responsibilities and capabilities

## Error Handling & Recovery

### Common Error Scenarios
1. **Missing Context Files** - Request specific files from user
2. **Incomplete Candidate Data** - Identify missing fields and request
3. **Quality Standard Failures** - Iterate and improve until standards met
4. **File Storage Issues** - Verify directory permissions and structure

### Recovery Protocols
- Stop execution when critical information is missing
- Provide clear error messages with specific requirements
- Offer suggestions for resolution
- Maintain data integrity throughout recovery process

## Service Delivery Focus

### Client-Centric Approach
- Prioritize client value and satisfaction
- Maintain professional service standards
- Deliver within promised timelines (30-day pilots)
- Provide comprehensive documentation and support

### Scalability Considerations
- Design solutions for multi-client deployment
- Implement configurable workflows
- Ensure robust error handling for production use
- Plan for volume scaling and performance optimization

## Continuous Improvement

### Learning Integration
- Incorporate feedback from successful executions
- Refine processes based on quality metrics
- Update context and guidelines based on new learnings
- Maintain alignment with evolving business objectives

### Documentation Updates
- Keep README.md as live documentation
- Update context files with new discoveries
- Maintain accurate process descriptions
- Document significant changes and improvements
