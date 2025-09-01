# chain_factory.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from service.prompt_registry import PromptRegistry, FSBackend

reg = PromptRegistry(FSBackend("prompts"))

def make_chain(key: str, version: str | None = None, model: str = "llama3"):
    # Store full conversation template as one file or split lines by delimiter
    tmpl = reg.get(key, version)  # full text with {variables}
    prompt = ChatPromptTemplate.from_messages([("system", tmpl)])
    return prompt | ChatOllama(model=model) | StrOutputParser()

# usage:
# chain = make_chain("summarizer")
# chain.invoke({"text": "..."})
