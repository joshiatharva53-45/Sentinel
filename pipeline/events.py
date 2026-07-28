from dataclasses import dataclass


@dataclass(slots=True)
class PipelineStarted:
    text: str


@dataclass(slots=True)
class PipelineFinished:
    text: str
    response: str


@dataclass(slots=True)
class PipelineError:
    text: str
    error: Exception