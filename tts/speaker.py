import subprocess
import tempfile
import os

from tts.config import PIPER_EXE, VOICE


class Speaker:

    def __init__(self):
        self.voice = str(VOICE)
        self.piper = str(PIPER_EXE)

    def speak(self, text: str):

        if not text:
            return

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ) as tmp:

            wav = tmp.name

        try:

            subprocess.run(
                [
                    self.piper,
                    "-m",
                    self.voice,
                    "-f",
                    wav,
                ],
                input=text,
                text=True,
                check=True,
            )

            subprocess.run(
                [
                    "powershell",
                    "-c",
                    f"(New-Object Media.SoundPlayer '{wav}').PlaySync();",
                ],
                check=True,
            )

        finally:

            if os.path.exists(wav):
                os.remove(wav)


speaker = Speaker()