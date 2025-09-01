# Prompt Engineer Python Project

This project demonstrates in-context learning and prompt engineering techniques in Python. 

## Getting Started
1. Ensure you have Python 3.7+ and https://ollama.com/windows installed.
2. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ollama pull llama3
   ollama serve
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the main demo:
   ```powershell
   python main.py
   ```
## Dev vs Prod management (LCEL)
- `service/langchain_ollama_service.py`: Integrates LangChain's pipe (`|`) chaining with Ollama as the backend. Example usage:
   ```python
   from service.langchain_ollama_service import joke_chain
   response = joke_chain.invoke({"adjective": "funny", "content": "chickens"})
   print(response)
   ```

- `lab/chain_factory.py`: Factory for creating LangChain chains using prompt templates and Ollama as backend. Use `make_chain(key, version, model)` to build a chain from registered prompts. Example:
   ```python
   chain = make_chain("summarizer")
   chain.invoke({"text": "..."})
   ```

- `app_llm.py`: Example app for using registered prompts and LLMService. Renders prompts from registry and generates responses with Ollama. Example:
   ```python
   prompt = reg.render("summarizer", {"text": "Write a concise summary of LangChain."})
   result = llm.generate(prompt)

- `service/prompt_registry.py`: Registry and backend for managing prompt templates. Supports file system (FSBackend) for development and database (DBBackend) for production. Use `PromptRegistry` to fetch and render prompts by key and version. Example:
   ```python
   reg = PromptRegistry(FSBackend("prompts"))
   prompt = reg.render("summarizer", {"text": "Write a summary."})
   ```

- `service/ollama_expression_service.py`: Provides functions for formatting prompts and generating responses using Ollama as the backend. Use `format_prompt` for prompt composition and `generate_response` to get model output.

- `service/ollama_joke_chain_service.py`: Implements a chain-like workflow for joke generation. Chains prompt formatting, LLM response, and output parsing. Use `joke_chain(template, variables, params)` to run the chain.

- `service/langchain_ollama_service.py`: Integrates LangChain's pipe (`|`) chaining with Ollama as the backend. Example usage:
   ```python
   from service.langchain_ollama_service import joke_chain
   response = joke_chain.invoke({"adjective": "funny", "content": "chickens"})
   print(response)
   ```

