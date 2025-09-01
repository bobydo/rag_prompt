from service.print_service import print_model_response
def get_wind_response(llm_service):
    prompt = "The wind is strong"
    print_model_response(llm_service,prompt)
