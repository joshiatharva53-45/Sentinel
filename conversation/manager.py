"""
conversation/manager.py

Manages the lifecycle of the Conversation Runtime.
"""

from __future__ import annotations

import logging

from conversation.runtime import ConversationRuntime

logger = logging.getLogger(__name__)


class ConversationManager:
    """
    Controls the Conversation Runtime.
    """

    def __init__(
        self,
        event_bus,
        router=None,
        llm=None,
    ) -> None:

        self.runtime = ConversationRuntime(
            event_bus=event_bus,
            router=router,
            llm=llm,
        )

        self.running = False

    def start(self) -> None:
        """
        Start conversation runtime.
        """

        if self.running:
            return

        logger.info("Starting Conversation Runtime")

        self.running = True

    def stop(self) -> None:
        """
        Stop conversation runtime.
        """

        if not self.running:
            return

        logger.info("Stopping Conversation Runtime")

        self.running = False

    def restart(self) -> None:
        """
        Restart runtime.
        """

        self.stop()
        self.start()

    def process(self, text: str):
        """
        Process user speech.
        """

        if not self.running:
            raise RuntimeError(
                "Conversation Runtime is not running."
            )

        return self.runtime.process(text)