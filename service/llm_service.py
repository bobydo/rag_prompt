import requests, json

class OllamaLLM:
    def __init__(self, model, host):
        self.model = model
        self.host = host

class LLMService:
    def __init__(self, model="llama3", host="http://localhost:11434"):
        self.ollama_llm = OllamaLLM(model=model, host=host)
    def generate(self, prompt: str, params=None) -> str:
        buf = []
        payload = {"model": self.ollama_llm.model, "prompt": prompt, "stream": True}
        try:
            if params:
                payload.update(params)
            with requests.post(
                f"{self.ollama_llm.host}/api/generate",
                json=payload,
                stream=True, timeout=120
            ) as r:
                r.raise_for_status() # only throws if not in 2XX
                for linebreak  in r.iter_lines():
                    if not linebreak:
                        continue
                    chunk = json.loads(linebreak.decode("utf-8"))
                    buf.append(chunk.get("response", ""))
            return "".join(buf).strip()
        except requests.exceptions.HTTPError as e:
            print(f"[HTTP error] {e}")
        except requests.exceptions.ConnectionError:
            print("[Connection error] Is Ollama running?")
        except requests.exceptions.Timeout:
            print("[Timeout] Ollama didn’t respond in time.")
        except Exception as e:
            print(f"[Unexpected error] {e}")

