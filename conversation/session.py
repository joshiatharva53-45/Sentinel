"""
conversation/session.py
"""

from __future__ import annotations

from conversation.history import ConversationHistory


class ConversationSession:

    def __init__(self):

        self.history = ConversationHistory()

    # ---------------------------------------------------------

    def user(self, text: str):

        self.history.add(
            "user",
            text,
        )

    # ---------------------------------------------------------

    def assistant(self, text: str):

        self.history.add(
            "assistant",
            text,
        )

    # ---------------------------------------------------------

    def system(self, text: str):

        self.history.add(
            "system",
            text,
        )

    # ---------------------------------------------------------

    def reset(self):

        self.history.clear()