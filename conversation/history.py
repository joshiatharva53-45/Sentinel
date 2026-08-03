"""
conversation/history.py
"""

from __future__ import annotations


class ConversationHistory:

    def __init__(self, max_messages: int = 20):

        self.max_messages = max_messages

        self.messages = []

    # ---------------------------------------------------------

    def add(
        self,
        role: str,
        content: str,
    ):

        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )

        if len(self.messages) > self.max_messages:

            self.messages = self.messages[-self.max_messages:]

    # ---------------------------------------------------------

    def clear(self):

        self.messages.clear()

    # ---------------------------------------------------------

    def last(self):

        if not self.messages:
            return None

        return self.messages[-1]

    # ---------------------------------------------------------

    def as_llm_messages(self):

        return list(self.messages)

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.messages)