# Graph RAG Architecture Proposal

## Executive Summary

The current design uses simple domain-separated storage, which limits context intelligence and extensibility. This proposal recommends implementing a **Graph RAG-based architecture** with multi-database integration to create a more intelligent, relationship-aware context system that can serve both the current Gefjon Growth project and future AI agents.

## Current Architecture Limitations

### **Simple Domain Storage Issues**:
- **No Semantic Relationships**: Cannot understand connections between candidates, skills, and values
- **Manual Context Assembly**: Requires predefined domain combinations
- **Limited Knowledge Discovery**: Cannot find indirect relationships or similar patterns
- **Poor Extensibility**: Hard to add new knowledge types or relationships
- **Inefficient Context Generation**: Relies on basic caching rather than intelligent retrieval

### **Monolithic Context Server Issues**:
- **Tight Coupling**: Context server is part of hiring system rather than independent service
- **Limited Reusability**: Cannot easily serve other AI agents or future projects
- **Scalability Constraints**: Single service handling all context operations

## Recommended Graph RAG Architecture

### **Independent Context Service (MSA)**

**Service Name**: `context-graph-service`
- **Purpose**: Universal context service for all AI agents (current and future)
- **Architecture**: Independent microservice following MSA principles
- **API**: RESTful JSON API for universal compatibility
- **Deployment**: Separate ECS service that can scale independently

### **Multi-Database Architecture**

#### **1. Knowledge Graph Database (Neo4j/Amazon Neptune)**
**Purpose**: Semantic relationships and intelligent context discovery

**Entities**:
```cypher
// Core entities with rich properties
(:Candidate {id, name, email, experience_years, current_role})
(:Skill {name, category, market_demand, complexity_level})
(:CoreValue {name, description, weight, examples})
(:Role {title, level, department, requirements})
(:Project {name, domain, technologies, impact})
(:Company {name, industry, size, values})
```

**Relationships**:
```cypher
// Rich relationships with properties and weights
(Candidate)-[:HAS_SKILL {proficiency: 0.9, years: 5, verified: true}]->(Skill)
(Candidate)-[:DEMONSTRATES {evidence: "text", score: 0.85, frequency: "often"}]->(CoreValue)
(Candidate)-[:WORKED_ON {duration: "2 years", role: "Lead", impact: "high"}]->(Project)
(Skill)-[:REQUIRED_FOR {importance: 0.8, level: "expert"}]->(Role)
(CoreValue)-[:CRITICAL_FOR {weight: 0.9, evaluation_method: "BEI"}]->(Role)
(Project)-[:DEMONSTRATES {strength: 0.7}]->(Skill)
(Project)-[:EXEMPLIFIES {clarity: 0.8}]->(CoreValue)
(Candidate)-[:SIMILAR_TO {similarity: 0.75, basis: "skills+values"}]->(Candidate)
```

#### **2. Vector Database (Pinecone/Weaviate/Amazon OpenSearch)**
**Purpose**: Semantic similarity and document retrieval

**Content Types**:
- **Candidate Profile Embeddings**: Semantic representation of complete profiles
- **Interview Transcript Embeddings**: Past interview content for pattern matching
- **Project Description Embeddings**: Technical project details and outcomes
- **Core Value Evidence Embeddings**: Examples of value demonstrations
- **Question Bank Embeddings**: BEI questions and technical assessments

#### **3. Relational Database (PostgreSQL)**
**Purpose**: Structured transactional data and audit trails

**Tables**:
- **candidates**: Structured profile data with JSON fields
- **interview_kits**: Generated interview materials with approval workflow
- **hiring_workflows**: Process state and milestone tracking
- **audit_events**: Immutable audit log with structured JSON
- **performance_metrics**: System performance and cost tracking

#### **4. NoSQL Database (DynamoDB)**
**Purpose**: High-performance session data and real-time caching

**Use Cases**:
- **Agent Sessions**: Active agent contexts and conversation state
- **Real-time Metrics**: Live performance and cost tracking
- **Configuration Data**: Agent-specific settings and preferences
- **Temporary Workspaces**: Draft interview kits and assessments

#### **5. Redis Cache**
**Purpose**: Ultra-high performance caching (>95% hit ratio)

