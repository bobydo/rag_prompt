#CoT is particularly effective for mathematical problems, logical reasoning,
#  and complex decision-making tasks.
from service.print_service import print_model_response
from config import update_params

def CoT(llm_service):
    params = {
    "max_new_tokens": 512,
    "temperature": 0.5,
    }
    update_params(params)
    prompt = """Consider the problem: 'A store had 22 apples. They sold 15 apples today and got a new delivery of 8 apples. 
                How many apples are there now?’

                Break down each step of your calculation

    """
    print_model_response(llm_service,prompt)

    # 1. Prompt for decision-making process
    decision_making_prompt = """A student has a test in two days. Think step by step about whether the student should study tonight or go to a movie with friends.
    In your reasoning, 
    consider factors such as 
    how well they already understand the material, 
    how important the test is for their grade, 
    how much time they will have to study tomorrow, 
    and the benefits of relaxing with friends. Then give your final recommendation."""

    # 2. Prompt for explaining a process
    sandwich_making_prompt = """Explain, step by step, the process of making a peanut butter and jelly sandwich. 
    In your reasoning, consider all the small details: 
    what ingredients and tools are needed, 
    how to prepare the bread, 
    how to spread the peanut butter and jelly evenly, 
    how to assemble the sandwich, and how to serve it. 
    Make sure each step is clear and in order."""

    responses = {}
    responses["decision_making"] = llm_service.generate(decision_making_prompt)
    responses["sandwich_making"] = llm_service.generate(decision_making_prompt)

    for prompt_type, response in responses.items():
        print(f"=== {prompt_type.upper()} RESPONSE ===")
        print(response)
        print()