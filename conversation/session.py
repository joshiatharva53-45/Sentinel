"""
conversation/session.py

Represents one active conversation session.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from uuid import uuid4

from conversation.history import ConversationHistory
from conversation.state import ConversationState


@dataclass(slots=True)
class ConversationSession:
    """
    Represents one active conversation.
    """

    timeout_seconds: int = 30

    session_id: str = field(default_factory=lambda: str(uuid4()))

    state: ConversationState = ConversationState.IDLE

    history: ConversationHistory = field(
        default_factory=ConversationHistory
    )

    started_at: datetime = field(default_factory=datetime.now)

    last_activity: datetime = field(default_factory=datetime.now)

    def touch(self) -> None:
        """
        Update last activity timestamp.
        """

        self.last_activity = datetime.now()

    def reset(self) -> None:
        """
        Reset the conversation.
        """

        self.history.clear()

        self.state = ConversationState.IDLE

        self.started_at = datetime.now()

        self.touch()

    def expired(self) -> bool:
        """
        Check whether the session has timed out.
        """

        return (
            datetime.now() - self.last_activity
        ) > timedelta(seconds=self.timeout_seconds)