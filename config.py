"""
============================================================
Sentinel V2 Configuration
============================================================
All configurable settings for Sentinel live here.

Never hardcode values anywhere else.
============================================================
"""

from pathlib import Path

# ---------------------------------------------------------
# Project Paths
# ---------------------------------------------------------

ROOT_DIR = Path(__file__).parent.resolve()

MODELS_DIR = ROOT_DIR / "models"

DATABASE_DIR = ROOT_DIR / "database"

LOG_DIR = ROOT_DIR / "logs"

ASSETS_DIR = ROOT_DIR / "assets"

# ---------------------------------------------------------
# Assistant
# ---------------------------------------------------------

ASSISTANT_NAME = "Sentinel"

VERSION = "2.0.0"

LANGUAGE = "en"

# ---------------------------------------------------------
# Audio
# ---------------------------------------------------------

SAMPLE_RATE = 16000

CHANNELS = 1

CHUNK_SIZE = 1024

RECORD_TIMEOUT = 5

SILENCE_TIMEOUT = 2

# ---------------------------------------------------------
# Wake Phrase
# ---------------------------------------------------------

WAKE_PHRASE = "hey sentinel"

WAKE_RESPONSE = "Yes?"

# ---------------------------------------------------------
# Speech Recognition
# ---------------------------------------------------------

WHISPER_MODEL = "base"

WHISPER_DEVICE = "cpu"

WHISPER_COMPUTE_TYPE = "int8"

# ---------------------------------------------------------
# Text To Speech
# ---------------------------------------------------------

TTS_ENGINE = "pyttsx3"

VOICE_RATE = 180

VOICE_VOLUME = 1.0

# ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

LLM_PROVIDER = "ollama"

OLLAMA_MODEL = "llama3.2"

OLLAMA_HOST = "http://localhost:11434"

TEMPERATURE = 0.7

MAX_TOKENS = 1024

# ---------------------------------------------------------
# Memory
# ---------------------------------------------------------

ENABLE_MEMORY = True

SQLITE_DB = DATABASE_DIR / "sentinel.db"

VECTOR_DB = DATABASE_DIR / "chroma"

MEMORY_TOP_K = 5

# ---------------------------------------------------------
# Vision
# ---------------------------------------------------------

CAMERA_INDEX = 0

ENABLE_VISION = False

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "sentinel.log"

# ---------------------------------------------------------
# Agent
# ---------------------------------------------------------

ENABLE_PLANNER = False

MAX_PLANNER_STEPS = 10