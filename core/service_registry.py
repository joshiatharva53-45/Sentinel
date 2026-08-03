"""
core/service_registry.py

Central registry for lifecycle services.
"""

from __future__ import annotations


class ServiceRegistry:

    def __init__(self):

        self._services = []

    # ---------------------------------------------------------

    def register(self, service):

        if service not in self._services:
            self._services.append(service)

        return service

    # ---------------------------------------------------------

    def unregister(self, service):

        if service in self._services:
            self._services.remove(service)

    # ---------------------------------------------------------

    def clear(self):

        self._services.clear()

    # ---------------------------------------------------------

    def all(self):

        return list(self._services)

    # ---------------------------------------------------------

    def initialize(self):

        for service in self._services:

            if hasattr(service, "initialize"):
                service.initialize()

    # ---------------------------------------------------------

    def start(self):

        for service in self._services:

            if hasattr(service, "start"):
                service.start()

    # ---------------------------------------------------------

    def stop(self):

        for service in reversed(self._services):

            if hasattr(service, "stop"):
                service.stop()

    # ---------------------------------------------------------

    def shutdown(self):

        for service in reversed(self._services):

            if hasattr(service, "shutdown"):
                service.shutdown()