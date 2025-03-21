# HR Blog Multi-Agent System

A Python-based multi-agent system that generates high-quality, SEO-optimized blog posts on trending HR topics. The system uses a modular architecture with specialized agents that work together to research, plan, generate, and optimize content.

## System Architecture

The system consists of four specialized agents:

1. **Research Agent**: Finds trending HR topics and gathers relevant information from reliable sources.
2. **Content Planning Agent**: Creates structured outlines based on research findings.
3. **Content Generation Agent**: Writes comprehensive blog posts following the planned outline.
4. **SEO Optimization Agent**: Ensures content follows SEO best practices and optimizes for target keywords.

### Agent Workflow

1. The Research Agent searches for trending HR topics and collects relevant information.
2. The Content Planning Agent creates a structured outline with sections and subsections.
3. The Content Generation Agent writes the blog post following the outline and research data.
4. The SEO Optimization Agent optimizes the content for search engines and readability.

## Features

- Automated research on trending HR topics
- SEO-optimized content generation
- Structured content planning
- Keyword optimization and density analysis
- Readability scoring and optimization
- Comprehensive metadata generation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hr-blog-mas.git
cd hr-blog-mas
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Import the orchestrator:
```python
from hr_blog_agents.orchestrator import BlogGenerationOrchestrator
```

2. Create an instance:
```python
orchestrator = BlogGenerationOrchestrator(target_word_count=2000)
```

3. Generate a blog post:
```python
# Generate post on a specific topic
result = await orchestrator.generate_blog_post(topic="Remote Work Best Practices")

# Or let the system find a trending topic
result = await orchestrator.generate_blog_post()
```

## Dependencies

- langchain: Agent development and orchestration
- beautifulsoup4: Web scraping
- requests: HTTP requests
- nltk: Natural language processing
- pandas: Data manipulation
- python-slugify: URL-friendly string generation
- colorama: Terminal output formatting
- rich: Rich text and formatting in terminal
- tqdm: Progress bars

## Development

- Written in Python 3.8+
- Uses async/await for efficient execution
- Modular architecture for easy extension
- Comprehensive logging and error handling
- Type hints for better code maintainability

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request