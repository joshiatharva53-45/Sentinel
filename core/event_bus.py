"""
core/event_bus.py

Thread-safe Event Bus.
"""

from __future__ import annotations

from collections import defaultdict
from threading import RLock
from typing import Callable, Any


class EventBus:

    def __init__(self):

        self._listeners: dict[str, list[Callable[..., Any]]] = defaultdict(list)

        self._lock = RLock()

    # ---------------------------------------------------------

    def on(
        self,
        event: str,
        callback: Callable[..., Any],
    ) -> None:

        with self._lock:

            if callback not in self._listeners[event]:

                self._listeners[event].append(callback)

    # ---------------------------------------------------------

    def off(
        self,
        event: str,
        callback: Callable[..., Any],
    ) -> None:

        with self._lock:

            if callback in self._listeners[event]:

                self._listeners[event].remove(callback)

    # ---------------------------------------------------------

    def emit(
        self,
        event: str,
        *args,
        **kwargs,
    ) -> None:

        callbacks = list(self._listeners.get(event, []))

        for callback in callbacks:

            callback(*args, **kwargs)

    # ---------------------------------------------------------

    def once(
        self,
        event: str,
        callback: Callable[..., Any],
    ):

        def wrapper(*args, **kwargs):

            self.off(event, wrapper)

            callback(*args, **kwargs)

        self.on(event, wrapper)

    # ---------------------------------------------------------

    def listener_count(
        self,
        event: str,
    ) -> int:

        return len(self._listeners.get(event, []))

    # ---------------------------------------------------------

    def clear(self):

        with self._lock:

            self._listeners.clear()