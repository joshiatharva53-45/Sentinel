"""
Thread-safe Audio Buffer
"""

from queue import Queue


class AudioBuffer:

    def __init__(self):
        self.queue = Queue()

    def put(self, audio):
        self.queue.put(audio)

    def get(self):
        if self.queue.empty():
            return None
        return self.queue.get()

    def empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()


audio_buffer = AudioBuffer()