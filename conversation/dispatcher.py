"""
conversation/dispatcher.py
"""

from __future__ import annotations

import logging

from conversation.response import Response
from core import constants

logger = logging.getLogger(__name__)


class ConversationDispatcher:

    def __init__(self, router=None, llm=None):
        self.router = router
        self.llm = llm

    def dispatch(self, text: str) -> Response:

        text = text.strip()

        if not text:
            return Response(
                text="I didn't hear anything.",
                success=False,
                source="dispatcher",
            )

        logger.info("User: %s", text)

        route = constants.ROUTER_LLM

        # -----------------------------
        # Router
        # -----------------------------

        if self.router:
            route = self.router.classify(text)

        # -----------------------------
        # EXIT
        # -----------------------------

        if route == constants.ROUTER_EXIT:
            return Response(
                text="Goodbye!",
                source="router",
            )

        # -----------------------------
        # COMMAND
        # -----------------------------

        if route == constants.ROUTER_COMMAND:
            return Response(
                text="COMMAND",
                source="router",
                metadata={
                    "route": constants.ROUTER_COMMAND,
                    "command": text,
                },
            )

        # -----------------------------
        # MEMORY
        # -----------------------------

        if route == constants.ROUTER_MEMORY:
            return Response(
                text="Memory not implemented yet.",
                source="memory",
            )

        # -----------------------------
        # LLM
        # -----------------------------

        if self.llm:

            try:

                answer = self.llm.generate(
                    history=self.session.history.as_llm_messages(),
                    user_message=text,
                )

                return Response(
                    text=answer,
                    source="llm",
                )

            except Exception as e:

                logger.exception(e)

                return Response(
                    text=str(e),
                    success=False,
                    source="llm",
                )

        return Response(
            text="No language model available.",
            success=False,
            source="dispatcher",
        )