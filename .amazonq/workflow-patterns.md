# Workflow Patterns & Examples

## Common Workflow Patterns

### 1. Context Engineering Pattern
Every task should follow this pattern:

```python
# Step 1: Load Context
context_files = load_all_context_files("context/")
existing_artifacts = scan_artifacts_directory("artifacts/")

# Step 2: Validate Completeness
required_info = identify_required_information(task)
missing_info = validate_information_completeness(context_files, required_info)

# Step 3: Request Missing Information (if needed)
if missing_info:
    request_missing_information(missing_info)
    return

# Step 4: Execute Task
result = execute_task_with_context(context_files, existing_artifacts)

# Step 5: Store Results
save_results_to_artifacts(result, appropriate_directory)
```

### 2. Candidate Processing Pattern
For hiring-related tasks:

```python
# Load candidate data
candidate_data = load_candidate_json("data/public/hiring/resume/candidate.json")

# Load company context
company_values = load_context("context/company_info/mission_vision_values.yaml")
hiring_process = load_context("context/hr_processes/hiring/hiring_stages.yaml")

# Generate interview materials
interview_kit = generate_interview_kit(candidate_data, company_values, hiring_process)

# Save to appropriate directory
save_interview_kit(interview_kit, f"artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/")
```

### 3. Quality Validation Pattern
All outputs should be validated:

```python
# Validate output quality
quality_score = validate_output_quality(output, quality_standards)

if quality_score < 9.0:
    # Iterate and improve
    improved_output = improve_output(output, feedback)
    quality_score = validate_output_quality(improved_output, quality_standards)

# Only proceed if quality standards are met
if quality_score >= 9.0:
    save_output(improved_output)
else:
    request_manual_review(output, quality_issues)
```

## Specific Use Cases

### Use Case 1: New Candidate Interview Kit Generation

**Input**: Candidate JSON file in `data/public/hiring/resume/`
**Output**: Complete interview kit in `artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/`

**Process**:
1. Load candidate data from JSON file
2. Load company context (values, hiring process, team info)
3. Analyze candidate against company values
4. Generate personalized BEI questions
5. Create technical assessment plan
6. Compile complete interview kit
7. Validate quality (target: 9.2/10)
8. Save to designated directory

**Example Command**:
```bash
python scripts/generate_interview_kit.py --candidate data/public/hiring/resume/john_doe.json
```

### Use Case 2: Batch Candidate Processing

**Input**: Multiple candidate JSON files
**Output**: Consolidated results and individual interview kits

**Process**:
1. Load all candidate files from directory
2. Load shared company context once
3. Process each candidate individually
4. Generate interview kits for qualified candidates
5. Create consolidated summary report
6. Save all outputs with proper organization

**Example Execution**:
```bash
python scripts/complete_workflow_final.py
```

### Use Case 3: Context Update and Validation

**Input**: New company information or process changes
**Output**: Updated context files and validation report

**Process**:
1. Identify changed information
2. Update relevant context files
3. Validate consistency across all context
4. Update any dependent artifacts
5. Generate change impact report

## Error Handling Patterns

### Pattern 1: Missing Context Information
```python
try:
    context = load_required_context(required_files)
except MissingContextError as e:
    print(f"Missing required context: {e.missing_files}")
    print("Please provide the following information:")
    for file in e.missing_files:
        print(f"- {file}: {e.descriptions[file]}")
    return
```

### Pattern 2: Quality Standard Failure
```python
quality_score = validate_quality(output)
if quality_score < MINIMUM_QUALITY_THRESHOLD:
    improvement_suggestions = analyze_quality_issues(output)
    print(f"Quality score {quality_score} below threshold {MINIMUM_QUALITY_THRESHOLD}")
    print("Suggested improvements:")
    for suggestion in improvement_suggestions:
        print(f"- {suggestion}")
    
    # Attempt automatic improvement
    improved_output = apply_improvements(output, improvement_suggestions)
    return improved_output
```

### Pattern 3: File System Issues
```python
try:
    save_output(output, target_directory)
except FileSystemError as e:
    # Create directory if it doesn't exist
    os.makedirs(target_directory, exist_ok=True)
    save_output(output, target_directory)
except PermissionError as e:
    print(f"Permission denied: {e}")
    print("Please check file permissions and try again")
    return
```

