"""
Sentinel Ollama Chat Client
"""

from __future__ import annotations

import requests


class Ollama:

    def __init__(
        self,
        model: str = "qwen2.5:7b",
        host: str = "http://localhost:11434",
    ):

        self.model = model
        self.url = f"{host}/api/chat"

        self.system_prompt = (
            "You are Sentinel, an offline AI assistant. "
            "You are concise, intelligent, helpful and proactive. "
            "Never say you are ChatGPT or another assistant. "
            "Answer naturally."
        )

    def chat(
        self,
        history: list[dict],
        user_message: str,
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]

        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

            return data["message"]["content"].strip()

        except Exception as e:

            return f"Ollama Error: {e}"