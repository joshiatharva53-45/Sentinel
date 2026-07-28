"""
core/events.py

Strongly-typed application events.
"""

from dataclasses import dataclass, field
from time import time


# ==========================================================
# Base Event
# ==========================================================

@dataclass(slots=True)
class Event:
    timestamp: float = field(default_factory=time)


# ==========================================================
# Application Events
# ==========================================================

@dataclass(slots=True)
class AppStarted(Event):
    pass


@dataclass(slots=True)
class AppStopped(Event):
    pass


# ==========================================================
# Wake Word
# ==========================================================

@dataclass(slots=True)
class WakeWordDetected(Event):
    keyword: str = ""


# ==========================================================
# Voice
# ==========================================================

@dataclass(slots=True)
class SpeechStarted(Event):
    pass


@dataclass(slots=True)
class SpeechFinished(Event):
    duration: float = 0.0


# ==========================================================
# Speech Recognition
# ==========================================================

@dataclass(slots=True)
class SpeechRecognized(Event):
    text: str = ""
    language: str = "en"
    confidence: float = 1.0


# ==========================================================
# TTS
# ==========================================================

@dataclass(slots=True)
class TTSStarted(Event):
    text: str = ""


@dataclass(slots=True)
class TTSFinished(Event):
    pass


# ==========================================================
# Conversation
# ==========================================================

@dataclass(slots=True)
class ConversationResponse(Event):
    text: str = ""


# ==========================================================
# Memory
# ==========================================================

@dataclass(slots=True)
class MemoryStored(Event):
    key: str = ""


# ==========================================================
# Plugins
# ==========================================================

@dataclass(slots=True)
class PluginExecuted(Event):
    plugin: str = ""