"""
Test file for question answering using LangChain Expression Language (LCEL) with Ollama backend.
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

def lcel_qa_test():
    content = """
        The solar system consists of the Sun, eight planets, their moons, dwarf planets, and smaller objects like asteroids and comets. 
        The inner planets—Mercury, Venus, Earth, and Mars—are rocky and solid. 
        The outer planets—Jupiter, Saturn, Uranus, and Neptune—are much larger and gaseous.
    """

    question = "Which planets in the solar system are rocky and solid?"

    template = """
        Answer the {question} based on the {content}.
        Respond "Unsure about answer" if not sure about the answer.
        
        Answer:
        
    """
    prompt = PromptTemplate.from_template(template)

    llm = Ollama(model="llama3")
    qa_chain = (
        RunnableLambda(lambda variables: prompt.format(**variables))
        | llm
        | StrOutputParser()
    )

    answer = qa_chain.invoke({"question": question, "content": content})
    print(f"Answer the {question} based on the {content}.\n\nAnswer:\n{answer}")
