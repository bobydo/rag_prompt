#LCEL gives you quality of the whole system (composition, reliability, maintainability).
#Use LCEL when your workflow has steps; stick to simple calls when it doesn’t.
from service.print_service import print_model_response
from config import update_params
from service.llm_service import LLMService

def LCEL(adjective, content):
    params = {
        "max_new_tokens": 256,
        "temperature": 0.5
    }
    update_params(params)
    prompt = f"Tell me a {adjective} joke about {content}."
    llm = LLMService()
    response = llm.generate(prompt)
    print(f"prompt: {prompt}\n")
    print(f"response : {response}\n")