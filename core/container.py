"""
core/container.py

Dependency Injection Container.
"""

from __future__ import annotations

from typing import Any, Callable

from core.exception import (
    ServiceAlreadyRegisteredError,
    ServiceNotFoundError,
)


class ServiceContainer:

    def __init__(self):

        self._singletons: dict[str, Any] = {}

        self._instances: dict[str, Any] = {}

        self._factories: dict[str, Callable[..., Any]] = {}

    # ---------------------------------------------------------

    def register_singleton(
        self,
        name: str,
        instance: Any,
    ) -> None:

        if self.has(name):

            raise ServiceAlreadyRegisteredError(name)

        self._singletons[name] = instance

    # ---------------------------------------------------------

    def register_factory(
        self,
        name: str,
        factory: Callable[..., Any],
    ) -> None:

        if self.has(name):

            raise ServiceAlreadyRegisteredError(name)

        self._factories[name] = factory

    # ---------------------------------------------------------

    def resolve(
        self,
        name: str,
    ) -> Any:

        if name in self._instances:

            return self._instances[name]

        if name in self._singletons:

            instance = self._singletons[name]

            self._instances[name] = instance

            return instance

        if name in self._factories:

            return self._factories[name]()

        raise ServiceNotFoundError(name)

    # ---------------------------------------------------------

    def unregister(
        self,
        name: str,
    ):

        self._singletons.pop(name, None)

        self._instances.pop(name, None)

        self._factories.pop(name, None)

    # ---------------------------------------------------------

    def has(
        self,
        name: str,
    ) -> bool:

        return (
            name in self._singletons
            or name in self._factories
        )

    # ---------------------------------------------------------

    def clear(self):

        self._singletons.clear()

        self._instances.clear()

        self._factories.clear()

    # ---------------------------------------------------------

    def list_services(self) -> list[str]:

        return sorted(

            list(self._singletons.keys())

            +

            list(self._factories.keys())

        )