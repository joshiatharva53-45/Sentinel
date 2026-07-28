"""
voice/queue.py

Thread-safe audio queue.

The microphone only pushes audio into this queue.
The worker consumes it.
"""

from queue import Queue, Empty
import numpy as np


class AudioQueue:

    def __init__(self, maxsize=100):
        self.queue = Queue(maxsize=maxsize)

    def put(self, audio: np.ndarray):
        """Push microphone audio into queue."""
        try:
            self.queue.put_nowait(audio)
        except Exception:
            # Queue full
            pass

    def get(self, timeout=0.1):
        """Get next chunk."""
        try:
            return self.queue.get(timeout=timeout)
        except Empty:
            return None

    def clear(self):
        """Remove all queued audio."""
        while not self.queue.empty():
            try:
                self.queue.get_nowait()
            except Empty:
                break

    def size(self):
        return self.queue.qsize()


audio_queue = AudioQueue()