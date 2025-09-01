from service.print_service import print_model_response
from config import update_params

def few_shot(llm_serive):
    # Update max_new_tokens using date_params
    date_params = {
        "max_new_tokens": 10
    }
    update_params(date_params)

    prompt = """Here are few examples of classifying emotions in statements:

                Statement: 'I just won my first marathon!'
                Emotion: Joy
                
                Statement: 'I can't believe I lost my keys again.'
                Emotion: Frustration
                
                Statement: 'My best friend is moving to another country.'
                Emotion: Sadness
                
                Now, classify the emotion in the following statement:
                Statement: 'That movie was so scary I had to cover my eyes.’
                
    """
    print_model_response(llm_serive,prompt)

