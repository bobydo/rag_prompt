# ollama_expression_service.py
"""
Service for formatting prompts and generating responses using Ollama backend.
"""
from service.llm_service import LLMService
from config import update_params

# Function to format prompt with variables
def format_prompt(template, variables):
    return template.format(**variables)

# Service function to generate response using formatted prompt
def generate_response(template, variables, params=None):
    prompt = format_prompt(template, variables)
    if params:
        update_params(params)
    llm = LLMService()
    return llm.generate(prompt)
