# AWS Bedrock Native Architecture

## Executive Summary for AWS Partnership Meeting

This document outlines a comprehensive AWS cloud-native implementation of the Graph RAG-based context-centric multi-agent system using Amazon Bedrock and AWS managed services. This approach leverages AWS's enterprise-grade infrastructure, managed AI services, and partnership pricing to create a scalable, cost-effective solution for HR automation.

## AWS Native Architecture Overview

### Core Value Proposition
- **Zero Infrastructure Management**: Fully managed AWS services eliminate operational overhead
- **Enterprise Security**: Built-in compliance, encryption, and access controls
- **Automatic Scaling**: Pay-per-use model with automatic capacity adjustment
- **AWS Partnership Benefits**: Preferred pricing, technical support, and co-innovation opportunities

### High-Level AWS Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AWS API Gateway + CloudFront                 │
│  Global Distribution │ Rate Limiting │ Authentication          │
└─────────────────────────────────────────────────────────────────┘
                                    │
┌─────────────────────────────────────────────────────────────────┐
│                    Amazon Bedrock Agent Layer                   │
│  Agent Orchestration │ Claude 3.5 Sonnet │ Guardrails         │
└─────────────────────────────────────────────────────────────────┘
                                    │
┌─────────────────────────────────────────────────────────────────┐
│                    AWS Lambda Serverless Functions              │
│  Context Assembly │ Hiring Workflow │ Token Optimization       │
└─────────────────────────────────────────────────────────────────┘
                                    │
┌─────────────────────────────────────────────────────────────────┐
│                    AWS Managed Data Services                    │
│  Neptune Graph │ OpenSearch Vector │ RDS │ DynamoDB │ Redis    │
└─────────────────────────────────────────────────────────────────┘
```

## Amazon Bedrock Integration Strategy

### Bedrock Agents for Multi-Agent Orchestration

**Agent Configuration**:
```json
{
  "agentName": "hiring-context-agent",
  "foundationModel": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "instruction": "You are a hiring context specialist that uses Graph RAG to discover relevant candidate information through knowledge graph relationships and semantic similarity.",
  "actionGroups": [
    {
      "actionGroupName": "graph-traversal",
      "description": "Query Neptune knowledge graph for candidate relationships",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:us-east-1:account:function:graph-query"
      }
    },
    {
      "actionGroupName": "vector-search",
      "description": "Search OpenSearch for semantically similar candidates",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:us-east-1:account:function:vector-search"
      }
    },
    {
      "actionGroupName": "context-fusion",
      "description": "Combine graph and vector results into optimized context",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:us-east-1:account:function:context-fusion"
      }
    }
  ],
  "knowledgeBases": [
    {
      "knowledgeBaseId": "hiring-knowledge-base",
      "description": "Company values, hiring processes, and successful candidate patterns"
    }
  ]
}
```

### Bedrock Knowledge Base Integration

**Knowledge Base Setup**:
- **Data Sources**: S3 buckets with company documentation, hiring guides, core values
- **Embeddings**: Amazon Titan Embeddings G1 - Text for semantic understanding
- **Vector Store**: Amazon OpenSearch Serverless for automatic scaling
- **Chunking Strategy**: Semantic chunking with relationship preservation

**Knowledge Base Configuration**:
```yaml
knowledgeBase:
  name: "hiring-context-kb"
  description: "Comprehensive hiring context with company values and processes"
  roleArn: "arn:aws:iam::account:role/bedrock-kb-role"
  
  dataSource:
    name: "company-hiring-docs"
    s3Configuration:
      bucketArn: "arn:aws:s3:::hiring-knowledge-bucket"
      inclusionPrefixes: ["company-values/", "hiring-processes/", "interview-guides/"]
    
  vectorIngestionConfiguration:
    chunkingConfiguration:
      chunkingStrategy: "SEMANTIC"
      semanticChunkingConfiguration:
        maxTokens: 300
        bufferSize: 20
        breakpointPercentileThreshold: 95
    
  storageConfiguration:
    type: "OPENSEARCH_SERVERLESS"
    opensearchServerlessConfiguration:
      collectionArn: "arn:aws:aoss:us-east-1:account:collection/hiring-vectors"
      vectorIndexName: "hiring-context-index"
      fieldMapping:
        vectorField: "embedding"
        textField: "content"
        metadataField: "metadata"
