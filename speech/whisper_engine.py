"""
speech/whisper_engine.py

Production Faster-Whisper service.
"""

from __future__ import annotations

import numpy as np
from faster_whisper import WhisperModel

from core.lifecycle import Service
from core.config import Config
from core.logger import Logger


class WhisperEngine(Service):

    def __init__(
        self,
        config: Config,
        logger: Logger,
    ):
        super().__init__("Whisper")

        self.config = config
        self.logger = logger

        self.model = None

    # ---------------------------------------------------------

    def initialize(self):

        cfg = self.config.whisper

        self.logger.info(
            f"Loading Whisper ({cfg.model_size})..."
        )

        self.model = WhisperModel(
            model_size_or_path=cfg.model_size,
            device=cfg.device,
            compute_type=cfg.compute_type,
        )

        self.initialized = True

        self.logger.info("Whisper loaded successfully.")

    # ---------------------------------------------------------

    def start(self):
        self.running = True
        self.logger.info("Whisper service started.")

    # ---------------------------------------------------------

    def stop(self):
        self.running = False
        self.logger.info("Whisper service stopped.")

    # ---------------------------------------------------------

    def shutdown(self):

        self.model = None

        self.initialized = False

        self.logger.info("Whisper unloaded.")

    # ---------------------------------------------------------

    def transcribe(
        self,
        audio: np.ndarray,
    ) -> str:

        if self.model is None:
            raise RuntimeError(
                "Whisper model not initialized."
            )

        segments, info = self.model.transcribe(
            audio,
            language=self.config.whisper.language,
            beam_size=5,
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return text.strip()