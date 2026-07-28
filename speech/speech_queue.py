"""
speech/speech_queue.py

Thread-safe speech queue for Piper.

Stores text waiting to be spoken.
"""

from queue import Queue, Empty


class SpeechQueue:

    def __init__(self, maxsize: int = 100):
        self._queue = Queue(maxsize=maxsize)

    # ---------------------------------------------------------

    def put(self, text: str):

        if not text:
            return

        try:
            self._queue.put_nowait(text)

        except Exception:
            # Queue full
            pass

    # ---------------------------------------------------------

    def get(self, timeout: float = 0.1):

        try:
            return self._queue.get(timeout=timeout)

        except Empty:
            return None

    # ---------------------------------------------------------

    def clear(self):

        while not self._queue.empty():

            try:
                self._queue.get_nowait()

            except Empty:
                break

    # ---------------------------------------------------------

    def empty(self):

        return self._queue.empty()

    # ---------------------------------------------------------

    def size(self):

        return self._queue.qsize()