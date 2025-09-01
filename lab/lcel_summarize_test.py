# lcel_summarize_test.py
"""
Test file for summarizing content using LangChain Expression Language (LCEL) with Ollama backend.
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

# Content to summarize
content = """
    The rapid advancement of technology in the 21st century has transformed various industries, including healthcare, education, and transportation. 
    Innovations such as artificial intelligence, machine learning, and the Internet of Things have revolutionized how we approach everyday tasks and complex problems. 
    For instance, AI-powered diagnostic tools are improving the accuracy and speed of medical diagnoses, while smart transportation systems are making cities more efficient and reducing traffic congestion. 
    Moreover, online learning platforms are making education more accessible to people around the world, breaking down geographical and financial barriers. 
    These technological developments are not only enhancing productivity but also contributing to a more interconnected and informed society.
"""

template = """Summarize the {content} in one sentence.
"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
llm = Ollama(model="llama3")
summarize_chain = (
    RunnableLambda(lambda variables: prompt.format(**variables))
    | llm
    | StrOutputParser()
)

# Run the chain
def main():
    summary = summarize_chain.invoke({"content": content})
    print(summary)

if __name__ == "__main__":
    main()
