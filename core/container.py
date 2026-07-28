"""
core/container.py

Production Dependency Injection Container
"""

from typing import Any, Callable


class ServiceContainer:
    """
    Dependency Injection Container.

    Supports:
    - Singleton services
    - Factory services
    """

    def __init__(self):
        self._singletons: dict[str, Any] = {}
        self._factories: dict[str, Callable[..., Any]] = {}
        self._instances: dict[str, Any] = {}

    # ---------------------------------------------------------

    def register_singleton(self, name: str, instance: Any) -> None:
        """Register a singleton instance."""

        if name in self._singletons or name in self._factories:
            raise ValueError(f"Service '{name}' is already registered.")

        self._singletons[name] = instance

    # ---------------------------------------------------------

    def register_factory(self, name: str, factory: Callable[..., Any]) -> None:
        """Register a factory."""

        if name in self._singletons or name in self._factories:
            raise ValueError(f"Service '{name}' is already registered.")

        self._factories[name] = factory

    # ---------------------------------------------------------

    def resolve(self, name: str) -> Any:
        """Resolve a service."""

        # Cached singleton
        if name in self._instances:
            return self._instances[name]

        # Singleton
        if name in self._singletons:
            instance = self._singletons[name]
            self._instances[name] = instance
            return instance

        # Factory
        if name in self._factories:
            return self._factories[name]()

        raise KeyError(f"Service '{name}' is not registered.")

    # ---------------------------------------------------------

    def unregister(self, name: str) -> None:
        """Remove a service."""

        self._singletons.pop(name, None)
        self._factories.pop(name, None)
        self._instances.pop(name, None)

    # ---------------------------------------------------------

    def has(self, name: str) -> bool:
        """Check if a service exists."""

        return (
            name in self._singletons
            or name in self._factories
        )

    # ---------------------------------------------------------

    def clear(self) -> None:
        """Remove every registered service."""

        self._singletons.clear()
        self._factories.clear()
        self._instances.clear()

    # ---------------------------------------------------------

    def list_services(self) -> list[str]:
        """Return all registered service names."""

        return sorted(
            set(self._singletons.keys())
            | set(self._factories.keys())
        )