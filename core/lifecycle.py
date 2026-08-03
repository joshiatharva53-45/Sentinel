"""
core/lifecycle.py

Base lifecycle for Sentinel services.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Service(ABC):

    def __init__(self, name: str):

        self.name = name

        self.initialized = False

        self.running = False

    # ---------------------------------------------------------

    @abstractmethod
    def initialize(self):

        ...

    # ---------------------------------------------------------

    @abstractmethod
    def start(self):

        ...

    # ---------------------------------------------------------

    @abstractmethod
    def stop(self):

        ...

    # ---------------------------------------------------------

    @abstractmethod
    def shutdown(self):

        ...

    # ---------------------------------------------------------

    def status(self):

        return {

            "name": self.name,

            "initialized": self.initialized,

            "running": self.running,

        }

    # ---------------------------------------------------------

    def __repr__(self):

        return (

            f"{self.__class__.__name__}"

            f"(name={self.name!r}, "

            f"initialized={self.initialized}, "

            f"running={self.running})"

        )