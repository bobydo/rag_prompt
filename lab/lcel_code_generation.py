from service.print_service import print_model_response
from config import update_params
from service.llm_service import LLMService
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

def lcel_code_generation():
    description = """
        Retrieve the names and email addresses of all customers from the 'customers' table who have made a purchase in the last 30 days. 
        The table 'purchases' contains a column 'purchase_date'
    """

    template = """
        Generate an SQL query based on the {description}
        
        SQL Query:
        
    """
    prompt = PromptTemplate.from_template(template)
    llm = Ollama(model="llama3")
    # Create the LCEL chain
    sql_generation_chain = (
        RunnableLambda(lambda variables: prompt.format(**variables)) 
        | llm 
        | StrOutputParser()
    )

    # Run the chain
    sql_query = sql_generation_chain.invoke({"description": description})
    print(sql_query)