**Cache Types**:
- **Graph Query Results**: Frequently accessed relationship patterns
- **Vector Search Results**: Similar candidate matches and context patterns
- **Optimized Context Payloads**: Agent-ready context in JSON format
- **Token Count Cache**: Pre-calculated token counts for optimization

## Graph RAG Context Generation Workflow

### **Intelligent Context Assembly**

```python
class GraphRAGContextEngine:
    def generate_context(self, candidate_id: str, task_type: str, agent_type: str) -> Dict:
        # 1. Multi-hop graph traversal for relationship discovery
        graph_context = self.discover_relationships(candidate_id, task_type)
        
        # 2. Vector similarity search for semantic context
        vector_context = self.find_similar_patterns(candidate_id, task_type)
        
        # 3. Intelligent context fusion
        fused_context = self.fuse_multi_source_context(graph_context, vector_context)
        
        # 4. Relevance-based ranking and filtering
        ranked_context = self.rank_by_relevance(fused_context, task_type)
        
        # 5. Agent-specific optimization
        optimized_context = self.optimize_for_agent(ranked_context, agent_type)
        
        return optimized_context
    
    def discover_relationships(self, candidate_id: str, task_type: str) -> Dict:
        """Multi-hop graph traversal for intelligent context discovery"""
        if task_type == "screening":
            # Focus on core values and skill relationships
            query = """
            MATCH (c:Candidate {id: $candidate_id})
            MATCH (c)-[r1:DEMONSTRATES]->(v:CoreValue)
            MATCH (c)-[r2:HAS_SKILL]->(s:Skill)-[r3:REQUIRED_FOR]->(role:Role)
            MATCH (c)-[r4:WORKED_ON]->(p:Project)-[r5:EXEMPLIFIES]->(v2:CoreValue)
            RETURN c, v, s, role, p, v2, r1, r2, r3, r4, r5
            ORDER BY r1.score DESC, r2.proficiency DESC
            """
        elif task_type == "interview_kit":
            # Focus on evidence and examples for BEI questions
            query = """
            MATCH (c:Candidate {id: $candidate_id})
            MATCH (c)-[r1:DEMONSTRATES]->(v:CoreValue)
            MATCH (c)-[r2:WORKED_ON]->(p:Project)
            MATCH (p)-[r3:DEMONSTRATES]->(s:Skill)
            MATCH (similar:Candidate)-[r4:SIMILAR_TO]-(c)
            MATCH (similar)-[r5:DEMONSTRATES]->(v)
            RETURN c, v, p, s, similar, r1, r2, r3, r4, r5
            ORDER BY r1.score DESC, r4.similarity DESC
            """
        
        return self.neo4j_client.run_query(query, candidate_id=candidate_id)
    
    def find_similar_patterns(self, candidate_id: str, task_type: str) -> List[Dict]:
        """Vector similarity search for semantic context"""
        candidate_embedding = self.get_candidate_embedding(candidate_id)
        
        similar_contexts = self.vector_db.similarity_search(
            query_vector=candidate_embedding,
            filter={
                "task_type": task_type,
                "quality_score": {"$gte": 0.8}
            },
            top_k=10,
            include_metadata=True
        )
        
        return similar_contexts
```

### **Context Quality Enhancement**

**Relationship-Aware Context**:
- **Multi-hop Discovery**: Find indirect relationships (candidate → project → skill → role requirement)
- **Pattern Recognition**: Identify successful candidate patterns for similar roles
- **Evidence Linking**: Connect candidate claims to concrete project examples
- **Value Demonstration**: Map abstract values to specific behavioral evidence

**Semantic Understanding**:
- **Skill Clustering**: Group related technical skills and competencies
- **Value Alignment**: Understand nuanced expressions of core values
- **Experience Relevance**: Weight experience based on role requirements
- **Cultural Fit**: Assess alignment with company culture and team dynamics

## Implementation Benefits

### **Intelligence Benefits**
1. **Relationship Discovery**: Automatically find relevant connections between entities
2. **Pattern Recognition**: Identify successful candidate patterns and anti-patterns
3. **Context Richness**: Provide deeper, more meaningful context for AI agents
4. **Adaptive Learning**: Graph relationships improve over time with more data

