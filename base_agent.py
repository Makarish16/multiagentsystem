from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from rich.console import Console
from colorama import Fore, Style

@dataclass
class AgentContext:
    """Shared context between agents containing task-related information."""
    topic: str
    keywords: List[str]
    target_word_count: int
    timestamp: datetime = datetime.now()
    metadata: Dict[str, Any] = None

class BaseAgent(ABC):
    """Abstract base class for all agents in the HR blog generation system."""
    
    def __init__(self, name: str, context: Optional[AgentContext] = None):
        self.name = name
        self.context = context or AgentContext(
            topic="",
            keywords=[],
            target_word_count=2000
        )
        self.console = Console()
        
    def log(self, message: str, level: str = "info") -> None:
        """Log messages with color-coded severity levels."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = {
            "info": Fore.BLUE,
            "warning": Fore.YELLOW,
            "error": Fore.RED,
            "success": Fore.GREEN
        }.get(level, Fore.WHITE)
        
        print(f"{color}[{timestamp}] {self.name}: {message}{Style.RESET_ALL}")
    
    @abstractmethod
    async def execute(self, *args, **kwargs) -> Any:
        """Execute the agent's primary task.
        
        This method must be implemented by all concrete agent classes.
        Returns the result of the agent's execution.
        """
        pass
    
    def update_context(self, **kwargs) -> None:
        """Update the agent's context with new information."""
        for key, value in kwargs.items():
            if hasattr(self.context, key):
                setattr(self.context, key, value)
            elif self.context.metadata is None:
                self.context.metadata = {key: value}
            else:
                self.context.metadata[key] = value
    
    def get_context_value(self, key: str) -> Any:
        """Retrieve a value from the agent's context."""
        if hasattr(self.context, key):
            return getattr(self.context, key)
        return self.context.metadata.get(key) if self.context.metadata else None