"""
core/bootstrap.py

Application Composition Root.

Responsible for:
- Creating services
- Registering services
- Wiring dependencies
"""

from core.container import ServiceContainer

from core.config import Config

from core.logger import Logger

from speech.whisper_engine import WhisperEngine

logger = Logger()

config = Config()

whisper = WhisperEngine(
    config=config,
    logger=logger,
)


class Bootstrapper:

    def __init__(self):
        self.container = ServiceContainer()

    def configure(self) -> ServiceContainer:
        """
        Register every application service here.
        """

        #
        # Infrastructure
        #

        self.container.register_singleton(
            "config",
            config,
        )

        self.container.register_singleton(
            "logger",
            logger,
        )

        # self.container.register_singleton(
        #     "event_bus",
        #     EventBus()
        # )

        #
        # AI
        #

        self.container.register_singleton(
            "whisper",
            whisper,
        )

        # self.container.register_singleton(
        #     "tts",
        #     PiperEngine(...)
        # )

        #
        # Voice
        #

        # self.container.register_singleton(
        #     "voice",
        #     VoiceManager(...)
        # )

        #
        # Memory
        #

        # self.container.register_singleton(
        #     "memory",
        #     MemoryManager(...)
        # )

        #
        # Conversation
        #

        # self.container.register_singleton(
        #     "conversation",
        #     ConversationManager(...)
        # )

        return self.container