```

## AWS Lambda Serverless Implementation

### Graph RAG Context Assembly Function

```python
import boto3
import json
import logging
from typing import Dict, List, Any

# Initialize AWS clients
bedrock_agent = boto3.client('bedrock-agent-runtime')
neptune = boto3.client('neptune')
opensearch = boto3.client('opensearch-serverless')
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """
    AWS Lambda function for Graph RAG context assembly
    Combines Neptune graph traversal with OpenSearch vector similarity
    """
    try:
        # Extract request parameters
        candidate_id = event['candidate_id']
        task_type = event['task_type']
        agent_type = event.get('agent_type', 'bedrock')
        
        logger.info(f"Processing context request for candidate {candidate_id}, task {task_type}")
        
        # Step 1: Graph traversal using Neptune
        graph_context = query_neptune_relationships(candidate_id, task_type)
        
        # Step 2: Vector similarity search using OpenSearch
        vector_context = search_opensearch_similarity(candidate_id, task_type)
        
        # Step 3: Context fusion using Bedrock
        fused_context = fuse_context_with_bedrock(graph_context, vector_context, task_type)
        
        # Step 4: Token optimization
        optimized_context = optimize_tokens_for_agent(fused_context, agent_type)
        
        # Step 5: Cache results in DynamoDB
        cache_context_result(candidate_id, task_type, optimized_context)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'context': optimized_context,
                'metadata': {
                    'candidate_id': candidate_id,
                    'task_type': task_type,
                    'token_count': len(optimized_context.split()),
                    'graph_relationships': len(graph_context.get('relationships', [])),
                    'similar_candidates': len(vector_context.get('similar', []))
                }
            })
        }
        
    except Exception as e:
        logger.error(f"Error processing context request: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def query_neptune_relationships(candidate_id: str, task_type: str) -> Dict[str, Any]:
    """Query Neptune for candidate relationships using Gremlin"""
    
    if task_type == "screening":
        # Focus on core values and skill relationships
        gremlin_query = f"""
        g.V().has('candidate', 'id', '{candidate_id}')
        .outE('DEMONSTRATES').inV().has('type', 'core_value')
        .project('value', 'evidence', 'score')
        .by('name')
        .by(outE('DEMONSTRATES').where(inV().has('id', '{candidate_id}')).values('evidence'))
        .by(outE('DEMONSTRATES').where(inV().has('id', '{candidate_id}')).values('score'))
        .order().by('score', desc).limit(10)
        """
    elif task_type == "interview_kit":
        # Focus on projects and achievements for BEI questions
        gremlin_query = f"""
        g.V().has('candidate', 'id', '{candidate_id}')
        .outE('WORKED_ON').inV().has('type', 'project')
        .project('project', 'skills', 'values', 'impact')
        .by('name')
        .by(outE('DEMONSTRATES').inV().has('type', 'skill').values('name').fold())
        .by(outE('EXEMPLIFIES').inV().has('type', 'core_value').values('name').fold())
        .by('impact_score')
        .order().by('impact_score', desc).limit(5)
        """
    
    # Execute Gremlin query (simplified - actual implementation would use Neptune client)
    response = neptune.execute_gremlin_query(query=gremlin_query)
    return response.get('result', {})

def search_opensearch_similarity(candidate_id: str, task_type: str) -> Dict[str, Any]:
    """Search OpenSearch for semantically similar candidates and patterns"""
    
    # Get candidate embedding from DynamoDB cache or generate new one
    candidate_embedding = get_candidate_embedding(candidate_id)
    
    search_query = {
        "size": 10,
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": candidate_embedding}
                }
            }
        },
        "_source": ["candidate_id", "profile_summary", "success_indicators", "hire_outcome"],
        "filter": {
            "term": {"task_type": task_type}
        }
    }
    
    response = opensearch.search(
        index="candidate-similarity-index",
        body=search_query
    )
    
    return {
        "similar": [hit["_source"] for hit in response["hits"]["hits"]],
        "similarity_scores": [hit["_score"] for hit in response["hits"]["hits"]]
    }

