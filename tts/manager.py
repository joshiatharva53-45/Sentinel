from __future__ import annotations

import queue
import threading

from tts.speaker import speaker

from voice.state import voice_state


class TTSManager:

    def __init__(self):

        self.queue = queue.Queue()

        self.worker = threading.Thread(
            target=self._worker,
            daemon=True,
        )

        self.worker.start()

    def _worker(self):

        while True:

            text = self.queue.get()

            if text is None:
                break

            try:
                voice_state.pause()
                speaker.speak(text)
            finally:
                voice_state.resume()
                self.queue.task_done()

    def say(self, text: str):

        if text:
            self.queue.put(text)

    def wait(self):

        self.queue.join()

    def shutdown(self):

        self.queue.put(None)
        self.worker.join()


tts = TTSManager()