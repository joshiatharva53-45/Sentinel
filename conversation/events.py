"""
conversation/events.py

Defines all conversation events used by the runtime.
"""

from enum import Enum


class ConversationEvent(str, Enum):
    """Conversation runtime events."""

    CONVERSATION_STARTED = "conversation_started"
    CONVERSATION_ENDED = "conversation_ended"

    USER_SPEECH_RECOGNIZED = "user_speech_recognized"

    INTENT_DETECTED = "intent_detected"

    REQUEST_PROCESSING = "request_processing"

    PLANNING_STARTED = "planning_started"

    TOOL_EXECUTION_STARTED = "tool_execution_started"
    TOOL_EXECUTION_FINISHED = "tool_execution_finished"

    RESPONSE_READY = "response_ready"

    ASSISTANT_SPEAKING_STARTED = "assistant_speaking_started"
    ASSISTANT_SPEAKING_FINISHED = "assistant_speaking_finished"

    CONVERSATION_TIMEOUT = "conversation_timeout"

    CONVERSATION_ERROR = "conversation_error"

    STATE_CHANGED = "conversation_state_changed"