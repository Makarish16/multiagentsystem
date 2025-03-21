from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from .base_agent import BaseAgent, AgentContext

@dataclass
class BlogOutline:
    """Structure for blog post outline."""
    title: str
    meta_description: str
    sections: List[Dict[str, Any]]
    target_keywords: List[str]
    estimated_word_count: int

class ContentPlanningAgent(BaseAgent):
    """Agent responsible for creating structured blog post outlines."""
    
    def __init__(self, name: str = "ContentPlanningAgent", context: Optional[AgentContext] = None):
        super().__init__(name, context)
    
    async def execute(self, research_data: Dict[str, Any]) -> BlogOutline:
        """Create a structured outline based on research data.
        
        Args:
            research_data: Dictionary containing research findings and key points
            
        Returns:
            BlogOutline object containing the structured outline
        """
        self.log("Starting content planning process", "info")
        
        # Extract relevant information from research data
        topic = research_data["selected_topic"]
        key_points = research_data["key_findings"]
        keywords = research_data["keywords"]
        
        # Generate meta description
        meta_description = self._generate_meta_description(topic, key_points)
        
        # Create sections structure
        sections = self._create_sections(topic, key_points)
        
        # Calculate estimated word count
        estimated_word_count = self._calculate_word_count(sections)
        
        outline = BlogOutline(
            title=self._generate_title(topic),
            meta_description=meta_description,
            sections=sections,
            target_keywords=keywords,
            estimated_word_count=estimated_word_count
        )
        
        self.update_context(
            metadata={
                "outline": outline,
                "meta_description": meta_description
            }
        )
        
        self.log(f"Content plan created for topic: {topic}", "success")
        return outline
    
    def _generate_title(self, topic: str) -> str:
        """Generate an SEO-friendly title for the blog post."""
        # Implement title generation logic
        # This is a placeholder implementation
        return f"The Complete Guide to {topic}: Strategies for 2024"
    
    def _generate_meta_description(self, topic: str, key_points: List[str]) -> str:
        """Generate an SEO-optimized meta description."""
        # Implement meta description generation logic
        # This is a placeholder implementation
        return f"Discover the latest insights and best practices for {topic}. Learn expert strategies for {', '.join(key_points[:2]).lower()} and more in this comprehensive guide."
    
    def _create_sections(self, topic: str, key_points: List[str]) -> List[Dict[str, Any]]:
        """Create a structured outline with sections and subsections."""
        sections = [
            {
                "title": "Introduction",
                "type": "section",
                "target_word_count": 200,
                "key_points": ["Context setting", "Problem statement", "Article overview"]
            }
        ]
        
        # Add main content sections based on key points
        for i, point in enumerate(key_points, 1):
            section = {
                "title": f"{point}",
                "type": "section",
                "target_word_count": 300,
                "subsections": [
                    {
                        "title": "Current Trends",
                        "type": "subsection",
                        "target_word_count": 150
                    },
                    {
                        "title": "Best Practices",
                        "type": "subsection",
                        "target_word_count": 150
                    }
                ]
            }
            sections.append(section)
        
        # Add conclusion section
        sections.append({
            "title": "Conclusion",
            "type": "section",
            "target_word_count": 200,
            "key_points": ["Summary of key points", "Future implications", "Call to action"]
        })
        
        return sections
    
    def _calculate_word_count(self, sections: List[Dict[str, Any]]) -> int:
        """Calculate estimated word count for the entire blog post."""
        total_words = 0
        
        for section in sections:
            total_words += section.get("target_word_count", 0)
            for subsection in section.get("subsections", []):
                total_words += subsection.get("target_word_count", 0)
        
        return total_words