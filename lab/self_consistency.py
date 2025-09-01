# Self-consistency: The model solves a problem multiple independent ways, 
# then compares the answers to select the most consistent and reliable result.
# Benefit: Encourages critical thinking and verification, 
# improving accuracy for complex decision-making (e.g., testing the sister’s age problem through three separate calculations).
from service.print_service import print_model_response
from config import update_params
from service.llm_service import LLMService

def self_consistency(llm_serive):
    params = {
        "max_new_tokens": 512,
    }
    update_params(params)
    prompt = """When I was 6, my sister was half of my age. Now I am 70, what age is my sister?

                Provide three independent calculations and explanations, then determine the most consistent result.
    """
    response = llm_serive.generate(prompt, params)
    print(f"prompt: {prompt}\n")
    print(f"response : {response}\n")

