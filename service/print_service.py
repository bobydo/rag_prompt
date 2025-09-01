def print_model_response(llm_service, prompt):
    response = llm_service.generate(prompt, None)
    print(f"Prompt sent to model:\n{prompt}")
    print("Model response:")
    print("------------------")
    print(response if response else "[No response returned]")
    print("------------------")
