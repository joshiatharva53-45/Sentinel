"""
voice/vad.py

Silero Voice Activity Detection wrapper.
Returns True when speech is detected.
"""

import numpy as np
from silero_vad import load_silero_vad, get_speech_timestamps


class VoiceActivityDetector:

    def __init__(
        self,
        sample_rate=16000,
        threshold=0.5,
        min_speech_duration_ms=100,
        min_silence_duration_ms=300,
    ):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.min_speech_duration_ms = min_speech_duration_ms
        self.min_silence_duration_ms = min_silence_duration_ms

        print("Loading Silero VAD...")
        self.model = load_silero_vad()
        print("Silero VAD Loaded")

    def is_speech(self, audio: np.ndarray) -> bool:
        """
        Returns True if speech is detected.
        """

        if len(audio) == 0:
            return False

        timestamps = get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=self.sample_rate,
            threshold=self.threshold,
            min_speech_duration_ms=self.min_speech_duration_ms,
            min_silence_duration_ms=self.min_silence_duration_ms,
        )

        return len(timestamps) > 0


vad = VoiceActivityDetector()