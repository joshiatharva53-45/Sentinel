"""
core/event_bus.py
"""

from collections import defaultdict
from threading import Lock
from typing import Callable, Type


class EventBus:

    def __init__(self):
        self._subscribers = defaultdict(list)
        self._lock = Lock()

    # ----------------------------------------------------

    def subscribe(self, event_type: Type, callback: Callable):

        with self._lock:

            if callback not in self._subscribers[event_type]:
                self._subscribers[event_type].append(callback)

    # ----------------------------------------------------

    def unsubscribe(self, event_type: Type, callback: Callable):

        with self._lock:

            if callback in self._subscribers[event_type]:
                self._subscribers[event_type].remove(callback)

    # ----------------------------------------------------

    def publish(self, event):

        callbacks = list(
            self._subscribers[type(event)]
        )

        for callback in callbacks:
            callback(event)

    # ----------------------------------------------------

    def clear(self):

        with self._lock:
            self._subscribers.clear()