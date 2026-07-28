"""
speech/piper_engine.py

Production Piper TTS service.
"""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from core.lifecycle import Service
from core.config import Config
from core.logger import Logger

from speech.audio_player import AudioPlayer


class PiperEngine(Service):

    def __init__(
        self,
        config: Config,
        logger: Logger,
        player: AudioPlayer,
    ):
        super().__init__("Piper")

        self.config = config
        self.logger = logger
        self.player = player

    # ---------------------------------------------------------

    def initialize(self):

        cfg = self.config.piper

        if not cfg.piper_path.exists():
            raise FileNotFoundError(cfg.piper_path)

        self.initialized = True

        self.logger.info("Piper initialized.")

    # ---------------------------------------------------------

    def start(self):

        self.running = True

        self.logger.info("Piper service started.")

    # ---------------------------------------------------------

    def stop(self):

        self.running = False

        self.player.stop()

        self.logger.info("Piper service stopped.")

    # ---------------------------------------------------------

    def shutdown(self):

        self.player.stop()

        self.initialized = False

        self.logger.info("Piper shutdown complete.")

    # ---------------------------------------------------------

    def speak(self, text: str):

        if not text.strip():
            return

        cfg = self.config.piper

        model = cfg.voices_path / f"{cfg.voice}.onnx"

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ) as tmp:

            output = Path(tmp.name)

        command = [

            str(cfg.piper_path),

            "--model",
            str(model),

            "--output_file",
            str(output),

        ]

        self.logger.info(f"Speaking: {text}")

        subprocess.run(

            command,

            input=text,

            text=True,

            check=True,

            cwd=cfg.piper_path.parent,

        )

        self.player.play(output)

        try:
            output.unlink()

        except Exception:
            pass