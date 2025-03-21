from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from .base_agent import AgentContext
from .research_agent import ResearchAgent
from .content_planning_agent import ContentPlanningAgent
from .content_generation_agent import ContentGenerationAgent
from .seo_optimization_agent import SEOOptimizationAgent

@dataclass
class BlogGenerationResult:
    """Structure for the final blog generation result."""
    title: str
    meta_description: str
    content: str
    word_count: int
    keywords: list[str]
    sources: list[str]
    keyword_density: Dict[str, float]
    readability_score: float
    generation_time: float

class BlogGenerationOrchestrator:
    """Orchestrates the multi-agent workflow for blog post generation."""
    
    def __init__(self, target_word_count: int = 2000):
        self.context = AgentContext(
            topic="",
            keywords=[],
            target_word_count=target_word_count
        )
        
        # Initialize agents
        self.research_agent = ResearchAgent(context=self.context)
        self.planning_agent = ContentPlanningAgent(context=self.context)
        self.generation_agent = ContentGenerationAgent(context=self.context)
        self.seo_agent = SEOOptimizationAgent(context=self.context)
    
    async def generate_blog_post(self, topic: Optional[str] = None) -> BlogGenerationResult:
        """Generate a complete, SEO-optimized blog post.
        
        Args:
            topic: Optional specific topic to write about. If None, will research trending topics.
            
        Returns:
            BlogGenerationResult containing the final blog post and metadata
        """
        start_time = datetime.now()
        
        # Step 1: Research phase
        research_data = await self.research_agent.execute(query=topic)
        
        # Step 2: Content planning phase
        outline = await self.planning_agent.execute(research_data)
        
        # Step 3: Content generation phase
        blog_post = await self.generation_agent.execute(outline, research_data)
        
        # Step 4: SEO optimization phase
        optimized_post = await self.seo_agent.execute(blog_post)
        
        # Calculate generation time
        generation_time = (datetime.now() - start_time).total_seconds()
        
        return BlogGenerationResult(
            title=optimized_post.title,
            meta_description=optimized_post.meta_description,
            content=optimized_post.content,
            word_count=optimized_post.word_count,
            keywords=optimized_post.keywords,
            sources=optimized_post.sources,
            keyword_density=optimized_post.keyword_density,
            readability_score=optimized_post.readability_score,
            generation_time=generation_time
        )
    
    def get_generation_status(self) -> Dict[str, Any]:
        """Get the current status of the blog generation process."""
        return {
            "topic": self.context.topic,
            "keywords": self.context.keywords,
            "target_word_count": self.context.target_word_count,
            "metadata": self.context.metadata
        }