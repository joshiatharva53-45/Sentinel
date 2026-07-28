from dataclasses import dataclass


@dataclass(slots=True)
class LLMConfig:
    model: str = "qwen2.5:7b"
    host: str = "http://localhost:11434"
    temperature: float = 0.7
    max_tokens: int = 1024