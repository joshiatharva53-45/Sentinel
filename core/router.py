"""
core/router.py
"""

from core import constants


class Router:
    """
    Decides where a user request should go.
    """

    def classify(self, text: str) -> str:

        text = text.lower().strip()

        # -------------------------
        # Exit
        # -------------------------

        if text in (
            "exit",
            "quit",
            "bye",
            "shutdown sentinel",
        ):
            return constants.ROUTER_EXIT

        # -------------------------
        # Commands
        # -------------------------

        command_keywords = (
            "open",
            "close",
            "play",
            "pause",
            "search",
            "calculate",
            "calc",
            "volume",
            "brightness",
            "shutdown",
            "restart",
            "lock",
        )

        if any(keyword in text for keyword in command_keywords):
            return constants.ROUTER_COMMAND

        # -------------------------
        # Memory (future)
        # -------------------------

        memory_keywords = (
            "remember",
            "forget",
            "what do you know",
            "my name",
        )

        if any(keyword in text for keyword in memory_keywords):
            return constants.ROUTER_MEMORY

        # -------------------------
        # Everything else goes to LLM
        # -------------------------

        return constants.ROUTER_LLM


router = Router()