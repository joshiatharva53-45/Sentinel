"""
voice/worker.py

Background worker that consumes audio chunks from the queue
and forwards them to the processing pipeline.
"""

import threading
import time

from voice.queue import audio_queue
from voice.state import voice_state


class AudioWorker:

    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.thread = None

    def run(self):

        print("🎙️ Audio Worker Started")

        while voice_state.running:

            audio = audio_queue.get(timeout=0.1)

            if audio is None:
                continue

            try:
                self.pipeline.process(audio)

            except Exception as e:
                print(f"[Worker Error] {e}")

        print("🛑 Audio Worker Stopped")

    def start(self):

        if self.thread and self.thread.is_alive():
            return

        voice_state.set_running(True)

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

    def stop(self):

        voice_state.set_running(False)

        if self.thread:
            self.thread.join(timeout=2)

            self.thread = None