### **Performance Benefits**
1. **Efficient Retrieval**: Graph queries are more efficient than complex joins
2. **Smart Caching**: Cache relationship patterns rather than raw data
3. **Relevance Ranking**: Prioritize most relevant context for token optimization
4. **Parallel Processing**: Query graph and vector databases simultaneously

### **Extensibility Benefits**
1. **Easy Entity Addition**: Add new entity types without schema changes
2. **Flexible Relationships**: Create new relationship types as needed
3. **Multi-Agent Support**: Serve different agents with tailored context
4. **Future-Proof**: Architecture supports unknown future requirements

### **Cost Optimization Benefits**
1. **Intelligent Context Selection**: Only include most relevant information
2. **Relationship-Based Compression**: Compress context while preserving meaning
3. **Pattern Reuse**: Reuse similar context patterns across candidates
4. **Efficient Caching**: Cache relationship patterns for maximum reuse

## Migration Strategy

### **Phase 1: Graph Database Setup**
- Deploy Neo4j/Amazon Neptune instance
- Create knowledge graph schema
- Migrate existing candidate and company data to graph format
- Establish basic relationships

### **Phase 2: Vector Database Integration**
- Set up Pinecone/Weaviate instance
- Generate embeddings for existing content
- Implement semantic similarity search
- Integrate with graph queries

### **Phase 3: Context Service Independence**
- Extract context functionality into separate microservice
- Implement RESTful JSON API
- Add multi-database query orchestration
- Deploy as independent ECS service

### **Phase 4: Graph RAG Implementation**
- Implement intelligent context assembly algorithms
- Add relationship-aware context generation
- Integrate vector similarity with graph traversal
- Optimize for agent-specific requirements

### **Phase 5: Performance Optimization**
- Implement advanced caching strategies
- Add query optimization and indexing
- Fine-tune relevance ranking algorithms
- Validate cost and performance targets

## Recommended Database Selection

### **Knowledge Graph**: Amazon Neptune
- **Pros**: Fully managed, AWS native, supports both Gremlin and SPARQL
- **Cons**: Higher cost than self-managed Neo4j
- **Recommendation**: Use for production due to AWS integration

### **Vector Database**: Amazon OpenSearch with vector engine
- **Pros**: AWS native, cost-effective, integrated with existing infrastructure
- **Cons**: Less specialized than Pinecone/Weaviate
- **Recommendation**: Use for cost optimization within AWS ecosystem

### **Relational**: PostgreSQL on RDS (existing)
- **Pros**: Already deployed, proven performance, JSON support
- **Cons**: None for this use case
- **Recommendation**: Continue using existing instance

### **NoSQL**: DynamoDB (existing)
- **Pros**: AWS native, high performance, cost-effective
- **Cons**: None for this use case
- **Recommendation**: Use existing tables where possible

### **Cache**: Redis (existing)
- **Pros**: High performance, existing deployment
- **Cons**: None for this use case
- **Recommendation**: Extend existing Redis cluster

## Cost Impact Analysis

### **Additional Infrastructure Costs**
- **Amazon Neptune**: ~$200-400/month for small instance
- **OpenSearch Vector Engine**: ~$100-200/month for vector indexing
- **Additional Storage**: ~$50-100/month for graph and vector data
- **Total Additional**: ~$350-700/month

### **Cost Savings**
- **Improved Context Efficiency**: 30-50% reduction in token usage through intelligent selection
- **Better Caching**: Higher cache hit ratios reduce LLM API calls
- **Reduced Development Time**: Faster context generation and maintenance
- **Future Agent Reuse**: Amortize costs across multiple AI agent projects

### **ROI Analysis**
- **Break-even**: 3-6 months based on improved efficiency and reusability
- **Long-term Savings**: Significant cost reduction as more agents use the service
- **Quality Improvement**: Better context leads to better AI agent performance

## Conclusion

The Graph RAG architecture provides significant advantages over the current simple domain storage approach:

1. **Intelligence**: Relationship-aware context generation
2. **Extensibility**: Easy to add new entities and relationships
3. **Performance**: More efficient context retrieval and caching
4. **Reusability**: Independent service for current and future agents
5. **Cost Optimization**: Intelligent context selection reduces token usage

**Recommendation**: Implement Graph RAG architecture as proposed, with phased migration to minimize risk and validate benefits incrementally.