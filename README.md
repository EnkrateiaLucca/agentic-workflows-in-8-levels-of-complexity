# Agentic Workflows in 8 Levels of Complexity

A comprehensive tutorial that progressively builds understanding of agentic workflows, from simple LLM calls to complex multi-agent systems.

## Overview

This repository contains a Jupyter notebook that demonstrates 8 increasingly sophisticated levels of agentic workflows:

1. **Simple LLM Call** - Basic interaction with an LLM
2. **Chaining LLM Calls** - Sequential processing through multiple prompts
3. **Routing LLM Calls** - Dynamic selection of processing paths
4. **LLMs + Functions in Prompt** - Including function definitions in prompts
5. **LLMs + Structured Outputs** - Using Pydantic models for structured responses
6. **LLMs + Function Calling** - Native function calling capabilities
7. **Agent Loop (ReAct)** - Implementing reasoning and action loops
8. **Agent as Step of Workflow** - Composing agents within larger workflows

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/[your-username]/agentic-workflows-in-8-levels-of-complexity.git
cd agentic-workflows-in-8-levels-of-complexity
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install jupyter notebook ipykernel
pip install openai
pip install pydantic
```

### 4. Set Up OpenAI API Key

You'll need an OpenAI API key to run the examples. The notebook will prompt you to enter it when needed, or you can set it as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook intro-agents-from-scratch.ipynb
```

## Running the Notebook

1. Open the notebook in Jupyter
2. Run cells sequentially from top to bottom
3. When prompted, enter your OpenAI API key
4. Follow along with each level of complexity

## Important Notes

- Files created during execution will be saved in your current working directory

## Files in This Repository

- `intro-agents-from-scratch.ipynb` - Main tutorial notebook
- `*.png` - Supporting diagrams and images
- Generated files from examples (e.g., `test.txt`, `ai-jokes.md`, etc.)

## Learning Path

Start with Level 1 and work your way through each level sequentially. Each level builds upon concepts from previous levels, gradually introducing more sophisticated patterns for building agentic systems.

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic's Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [ReAct Paper](https://arxiv.org/pdf/2210.03629)

## License

This project is for educational purposes. Please refer to the OpenAI usage policies when using their API.

## Contributing

Feel free to open issues or submit pull requests with improvements or corrections.