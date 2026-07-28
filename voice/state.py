"""
voice/state.py

Global runtime state for the Voice Core.

Every component imports this object instead of maintaining
its own copy of flags.
"""

from dataclasses import dataclass, field
from threading import Lock


@dataclass
class VoiceState:
    # -------------------------------------------------
    # System lifecycle
    # -------------------------------------------------

    running: bool = False

    # Wake word has activated listening
    listening: bool = False

    # Currently recording speech
    recording: bool = False

    # Whisper is transcribing
    transcribing: bool = False

    # Piper (or other TTS) is speaking
    speaking: bool = False

    # Allow interruption while speaking
    interrupt_requested: bool = False

    # Last transcription
    last_text: str = ""

    # Thread safety
    lock: Lock = field(default_factory=Lock)

    # -------------------------------

    def set_running(self, value: bool):
        with self.lock:
            self.running = value

    def set_listening(self, value: bool):
        with self.lock:
            self.listening = value

    def set_recording(self, value: bool):
        with self.lock:
            self.recording = value

    def set_transcribing(self, value: bool):
        with self.lock:
            self.transcribing = value

    def set_speaking(self, value: bool):
        with self.lock:
            self.speaking = value

    def set_interrupt(self, value: bool):
        with self.lock:
            self.interrupt_requested = value

    def set_last_text(self, text: str):
        with self.lock:
            self.last_text = text

    # -------------------------------

    def reset(self):
        with self.lock:
            self.running = False
            self.listening = False
            self.recording = False
            self.transcribing = False
            self.speaking = False
            self.interrupt_requested = False
            self.last_text = ""


voice_state = VoiceState()