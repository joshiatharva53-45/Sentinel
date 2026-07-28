"""
voice/stream.py

Continuously captures microphone audio and sends it
to the shared audio queue.
"""

import sounddevice as sd
import numpy as np

from voice.queue import audio_queue
from voice.state import voice_state


class AudioStream:

    def __init__(
        self,
        sample_rate=16000,
        channels=1,
        block_size=1600,
        device=None,
    ):
        self.sample_rate = sample_rate
        self.channels = channels
        self.block_size = block_size
        self.device = device

        self.stream = None

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        if not voice_state.running:
            return

        audio = np.copy(indata[:, 0])

        audio_queue.put(audio)

    def start(self):

        if self.stream is not None:
            return

        voice_state.set_running(True)

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            blocksize=self.block_size,
            dtype="float32",
            callback=self.callback,
            device=self.device,
        )

        self.stream.start()

        print("🎤 Microphone stream started")

    def stop(self):

        voice_state.set_running(False)

        if self.stream:

            self.stream.stop()
            self.stream.close()
            self.stream = None

            print("🛑 Microphone stream stopped")