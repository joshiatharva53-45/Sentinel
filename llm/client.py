from ollama import Client


class OllamaClient:
    def __init__(self, host: str):
        self.client = Client(host=host)

    def chat(self, model: str, messages: list, options: dict | None = None) -> str:
        response = self.client.chat(
            model=model,
            messages=messages,
            options=options or {},
        )

        return response.message.content