"""
core/lifecycle.py

Base lifecycle for every Sentinel service.
"""

from abc import ABC
from abc import abstractmethod


class Service(ABC):
    """
    Base class for every Sentinel service.
    """

    def __init__(self, name: str):
        self.name = name

        self.initialized = False
        self.running = False

    # ------------------------------------------------

    @abstractmethod
    def initialize(self):
        """
        Allocate resources.

        Load models.

        Connect hardware.

        Read configuration.
        """
        ...

    # ------------------------------------------------

    @abstractmethod
    def start(self):
        """
        Begin execution.
        """
        ...

    # ------------------------------------------------

    @abstractmethod
    def stop(self):
        """
        Stop execution safely.
        """
        ...

    # ------------------------------------------------

    @abstractmethod
    def shutdown(self):
        """
        Release resources.
        """
        ...

    # ------------------------------------------------

    def status(self):

        return {
            "name": self.name,
            "initialized": self.initialized,
            "running": self.running,
        }