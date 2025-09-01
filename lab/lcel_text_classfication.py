from service.print_service import print_model_response
from config import update_params
from service.llm_service import LLMService
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

def lcel_text_classfication():
    llm = LLMService()
    text = """
        The concert last night was an exhilarating experience with outstanding performances by all artists.
    """

    categories = "Entertainment, Food and Dining, Technology, Literature, Music."

    template = """
        Classify the {text} into one of the {categories}.
        
        Category:
    """
    prompt = PromptTemplate.from_template(template)
    llm = Ollama(model="llama3")
    classification_chain = (
        RunnableLambda(lambda variables: prompt.format(**variables))
        | llm
        | StrOutputParser()
    )
    category = classification_chain.invoke({"text": text, "categories": categories})
    print(category)