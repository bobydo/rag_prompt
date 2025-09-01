# app_llm.py
from service.prompt_registry import PromptRegistry, FSBackend
from service.llm_service import LLMService  # your existing class

reg = PromptRegistry(FSBackend(root="prompts"))
llm = LLMService(model="llama3")  # or llama3.1:8b, etc.

# Example: summarizer latest
prompt = reg.render("summarizer", {"text": "Write a concise summary of LangChain."})
result = llm.generate(prompt)
print(result)

# Example: joke_writer v1
prompt = reg.render("joke_writer", {"adjective": "dry", "content": "databases"}, version="v1")
print(llm.generate(prompt))
