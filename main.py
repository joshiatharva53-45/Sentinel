import time

from core.assistant import assistant
from voice.manager import voice_manager


def main():

    voice_manager.initialize()

    assistant.startup()

    voice_manager.start()

    print("\n🎤 Sentinel is listening...\n")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        pass

    finally:

        voice_manager.stop()

        assistant.shutdown()


if __name__ == "__main__":
    main()