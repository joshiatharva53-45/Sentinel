"""
pipeline/ai_pipeline.py

Main AI execution pipeline.
"""

from __future__ import annotations

from conversation.response import Response

from conversation.events import ConversationEvent


class AIPipeline:

    def __init__(
        self,
        conversation,
        speech,
        whisper=None,
        event_bus=None,
        logger=None,
    ):

        self.conversation = conversation
        self.speech = speech
        self.whisper = whisper

        self.event_bus = event_bus
        self.logger = logger

    # ---------------------------------------------------------

    def process_text(
        self,
        text: str,
    ) -> Response:

        try:

            if self.event_bus:

                self.event_bus.emit(
                    ConversationEvent.REQUEST_PROCESSING.value,
                    text,
                )

            response = self.conversation.process(text)

            if (
                response.speak
                and self.speech
            ):

                self.speech.speak(response.text)

            return response

        except Exception as e:

            if self.logger:

                self.logger.exception(e)

            raise

    # ---------------------------------------------------------

    def process_audio(
        self,
        audio,
    ) -> Response:

        if self.whisper is None:

            raise RuntimeError(
                "Whisper engine is not configured."
            )

        text = self.whisper.transcribe(audio)

        return self.process_text(text)