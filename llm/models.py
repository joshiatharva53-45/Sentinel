from dataclasses import dataclass


@dataclass(slots=True)
class ChatRequest:
    history: list
    user_message: str


@dataclass(slots=True)
class ChatResponse:
    text: str
    success: bool = True