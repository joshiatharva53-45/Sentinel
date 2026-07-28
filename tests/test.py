from pipeline import AIPipeline

from conversation.manager import ConversationManager
from speech.speech_manager import SpeechManager


conversation = ConversationManager()

speech = SpeechManager()

speech.start()

pipeline = AIPipeline(
    conversation=conversation,
    speech=speech,
)

pipeline.process_text(
    "Introduce yourself."
)

pipeline.process_text(
    "What is Python?"
)

pipeline.process_text(
    "Tell me a joke."
)

speech.stop()