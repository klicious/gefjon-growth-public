# Technical Specifications

## Development Environment

### System Requirements
- **Python Version**: ≥3.12 (specified in pyproject.toml)
- **Package Manager**: UV (uv.lock present)
- **Data Versioning**: DVC (dvc.yaml)
- **Operating System**: macOS (current development environment)

### Dependencies & Tools
- **AI Framework**: Multi-agent system integration
- **MCP Servers**: Research, sequential thinking, browser automation, fetch
- **File Formats**: JSON (candidate data), YAML (context), Markdown (documentation)
- **Version Control**: Git with structured commit patterns

## MCP Server Integration

### Available MCP Servers
Amazon Q Developer should leverage these MCP servers when appropriate:

#### Research Capabilities
- **Primary**: `exa` - AI-powered research with advanced content discovery
- **Fallback**: `google-search` - Reliable web search and content extraction
- **Usage**: Web research, company research, content discovery/crawling
- **Trigger Words**: "research", "find info on", "deep dive on", "crawl site"

#### Reasoning & Planning
- **Server**: `sequential-thinking`
- **Usage**: Structured step-by-step reasoning and planning for complex tasks
- **Trigger Words**: "think step-by-step", "plan steps", "break down", "reason"

#### Browser Automation
- **Server**: `playwright`
- **Usage**: Browser automation and scripted web interactions
- **Capabilities**: Open page, click, fill forms, screenshot, scrape flows
- **Trigger Words**: "open page", "click", "fill", "screenshot", "scrape"

#### URL Fetching
- **Server**: `fetch`
- **Usage**: Direct URL fetching/HTTP downloads and simple scraping
- **Note**: Ensure proper configuration before use

### Research Fallback Protocol
1. Attempt `exa` for comprehensive AI-powered research first
2. Fall back to `google-search` if `exa` fails, unavailable, or budget constraints
3. Both tools support similar research workflows with different implementations

## File Structure & Naming Conventions

### Directory Organization
```
.amazonq/
├── context.md              # Main project context
├── project-guidelines.md   # Amazon Q specific guidelines
├── technical-specs.md      # This file - technical specifications
└── workflow-patterns.md    # Common workflow patterns and examples
```

### Naming Conventions
- **Candidate Files**: `{candidate_name}_{date}.json`
- **Output Directories**: `{date}_{process_type}/`
- **Interview Materials**: `{candidate_id}/candidate_context.md`, `interview_guide.md`, `interview_script.md`
- **Context Files**: `{domain}_{type}.yaml`

## Data Formats & Schemas

### Candidate Data Format (JSON)
```json
{
  "id": "candidate_unique_id",
  "name": "Candidate Name",
  "email": "candidate@example.com",
  "experience_years": 5,
  "skills": ["Python", "AWS", "Docker"],
  "education": {...},
  "work_history": [...],
  "projects": [...]
}
```

### Context File Format (YAML)
```yaml
---
id: "context_identifier"
type: "company_info|hr_process|team_structure"
domain: "hiring|performance|development"
last_updated: "2025-08-21"
tags: ["tag1", "tag2"]
visibility: "public|private"
---
# Content in markdown format
```

## Integration Patterns

### Multi-Agent Coordination
- **Claude Code**: Primary code development and complex logic
- **Gemini CLI**: ReAct workflow execution and process orchestration
- **Amazon Q Developer**: AWS-focused development and infrastructure
- **Coordination**: Shared context engineering protocol across all agents

### Context Sharing Protocol
1. All agents read from same `context/` directory
2. All agents write to structured `artifacts/` directories
3. Consistent naming conventions across agents
4. Shared quality standards and validation criteria

## Performance & Scalability

### Performance Targets
- **Processing Speed**: 6 hours for 13 candidates (baseline)
- **Quality Score**: 9.2/10 average (target)
- **Success Rate**: 90%+ candidate qualification
- **Error Rate**: <1% system errors

### Scalability Considerations
- **Horizontal Scaling**: Design for multiple concurrent candidates
- **Vertical Scaling**: Optimize for larger candidate datasets
- **Resource Management**: Efficient memory and processing usage
- **Error Handling**: Robust failure recovery and retry mechanisms

## Security & Compliance

### Data Protection
- **Sensitive Data**: Handle candidate PII appropriately
- **Access Controls**: Implement proper file permissions
- **Audit Trails**: Log all significant operations
- **Data Retention**: Follow appropriate retention policies

### Compliance Requirements
- **Privacy Regulations**: GDPR, CCPA compliance considerations
- **Data Security**: Encryption for sensitive information
- **Access Logging**: Track all data access and modifications
- **Backup & Recovery**: Ensure data integrity and availability

## Testing & Validation

### Quality Assurance
- **Unit Testing**: Individual component validation
- **Integration Testing**: Multi-agent workflow testing
- **End-to-End Testing**: Complete pipeline validation
- **Performance Testing**: Speed and efficiency validation

### Validation Criteria
- **Context Completeness**: All required information available
- **Output Quality**: Meets established quality standards
- **Process Compliance**: Follows context engineering protocol
- **Error Handling**: Graceful failure management

## Monitoring & Observability

### Key Metrics
- **Processing Time**: Track workflow execution duration
- **Quality Scores**: Monitor output quality consistency
- **Error Rates**: Track and analyze failure patterns
- **Resource Usage**: Monitor system resource consumption

### Logging Standards
- **Structured Logging**: JSON format for machine readability
- **Log Levels**: DEBUG, INFO, WARN, ERROR, CRITICAL
- **Context Inclusion**: Include relevant context in log entries
- **Performance Metrics**: Track timing and resource usage
