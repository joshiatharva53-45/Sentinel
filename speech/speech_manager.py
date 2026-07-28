"""
speech/speech_manager.py

Manages all speech output for Sentinel.
"""

from __future__ import annotations

import threading

from core.lifecycle import Service
from core.logger import Logger

from speech.speech_queue import SpeechQueue
from speech.piper_engine import PiperEngine


class SpeechManager(Service):

    def __init__(
        self,
        logger: Logger,
        queue: SpeechQueue,
        piper: PiperEngine,
    ):
        super().__init__("SpeechManager")

        self.logger = logger
        self.queue = queue
        self.piper = piper

        self.worker = None

    # ---------------------------------------------------------

    def initialize(self):

        self.initialized = True

        self.logger.info("Speech Manager initialized.")

    # ---------------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.worker = threading.Thread(
            target=self.run,
            daemon=True,
        )

        self.worker.start()

        self.logger.info("Speech Manager started.")

    # ---------------------------------------------------------

    def run(self):

        while self.running:

            text = self.queue.get(timeout=0.2)

            if text is None:
                continue

            try:

                self.piper.speak(text)

            except Exception as e:

                self.logger.exception(e)

    # ---------------------------------------------------------

    def speak(self, text: str):

        self.queue.put(text)

    # ---------------------------------------------------------

    def stop(self):

        self.running = False

        self.queue.clear()

        self.piper.stop()

        if self.worker:

            self.worker.join(timeout=2)

            self.worker = None

        self.logger.info("Speech Manager stopped.")

    # ---------------------------------------------------------

    def shutdown(self):

        self.stop()

        self.initialized = False

        self.logger.info("Speech Manager shutdown.")

    # ---------------------------------------------------------

    def clear(self):

        self.queue.clear()

    # ---------------------------------------------------------

    def interrupt(self):

        self.clear()

        self.piper.stop()