# lcel_custom_format.py
"""
Starter code for custom product review analysis using LCEL and an LLM.
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

def lcel_custom_format():
    # Use these parameters (not used directly in Ollama's LangChain integration, but shown for reference)
    parameters = {
        "max_new_tokens": 512,
        "temperature": 0.2,
    }

    # TODO: Initialize your LLM
    llm = Ollama(model="llama3")

    # Example template for product review analysis
    template = """
    Analyze the following product review:
    "{review}"

    Provide your analysis in the following format:
    - Sentiment: (positive, negative, or neutral)
    - Key Features Mentioned: (list the product features mentioned)
    - Summary: (one-sentence summary)
    """

    # TODO: Create your prompt template
    product_review_prompt = PromptTemplate.from_template(template)

    # TODO: Create a formatting function
    def format_review_prompt(variables):
        return product_review_prompt.format(**variables)

    # TODO: Build your LCEL chain
    review_analysis_chain = (
        RunnableLambda(format_review_prompt)
        | llm
        | StrOutputParser()
    )

    # Example reviews to process
    reviews = [
        "I love this smartphone! The camera quality is exceptional and the battery lasts all day. The only downside is that it heats up a bit during gaming.",
        "This laptop is terrible. It's slow, crashes frequently, and the keyboard stopped working after just two months. Customer service was unhelpful."
    ]

    # TODO: Process the reviews
    for review in reviews:
        result = review_analysis_chain.invoke({"review": review})
        print(result)