def fuse_context_with_bedrock(graph_context: Dict, vector_context: Dict, task_type: str) -> str:
    """Use Bedrock to intelligently fuse graph and vector context"""
    
    fusion_prompt = f"""
    You are an expert at combining different types of context for hiring decisions.
    
    Task Type: {task_type}
    
    Graph Context (Relationships):
    {json.dumps(graph_context, indent=2)}
    
    Vector Context (Similar Patterns):
    {json.dumps(vector_context, indent=2)}
    
    Please create a comprehensive, coherent context that:
    1. Combines the relationship data with similar candidate patterns
    2. Highlights the most relevant information for {task_type}
    3. Maintains semantic coherence and meaning
    4. Prioritizes evidence-based insights
    
    Format the response as structured JSON with clear sections.
    """
    
    response = bedrock_agent.invoke_model(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        body=json.dumps({
            'messages': [{'role': 'user', 'content': fusion_prompt}],
            'max_tokens': 2000,
            'temperature': 0.1
        })
    )
    
    return json.loads(response['body'])['content'][0]['text']

def optimize_tokens_for_agent(context: str, agent_type: str) -> str:
    """Optimize context length for specific agent requirements"""
    
    # Agent-specific token limits (empirically determined)
    token_limits = {
        'bedrock': 4000,
        'gemini_cli': 3000,
        'claude_code': 8000,  # Can handle more with 200k window
        'amazon_q': 2000,
        'openai_mini': 1500   # Cost-optimized
    }
    
    max_tokens = token_limits.get(agent_type, 3000)
    current_tokens = len(context.split())
    
    if current_tokens <= max_tokens:
        return context
    
    # Use Bedrock to compress while preserving meaning
    compression_prompt = f"""
    Please compress this context to approximately {max_tokens} tokens while preserving:
    1. All key relationships and evidence
    2. Semantic meaning and coherence
    3. Critical insights for hiring decisions
    
    Original context:
    {context}
    
    Provide the compressed version maintaining JSON structure.
    """
    
    response = bedrock_agent.invoke_model(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        body=json.dumps({
            'messages': [{'role': 'user', 'content': compression_prompt}],
            'max_tokens': max_tokens,
            'temperature': 0.1
        })
    )
    
    return json.loads(response['body'])['content'][0]['text']

def cache_context_result(candidate_id: str, task_type: str, context: str) -> None:
    """Cache context result in DynamoDB for reuse"""
    
    table = dynamodb.Table('context-cache')
    
    table.put_item(
        Item={
            'cache_key': f"{candidate_id}#{task_type}",
            'context': context,
            'timestamp': int(time.time()),
            'ttl': int(time.time()) + 3600  # 1 hour TTL
        }
    )

def get_candidate_embedding(candidate_id: str) -> List[float]:
    """Get or generate candidate embedding using Bedrock Titan"""
    
    # Check cache first
    table = dynamodb.Table('embedding-cache')
    response = table.get_item(Key={'candidate_id': candidate_id})
    
    if 'Item' in response:
        return response['Item']['embedding']
    
    # Generate new embedding using Titan
    candidate_profile = get_candidate_profile(candidate_id)
    
    response = bedrock_agent.invoke_model(
        modelId='amazon.titan-embed-text-v1',
        body=json.dumps({
            'inputText': candidate_profile
        })
    )
    
    embedding = json.loads(response['body'])['embedding']
    
    # Cache the embedding
    table.put_item(
        Item={
            'candidate_id': candidate_id,
            'embedding': embedding,
            'timestamp': int(time.time())
        }
    )
    
    return embedding
