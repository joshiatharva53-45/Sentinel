"""
voice/pipeline.py

Voice Processing Pipeline

Worker
   ↓
Pipeline
   ↓
Rolling Buffer
   ↓
Silero VAD
   ↓
Speech Buffer
   ↓
Whisper
"""

import numpy as np

from voice.vad import vad
from voice.state import voice_state


class VoicePipeline:

    def __init__(self):

        self.window_size = 16000          # 1 second
        self.chunk_size = 1600            # 100 ms

        self.rolling_buffer = np.array([], dtype=np.float32)
        self.speech_buffer = np.array([], dtype=np.float32)

        self.in_speech = False
        self.silence_chunks = 0

        self.max_silence_chunks = 5       # 500 ms

    def process(self, audio):

        # Maintain rolling window
        self.rolling_buffer = np.concatenate(
            (self.rolling_buffer, audio)
        )

        if len(self.rolling_buffer) > self.window_size:
            self.rolling_buffer = self.rolling_buffer[-self.window_size:]

        # Wait until we have enough audio
        if len(self.rolling_buffer) < self.window_size:
            return

        speech = vad.is_speech(self.rolling_buffer)

        if speech:

            if not self.in_speech:
                print("\n🎤 Speech Started")

                self.in_speech = True
                voice_state.set_recording(True)

            self.speech_buffer = np.concatenate(
                (self.speech_buffer, audio)
            )

            self.silence_chunks = 0

        else:

            if self.in_speech:

                self.silence_chunks += 1

                self.speech_buffer = np.concatenate(
                    (self.speech_buffer, audio)
                )

                if self.silence_chunks >= self.max_silence_chunks:

                    print(
                        f"🛑 Speech Finished ({len(self.speech_buffer)} samples)"
                    )

                    voice_state.set_recording(False)

                    from speech.whisper_engine import whisper

                    print("🧠 Transcribing...")

                    text = whisper.transcribe(self.speech_buffer)

                    print(f"\nYou: {text}\n")

                    self.speech_buffer = np.array(
                        [],
                        dtype=np.float32
                    )

                    self.in_speech = False
                    self.silence_chunks = 0