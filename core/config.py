"""
core/config.py

Central configuration for Sentinel V2.
"""

from dataclasses import dataclass, field
from pathlib import Path
from llm.config import LLMConfig

# ==========================================================
# Audio
# ==========================================================

@dataclass(slots=True, frozen=True)
class AudioConfig:
    sample_rate: int = 16000
    channels: int = 1
    dtype: str = "float32"
    chunk_size: int = 1600          # 100 ms
    silence_chunks: int = 5


# ==========================================================
# Whisper
# ==========================================================

@dataclass(slots=True, frozen=True)
class WhisperConfig:
    model_size: str = "base"
    device: str = "cuda"
    compute_type: str = "float16"
    language: str | None = None


# ==========================================================
# Piper
# ==========================================================

@dataclass(slots=True, frozen=True)
class PiperConfig:
    piper_path: Path = Path(r"E:\AI\Piper\piper.exe")
    voices_path: Path = Path(r"E:\AI\Piper\voices")
    voice: str = "en_US-lessac-medium"
    sample_rate: int = 22050


# ==========================================================
# Memory
# ==========================================================

@dataclass(slots=True, frozen=True)
class MemoryConfig:
    vector_db: Path = Path("memory/vector_store")
    history: Path = Path("memory/history")


# ==========================================================
# Application
# ==========================================================

@dataclass(slots=True, frozen=True)
class AppConfig:
    app_name: str = "Sentinel V2"
    debug: bool = True


# ==========================================================
# Root Config
# ==========================================================

@dataclass(slots=True)
class Config:
    app: AppConfig = field(default_factory=AppConfig)
    audio: AudioConfig = field(default_factory=AudioConfig)
    whisper: WhisperConfig = field(default_factory=WhisperConfig)
    piper: PiperConfig = field(default_factory=PiperConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)