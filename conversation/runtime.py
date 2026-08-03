"""
conversation/runtime.py

Main conversation runtime.
Receives recognized speech, dispatches it, and returns a response.
"""

from __future__ import annotations

import logging

from conversation.dispatcher import ConversationDispatcher
from conversation.events import ConversationEvent
from conversation.response import Response
from conversation.session import ConversationSession
from conversation.state import ConversationState

logger = logging.getLogger(__name__)


class ConversationRuntime:
    """
    Main conversation runtime.
    """

    def __init__(
        self,
        event_bus,
        router=None,
        llm=None,
    ) -> None:

        self.event_bus = event_bus

        self.session = ConversationSession()

        self.dispatcher = ConversationDispatcher(
            router=router,
            llm=llm,
        )

    def process(self, text: str) -> Response:
        """
        Process recognized speech.
        """

        logger.info("Conversation Runtime: %s", text)

        self.session.touch()

        self.session.state = ConversationState.PROCESSING

        self.event_bus.emit(
            ConversationEvent.STATE_CHANGED.value,
            self.session.state,
        )

        self.event_bus.emit(
            ConversationEvent.USER_SPEECH_RECOGNIZED.value,
            text,
        )

        response = self.dispatcher.dispatch(
            text=text,
            history=self.session.history.as_llm_messages(),
        )

        if response.success:

            self.session.history.add(
                role="user",
                content=text,
            )

            self.session.history.add(
                role="assistant",
                content=response.text,
            )

        self.session.state = ConversationState.RESPONDING

        self.event_bus.emit(
            ConversationEvent.RESPONSE_READY.value,
            response,
        )

        return response

    def reset(self) -> None:
        """
        Reset conversation.
        """

        self.session.reset()

    def history(self):
        """
        Return conversation history.
        """

        return self.session.history.as_llm_messages()