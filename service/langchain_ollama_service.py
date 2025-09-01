# langchain_ollama_service.py
"""
Service for chaining prompt formatting and response generation using LangChain with Ollama as backend.
Requires: langchain, langchain_community, ollama
Install with:
    pip install langchain langchain_community ollama
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

# Create Ollama LLM instance
llm = Ollama(model="llama3")

# Function to format prompt with variables
def format_prompt(variables):
    template = "Tell me a {adjective} joke about {content}."
    return template.format(**variables)

# Create the chain with explicit formatting
joke_chain = (
    RunnableLambda(format_prompt)
    | llm
    | StrOutputParser()
)

def get_joke(adjective, content):
    variables = {"adjective": adjective, "content": content}
    return joke_chain.invoke(variables)
