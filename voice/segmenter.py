"""
Speech Segmenter
"""

import numpy as np

from voice.vad import vad


class SpeechSegmenter:

    def __init__(self):

        self.buffer = []

    def process(self, chunk):

        audio = chunk.flatten()

        if vad.detect(audio):

            self.buffer.append(audio)

            return None

        if len(self.buffer) == 0:
            return None

        speech = np.concatenate(self.buffer)

        self.buffer.clear()

        return speech


segmenter = SpeechSegmenter()