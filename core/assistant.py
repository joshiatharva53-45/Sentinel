from core.engine import engine
from core.state import state
from core.logger import info
from core import constants
from core.plugin_manager import plugin_manager
from core.router import router
from core.event_bus import event_bus

from conversation import ConversationManager

from ai import Ollama
from tts import tts


class Assistant:

    def __init__(self):

        self.conversation = None
        self.llm = Ollama()

    def startup(self):

        engine.start()

        print(constants.WELCOME_MESSAGE)
        print(f"Loaded Plugins: {plugin_manager.all_plugins()}")

        self.conversation = ConversationManager(
            event_bus=event_bus,
            router=router,
            llm=self.llm,
        )

        self.conversation.start()

        event_bus.subscribe(
            "speech_recognized",
            self.handle_speech,
        )

        state.is_running = True

        info("Assistant Started")

    def shutdown(self):

        if self.conversation:
            self.conversation.stop()

        engine.stop()

        state.is_running = False
        tts.shutdown()

        print(constants.GOODBYE_MESSAGE)

    def handle_speech(self, text):

        response = self.conversation.process(text)

        print(f"\nSentinel > {response.text}\n")

        tts.say(response.text)

        return response

    def process(self, text):

        state.last_command = text

        return self.handle_speech(text)


assistant = Assistant()