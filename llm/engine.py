from llm.client import OllamaClient
from llm.config import LLMConfig


class LLMEngine:

    def __init__(self, config: LLMConfig):

        self.config = config

        self.client = OllamaClient(config.host)

    def generate(
        self,
        history: list,
        user_message: str,
    ) -> str:

        messages = list(history)

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        return self.client.chat(
            model=self.config.model,
            messages=messages,
            options={
                "temperature": self.config.temperature,
                "num_predict": self.config.max_tokens,
            },
        )