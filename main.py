from service.llm_service import LLMService
from lab.wind import get_wind_response
from lab.classify import classify_eiffel_tower
from service.print_service import print_model_response
from lab.one_shot import one_shot

# zero and few shots examples
prompts = [
    "Translate to French: 'I love programming.'",
    "Summarize in 2 bullet points, each ≤10 words: 'The ability of LLMs to learn from examples provided inside the prompt at inference time (no fine-tuning).'"
]

if __name__ == "__main__":
    llm_service = LLMService()
    #get_wind_response(llm_service)
    #classify_eiffel_tower(llm_service)
    #for prompt in prompts:
    #    print_model_response(llm_service,prompt)
    one_shot(llm_service)
