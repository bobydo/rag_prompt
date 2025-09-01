params = {
    "max_new_tokens": 128,
    "min_new_tokens": 5,
    "temperature": 0.4,
    "top_p": 0.9,
    "top_k": 40
}

def get_params():
    return params

def update_params(new_params: dict):
    params.update(new_params)
