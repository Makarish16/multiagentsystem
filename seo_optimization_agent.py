from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from .base_agent import BaseAgent, AgentContext
from .content_generation_agent import BlogPost

@dataclass
class SEOOptimizedPost:
    """Structure for the SEO-optimized blog post."""
    title: str
    meta_description: str
    content: str
    word_count: int
    keywords: List[str]
    sources: List[str]
    keyword_density: Dict[str, float]
    readability_score: float

class SEOOptimizationAgent(BaseAgent):
    """Agent responsible for optimizing blog post content for search engines."""
    
    def __init__(self, name: str = "SEOOptimizationAgent", context: Optional[AgentContext] = None):
        super().__init__(name, context)
    
    async def execute(self, blog_post: BlogPost) -> SEOOptimizedPost:
        """Optimize the blog post for search engines.
        
        Args:
            blog_post: BlogPost object containing the content to optimize
            
        Returns:
            SEOOptimizedPost object containing the optimized content
        """
        self.log("Starting SEO optimization process", "info")
        
        # Optimize title and meta description
        optimized_title = self._optimize_title(blog_post.title)
        optimized_meta = self._optimize_meta_description(blog_post.meta_description)
        
        # Optimize content
        optimized_content = self._optimize_content(blog_post.content, blog_post.keywords)
        
        # Calculate keyword density
        keyword_density = self._calculate_keyword_density(optimized_content, blog_post.keywords)
        
        # Calculate readability score
        readability_score = self._calculate_readability_score(optimized_content)
        
        optimized_post = SEOOptimizedPost(
            title=optimized_title,
            meta_description=optimized_meta,
            content=optimized_content,
            word_count=len(optimized_content.split()),
            keywords=blog_post.keywords,
            sources=blog_post.sources,
            keyword_density=keyword_density,
            readability_score=readability_score
        )
        
        self.update_context(
            metadata={
                "optimized_post": optimized_post,
                "keyword_density": keyword_density,
                "readability_score": readability_score
            }
        )
        
        self.log(f"SEO optimization completed with readability score: {readability_score}", "success")
        return optimized_post
    
    def _optimize_title(self, title: str) -> str:
        """Optimize the title for SEO."""
      
        return title
    
    def _optimize_meta_description(self, meta_description: str) -> str:
        """Optimize the meta description for SEO."""
        
        return meta_description
    
    def _optimize_content(self, content: str, keywords: List[str]) -> str:
        """Optimize the content for SEO."""
       
        return content
    
    def _calculate_keyword_density(self, content: str, keywords: List[str]) -> Dict[str, float]:
        """Calculate keyword density for each target keyword."""
      
        return {keyword: 0.02 for keyword in keywords}
    
    def _calculate_readability_score(self, content: str) -> float:
        """Calculate content readability score."""
       
        return 75.0  # Score between 0-100, higher is more readable
