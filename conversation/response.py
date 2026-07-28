"""
conversation/response.py

Standard response object used throughout Sentinel.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass(slots=True)
class Response:
    """
    Standard response returned by every Sentinel component.
    """

    text: str

    speak: bool = True

    success: bool = True

    source: str = "unknown"

    tool: Optional[str] = None

    metadata: Dict[str, Any] = field(default_factory=dict)

    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert response to a dictionary."""

        return {
            "text": self.text,
            "speak": self.speak,
            "success": self.success,
            "source": self.source,
            "tool": self.tool,
            "metadata": self.metadata,
            "error": self.error,
        }