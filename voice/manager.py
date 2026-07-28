"""
voice/manager.py

Initializes and manages the voice subsystem.
"""

from voice.devices import list_devices
from voice.stream import audio_stream
from voice.worker import audio_worker
from speech.whisper_engine import whisper_engine
from voice.vad import vad


class VoiceManager:

    def initialize(self):

        print("\n========== Voice Initialization ==========\n")

        list_devices()

        whisper_engine.load()

        vad.load()

        print("\n✅ Voice subsystem ready.\n")

    def start(self):

        print("Starting microphone...")

        audio_stream.start()

        print("Starting audio worker...")

        audio_worker.start()

        print("✅ Voice manager started.\n")

    def stop(self):

        print("\nStopping voice manager...")

        audio_worker.stop()

        audio_stream.stop()

        print("✅ Voice manager stopped.")


voice_manager = VoiceManager()