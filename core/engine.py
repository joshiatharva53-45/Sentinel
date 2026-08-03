"""
core/engine.py

Sentinel Application Engine
"""

from __future__ import annotations

from conversation.response import Response

from core.bootstrap import Bootstrapper


class Engine:
    """
    Main application engine.

    Owns the dependency container and exposes the public
    interface used by the rest of Sentinel.
    """

    def __init__(self):

        bootstrap = Bootstrapper()

        self.container = bootstrap.configure()

        self.registry = self.resolve("registry")

        self.pipeline = self.resolve("pipeline")

        self.running = False

    # ---------------------------------------------------------
    # Dependency Resolution
    # ---------------------------------------------------------

    def resolve(
        self,
        name: str,
    ):

        return self.container.resolve(name)

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    def initialize(self):

        self.registry.initialize()

    # ---------------------------------------------------------

    def start(self):

        if self.running:
            return

        self.initialize()

        self.registry.start()

        conversation = self.resolve("conversation")
        conversation.start()

        self.running = True

    # ---------------------------------------------------------

    def stop(self):

        if not self.running:
            return

        conversation = self.resolve("conversation")
        conversation.stop()

        self.registry.stop()

        self.running = False

    # ---------------------------------------------------------

    def shutdown(self):

        if self.running:
            self.stop()

        self.registry.shutdown()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def process_text(
        self,
        text: str,
    ) -> Response:

        if not self.running:
            raise RuntimeError(
                "Engine is not running."
            )

        return self.pipeline.process_text(text)

    # ---------------------------------------------------------

    def process_audio(
        self,
        audio,
    ) -> Response:

        if not self.running:
            raise RuntimeError(
                "Engine is not running."
            )

        return self.pipeline.process_audio(audio)

    # ---------------------------------------------------------

    def chat(
        self,
        text: str,
    ) -> Response:

        return self.process_text(text)

    # ---------------------------------------------------------
    # Convenience Properties
    # ---------------------------------------------------------

    @property
    def config(self):

        return self.resolve("config")

    # ---------------------------------------------------------

    @property
    def logger(self):

        return self.resolve("logger")

    # ---------------------------------------------------------

    @property
    def event_bus(self):

        return self.resolve("event_bus")

    # ---------------------------------------------------------

    @property
    def whisper(self):

        return self.resolve("whisper")

    # ---------------------------------------------------------

    @property
    def speech(self):

        return self.resolve("speech")

    # ---------------------------------------------------------

    @property
    def llm(self):

        return self.resolve("llm")

    # ---------------------------------------------------------

    @property
    def conversation(self):

        return self.resolve("conversation")

    # ---------------------------------------------------------

    @property
    def ai_pipeline(self):

        return self.pipeline


#
# Global engine instance
#

engine = Engine()