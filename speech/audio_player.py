"""
speech/audio_player.py

Simple audio playback service.

Used by PiperEngine to play generated WAV files.
"""

from pathlib import Path
import sounddevice as sd
import soundfile as sf


class AudioPlayer:

    def __init__(self):

        self._playing = False

    # ---------------------------------------------------------

    def play(self, audio_file: str | Path):

        audio_file = Path(audio_file)

        if not audio_file.exists():
            raise FileNotFoundError(audio_file)

        data, samplerate = sf.read(audio_file)

        self._playing = True

        sd.play(data, samplerate)

        sd.wait()

        self._playing = False

    # ---------------------------------------------------------

    def stop(self):

        sd.stop()

        self._playing = False

    # ---------------------------------------------------------

    def is_playing(self):

        return self._playing