## Integration Examples

### Example 1: Working with Claude Code
```python
# Amazon Q Developer prepares AWS infrastructure context
aws_context = prepare_aws_infrastructure_context()

# Claude Code handles complex algorithm development
algorithm_result = claude_code.develop_matching_algorithm(candidate_data, aws_context)

# Amazon Q Developer handles AWS deployment
deployment_result = deploy_to_aws(algorithm_result, aws_context)
```

### Example 2: Working with Gemini CLI
```python
# Gemini CLI orchestrates the overall workflow
workflow_plan = gemini_cli.create_workflow_plan(candidates)

# Amazon Q Developer handles AWS-specific components
for step in workflow_plan:
    if step.requires_aws:
        aws_result = amazon_q.execute_aws_step(step)
        gemini_cli.update_workflow_status(step, aws_result)
```

## Best Practice Examples

### Example 1: Comprehensive Context Loading
```python
def load_complete_context():
    """Load all necessary context for HR automation tasks."""
    context = {}
    
    # Company information
    context['company'] = {
        'values': load_yaml('context/company_info/mission_vision_values.yaml'),
        'goals': load_yaml('context/company_info/goals_okrs.yaml'),
        'trends': load_yaml('context/company_info/hr_trends.yaml')
    }
    
    # HR processes
    context['hr_processes'] = {
        'hiring': load_yaml('context/hr_processes/hiring/hiring_stages.yaml'),
        'evaluation': load_yaml('context/hr_processes/evaluation/performance_review_process.yaml'),
        'onboarding': load_yaml('context/hr_processes/onboarding/onboarding_plan.yaml')
    }
    
    # Team information
    context['teams'] = {
        'platform': load_yaml('context/teams/platform_development_team.yaml')
    }
    
    return context
```

### Example 2: Quality-Driven Output Generation
```python
def generate_high_quality_output(input_data, context, max_iterations=3):
    """Generate output with iterative quality improvement."""
    
    for iteration in range(max_iterations):
        # Generate output
        output = generate_output(input_data, context)
        
        # Validate quality
        quality_score = validate_quality(output)
        
        if quality_score >= TARGET_QUALITY_SCORE:
            return output
        
        # Analyze and improve
        issues = analyze_quality_issues(output)
        context = enhance_context_based_on_issues(context, issues)
    
    # If still not meeting standards, request manual review
    request_manual_review(output, "Quality standards not met after maximum iterations")
    return output
```

### Example 3: Structured Output Organization
```python
def organize_output(output, candidate_id, process_type):
    """Organize output according to established patterns."""
    
    base_dir = f"artifacts/public/hiring/{process_type}"
    candidate_dir = f"{base_dir}/{candidate_id}"
    
    # Create directory structure
    os.makedirs(candidate_dir, exist_ok=True)
    
    # Save different components
    save_file(output['context'], f"{candidate_dir}/candidate_context.md")
    save_file(output['guide'], f"{candidate_dir}/interview_guide.md")
    save_file(output['script'], f"{candidate_dir}/interview_script.md")
    
    # Update index
    update_candidate_index(candidate_id, candidate_dir, output['metadata'])
```

## Performance Optimization Patterns

### Pattern 1: Efficient Context Caching
```python
# Cache frequently used context to avoid repeated file I/O
context_cache = {}

def get_cached_context(context_type):
    if context_type not in context_cache:
        context_cache[context_type] = load_context(context_type)
    return context_cache[context_type]
```

### Pattern 2: Batch Processing Optimization
```python
def process_candidates_batch(candidate_files):
    """Process multiple candidates efficiently."""
    
    # Load shared context once
    shared_context = load_complete_context()
    
    # Process candidates in parallel where possible
    results = []
    for candidate_file in candidate_files:
        candidate_data = load_candidate(candidate_file)
        result = process_single_candidate(candidate_data, shared_context)
        results.append(result)
    
    return results
```

These patterns provide concrete examples of how Amazon Q Developer should operate within the Gefjon Growth ecosystem while maintaining the established quality standards and context engineering principles.
