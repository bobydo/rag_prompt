from service.print_service import print_model_response

def classify_eiffel_tower(llm_service):
    prompt = """Classify the following statement as true or false: 
    'The Eiffel Tower is located in Berlin.'"""
    print_model_response(llm_service,prompt)
