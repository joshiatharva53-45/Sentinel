"""
conversation/history.py

Stores the active conversation history.
This is NOT long-term memory.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Message:
    """
    Represents one conversation message.
    """

    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)


class ConversationHistory:
    """
    Stores messages for the current conversation only.
    """

    def __init__(self) -> None:
        self._messages: list[Message] = []

    def add(
        self,
        role: str,
        content: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Add a message to history.
        """

        self._messages.append(
            Message(
                role=role,
                content=content,
                metadata=metadata or {},
            )
        )

    def clear(self) -> None:
        """
        Remove all messages.
        """

        self._messages.clear()

    def count(self) -> int:
        """
        Number of stored messages.
        """

        return len(self._messages)

    def messages(self) -> list[Message]:
        """
        Return a copy of all messages.
        """

        return list(self._messages)

    def last(self) -> Message | None:
        """
        Return the most recent message.
        """

        if not self._messages:
            return None

        return self._messages[-1]

    def as_llm_messages(self) -> list[dict[str, str]]:
        """
        Convert history into the standard LLM message format.
        """

        return [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in self._messages
        ]