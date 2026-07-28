"""
conversation/state.py

Defines all conversation runtime states.
This module contains no business logic.
"""

from enum import Enum, auto


class ConversationState(Enum):
    """Conversation runtime states."""

    STARTING = auto()
    IDLE = auto()
    LISTENING = auto()
    PROCESSING = auto()
    PLANNING = auto()
    EXECUTING = auto()
    RESPONDING = auto()
    SPEAKING = auto()
    INTERRUPTED = auto()
    ERROR = auto()
    STOPPING = auto()

    def __str__(self) -> str:
        return self.name