```

## AWS Step Functions Hiring Workflow

### Complete Hiring Process Orchestration

```json
{
  "Comment": "Graph RAG-Powered Hiring Process Automation",
  "StartAt": "CandidateIntake",
  "States": {
    "CandidateIntake": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:account:function:candidate-intake",
      "Parameters": {
        "candidate_data.$": "$.candidate_data",
        "role_requirements.$": "$.role_requirements"
      },
      "ResultPath": "$.intake_result",
      "Next": "BuildKnowledgeGraph"
    },
    
    "BuildKnowledgeGraph": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:account:function:build-knowledge-graph",
      "Parameters": {
        "candidate_id.$": "$.intake_result.candidate_id",
        "profile_data.$": "$.intake_result.profile_data"
      },
      "ResultPath": "$.graph_result",
      "Next": "CoreValuesScreening"
    },
    
    "CoreValuesScreening": {
      "Type": "Task",
      "Resource": "arn:aws:states:::bedrock:invokeAgent",
      "Parameters": {
        "agentId": "hiring-context-agent",
        "agentAliasId": "TSTALIASID",
        "sessionId.$": "$.session_id",
        "inputText": {
          "Fn::Format": [
            "Screen candidate {} against our 10 core values using Graph RAG context discovery. Provide evidence-based scoring with specific examples from their experience.",
            ["$.intake_result.candidate_id"]
          ]
        }
      },
      "ResultPath": "$.screening_result",
      "Next": "ScreeningDecision"
    },
    
    "ScreeningDecision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.screening_result.recommendation",
          "StringEquals": "PASS",
          "Next": "TechnicalAssessment"
        },
        {
          "Variable": "$.screening_result.recommendation",
          "StringEquals": "NEEDS_REVIEW",
          "Next": "ManualScreeningReview"
        }
      ],
      "Default": "RejectCandidate"
    },
    
    "TechnicalAssessment": {
      "Type": "Task",
      "Resource": "arn:aws:states:::bedrock:invokeAgent",
      "Parameters": {
        "agentId": "hiring-context-agent",
        "agentAliasId": "TSTALIASID",
        "sessionId.$": "$.session_id",
        "inputText": {
          "Fn::Format": [
            "Generate a personalized technical assessment for candidate {} based on their profile and role requirements. Use Graph RAG to find similar successful candidates and appropriate challenge levels.",
            ["$.intake_result.candidate_id"]
          ]
        }
      },
      "ResultPath": "$.assessment_result",
      "Next": "InterviewKitGeneration"
    },
    
    "InterviewKitGeneration": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:account:function:interview-kit-generator",
      "Parameters": {
        "candidate_id.$": "$.intake_result.candidate_id",
        "screening_results.$": "$.screening_result",
        "assessment_results.$": "$.assessment_result",
        "task_type": "interview_kit"
      },
      "ResultPath": "$.interview_kit",
      "Next": "ManualApproval"
    },
    
    "ManualApproval": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke.waitForTaskToken",
      "Parameters": {
        "FunctionName": "manual-approval-handler",
        "Payload": {
          "TaskToken.$": "$$.Task.Token",
          "ApprovalData": {
            "candidate_id.$": "$.intake_result.candidate_id",
            "interview_kit.$": "$.interview_kit",
            "screening_summary.$": "$.screening_result.summary"
          }
        }
      },
      "ResultPath": "$.approval_result",
      "Next": "CreateDoorayTasks"
    },
    
    "CreateDoorayTasks": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:account:function:dooray-integration",
      "Parameters": {
        "candidate_id.$": "$.intake_result.candidate_id",
        "interview_kit.$": "$.interview_kit",
        "approval_status.$": "$.approval_result.status"
      },
      "ResultPath": "$.dooray_result",
      "Next": "NotifyStakeholders"
    },
    
    "NotifyStakeholders": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:us-east-1:account:hiring-notifications",
        "Message": {
          "Fn::Format": [
            "Interview kit generated for candidate {}. Dooray tasks created: {}",
            ["$.intake_result.candidate_id", "$.dooray_result.task_ids"]
          ]
        }
      },
      "End": true
    },
    
    "ManualScreeningReview": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke.waitForTaskToken",
      "Parameters": {
        "FunctionName": "manual-review-handler",
        "Payload": {
          "TaskToken.$": "$$.Task.Token",
          "ReviewData": {
            "candidate_id.$": "$.intake_result.candidate_id",
            "screening_results.$": "$.screening_result",
            "review_type": "screening"
          }
        }
      },
      "Next": "ScreeningDecision"
    },
    
    "RejectCandidate": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:account:function:candidate-rejection",
      "Parameters": {
        "candidate_id.$": "$.intake_result.candidate_id",
        "rejection_reason.$": "$.screening_result.rejection_reason"
      },
      "End": true
    }
  }
}
```

## Cost Analysis and ROI

### AWS Native vs Custom Implementation

**Monthly Cost Comparison (40 candidates/month)**:

| Service Category | AWS Native | Custom Python | Savings |
|------------------|------------|---------------|---------|
| **Compute** | Lambda: $30-50 | ECS: $200-300 | $150-250 |
| **AI/ML** | Bedrock: $200-300 | Subscriptions: $79-109 | -$121-191 |
| **Database** | Managed: $400-600 | Self-managed: $200-300 | -$200-300 |
| **Operations** | $0 (managed) | $500-1000 | $500-1000 |
| **Total** | $630-950 | $779-1409 | $149-459 |

**AWS Partnership Benefits**:
- **Preferred Pricing**: 20-30% discount on Bedrock usage
- **Technical Support**: Direct access to AWS solution architects
- **Co-Innovation**: Joint development and case study opportunities
- **Enterprise Credits**: Potential AWS credits for partnership projects

### Return on Investment

**Quantifiable Benefits**:
- **Reduced Development Time**: 60-80% faster implementation
- **Zero Operational Overhead**: No infrastructure management
- **Automatic Scaling**: Handle peak loads without manual intervention
- **Enterprise Security**: Built-in compliance and security controls

**Strategic Benefits**:
- **AWS Partnership**: Strengthen relationship with AWS for future projects
- **Competitive Advantage**: Leverage cutting-edge AWS AI services
- **Scalability**: Easy expansion to other HR processes and departments
- **Innovation**: Access to latest AWS AI/ML capabilities

## Implementation Roadmap for AWS Meeting

### Phase 1: Proof of Concept (2-3 weeks)
- Set up basic Bedrock Agent with Claude 3.5 Sonnet
- Implement simple Lambda function for context assembly
- Create Neptune knowledge graph with sample data
- Demonstrate Graph RAG context generation

### Phase 2: Core Functionality (4-6 weeks)
- Complete Step Functions hiring workflow
- Integrate OpenSearch vector database
- Implement all Lambda functions
- Add Bedrock Knowledge Base integration

### Phase 3: Production Deployment (2-3 weeks)
- Set up monitoring and alerting
- Implement security and compliance controls
- Performance testing and optimization
- Documentation and training

### Phase 4: Optimization and Scaling (Ongoing)
- Cost optimization and monitoring
- Performance tuning
- Feature enhancements
- Expansion to other use cases

## AWS Partnership Proposal

### Collaboration Opportunities

**Technical Collaboration**:
- Joint architecture review sessions
- Access to AWS AI/ML specialists
- Beta testing of new Bedrock features
- Technical case study development

**Business Collaboration**:
- Co-marketing opportunities
- Conference presentations
- Customer reference development
- Partnership pricing negotiations

**Innovation Collaboration**:
- Research and development projects
- New service feature feedback
- Industry best practices development
- Thought leadership content

### Success Metrics

**Technical Metrics**:
- Context generation latency: <200ms (p95)
- Interview kit generation: <4 hours
- System availability: >99.9%
- Cost per candidate: <$15

**Business Metrics**:
- Time-to-hire reduction: 20-30%
- Interview consistency: >90%
- Hiring quality improvement: 15-25%
- Operational cost reduction: 40-60%

This AWS Bedrock native architecture provides a compelling alternative to the custom Python implementation, offering enterprise-grade capabilities with reduced operational complexity and strong partnership benefits with AWS.