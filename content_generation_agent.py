from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from .base_agent import BaseAgent, AgentContext
from .content_planning_agent import BlogOutline

@dataclass
class BlogPost:
    """Structure for the generated blog post."""
    title: str
    meta_description: str
    content: str
    word_count: int
    keywords: List[str]
    sources: List[str]

class ContentGenerationAgent(BaseAgent):
    """Agent responsible for generating the blog post content based on research and outline."""
    
    def __init__(self, name: str = "ContentGenerationAgent", context: Optional[AgentContext] = None):
        super().__init__(name, context)
    
    async def execute(self, outline: BlogOutline, research_data: Dict[str, Any]) -> BlogPost:
        """Generate blog post content based on the provided outline and research data.
        
        Args:
            outline: BlogOutline object containing the content structure
            research_data: Dictionary containing research findings and sources
            
        Returns:
            BlogPost object containing the generated content
        """
        self.log("Starting content generation process", "info")
        
        # Generate content for each section
        content_sections = []
        for section in outline.sections:
            section_content = self._generate_section_content(section, research_data)
            content_sections.append(section_content)
        
        # Combine all sections into full content
        full_content = "\n\n".join(content_sections)
        
        # Calculate actual word count
        word_count = len(full_content.split())
        
        blog_post = BlogPost(
            title=outline.title,
            meta_description=outline.meta_description,
            content=full_content,
            word_count=word_count,
            keywords=outline.target_keywords,
            sources=research_data["sources"]
        )
        
        self.update_context(
            metadata={
                "blog_post": blog_post,
                "actual_word_count": word_count
            }
        )
        
        self.log(f"Content generation completed with {word_count} words", "success")
        return blog_post
    
    def _generate_section_content(self, section: Dict[str, Any], research_data: Dict[str, Any]) -> str:
        """Generate content for a specific section of the blog post.
        
        Args:
            section: Dictionary containing section structure and requirements
            research_data: Dictionary containing research findings and sources
            
        Returns:
            Generated content for the section
        """
        # This is a placeholder implementation
        # In a real implementation, this would use an LLM to generate content
        content_parts = [f"# {section['title']}\n"]
        
        if section.get("key_points"):
            for point in section["key_points"]:
                content_parts.append(f"## {point}\n")
                content_parts.append(f"Content about {point.lower()}...\n")
        
        if section.get("subsections"):
            for subsection in section["subsections"]:
                content_parts.append(f"## {subsection['title']}\n")
                content_parts.append(f"Content about {subsection['title'].lower()}...\n")
        
        return "\n".join(content_parts)
    
    def _ensure_keyword_density(self, content: str, keywords: List[str]) -> str:
        """Ensure proper keyword density in the content.
        
        Args:
            content: The generated content
            keywords: List of target keywords
            
        Returns:
            Content with optimized keyword density
        """
        # This is a placeholder implementation
        # In a real implementation, this would analyze and optimize keyword density
        return content