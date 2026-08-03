"""
core/bootstrap.py

Application Composition Root.
"""

from __future__ import annotations

from core.container import ServiceContainer
from core.config import Config
from core.logger import Logger
from core.event_bus import EventBus
from core.service_registry import ServiceRegistry
from core.router import router

from speech.audio_player import AudioPlayer
from speech.speech_queue import SpeechQueue
from speech.whisper_engine import WhisperEngine
from speech.piper_engine import PiperEngine
from speech.speech_manager import SpeechManager

from llm.engine import LLMEngine

from conversation.manager import ConversationManager

from pipeline.ai_pipeline import AIPipeline


class Bootstrapper:
    """
    Creates and wires the entire Sentinel application.
    """

    def __init__(self):

        self.container = ServiceContainer()

    # ---------------------------------------------------------

    def configure(self) -> ServiceContainer:

        #
        # Infrastructure
        #

        config = Config()

        logger = Logger()

        event_bus = EventBus()

        registry = ServiceRegistry()

        #
        # Speech
        #

        player = AudioPlayer()

        speech_queue = SpeechQueue()

        whisper = WhisperEngine(
            config=config,
            logger=logger,
        )

        piper = PiperEngine(
            config=config,
            logger=logger,
            player=player,
        )

        speech = SpeechManager(
            logger=logger,
            queue=speech_queue,
            piper=piper,
        )

        #
        # AI
        #

        llm = LLMEngine(
            config.llm,
        )

        conversation = ConversationManager(
            event_bus=event_bus,
            router=router,
            llm=llm,
        )

        pipeline = AIPipeline(
            conversation=conversation,
            speech=speech,
            whisper=whisper,
            event_bus=event_bus,
            logger=logger,
        )

        #
        # Register infrastructure
        #

        self.container.register_singleton(
            "config",
            config,
        )

        self.container.register_singleton(
            "logger",
            logger,
        )

        self.container.register_singleton(
            "event_bus",
            event_bus,
        )

        self.container.register_singleton(
            "registry",
            registry,
        )

        #
        # Register speech
        #

        self.container.register_singleton(
            "player",
            player,
        )

        self.container.register_singleton(
            "speech_queue",
            speech_queue,
        )

        self.container.register_singleton(
            "whisper",
            whisper,
        )

        self.container.register_singleton(
            "piper",
            piper,
        )

        self.container.register_singleton(
            "speech",
            speech,
        )

        #
        # Register AI
        #

        self.container.register_singleton(
            "llm",
            llm,
        )

        self.container.register_singleton(
            "conversation",
            conversation,
        )

        self.container.register_singleton(
            "pipeline",
            pipeline,
        )

        #
        # Lifecycle services
        #

        registry.register(whisper)

        registry.register(piper)

        registry.register(speech)

        return self.container