"""
core/exceptions.py

Sentinel custom exceptions.
"""


class SentinelError(Exception):
    """Base Sentinel exception."""
    pass


class ConfigurationError(SentinelError):
    """Invalid configuration."""
    pass


class InitializationError(SentinelError):
    """Service initialization failed."""
    pass


class ServiceNotFoundError(SentinelError):
    """Requested service does not exist."""
    pass


class ServiceAlreadyRegisteredError(SentinelError):
    """Duplicate service registration."""
    pass


class PipelineError(SentinelError):
    """Pipeline execution failed."""
    pass


class ConversationError(SentinelError):
    """Conversation runtime error."""
    pass


class SpeechError(SentinelError):
    """Speech subsystem error."""
    pass


class LLMError(SentinelError):
    """Language model error."""
    pass