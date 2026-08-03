"""
core/assistant.py

High-level Sentinel Assistant.
"""

from __future__ import annotations

from conversation.response import Response

from core.engine import engine
from core.state import state
from core import constants


class Assistant:
    """
    Public interface for Sentinel.
    """

    def __init__(self):

        self.engine = engine

    # ---------------------------------------------------------

    def startup(self):

        self.engine.start()

        print(constants.WELCOME_MESSAGE)

        state.is_running = True

    # ---------------------------------------------------------

    def shutdown(self):

        self.engine.shutdown()

        state.is_running = False

        print(constants.GOODBYE_MESSAGE)

    # ---------------------------------------------------------

    def process(
        self,
        text: str,
    ) -> Response:

        state.last_command = text

        response = self.engine.process_text(text)

        print(f"\nSentinel > {response.text}\n")

        return response

    # ---------------------------------------------------------

    def process_audio(
        self,
        audio,
    ) -> Response:

        response = self.engine.process_audio(audio)

        print(f"\nSentinel > {response.text}\n")

        return response

    # ---------------------------------------------------------

    @property
    def config(self):

        return self.engine.config

    # ---------------------------------------------------------

    @property
    def logger(self):

        return self.engine.logger

    # ---------------------------------------------------------

    @property
    def event_bus(self):

        return self.engine.event_bus


#
# Global assistant instance
#

assistant = Assistant()