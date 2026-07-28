"""
core/engine.py

Sentinel Application Engine
"""

from core.container import container
from core.lifecycle import Service
from core.bootstrap import Bootstrapper


class Engine:

    def __init__(self):

        
        class Engine:

            def __init__(self):

                bootstrap = Bootstrapper()

                self.container = bootstrap.configure()

        self.services = []
        self.services = []

    # ------------------------------------------------

    def register(self, name, service):

        self.container.register_singleton(name, service)

        self.services.append(service)

    # ------------------------------------------------

    def initialize(self):

        print("\n========== INITIALIZING ==========\n")

        for service in self.services:

            print(f"[INIT] {service.name}")

            service.initialize()

            service.initialized = True

        print("\nInitialization Complete\n")

    # ------------------------------------------------

    def start(self):

        print("\n========== STARTING ==========\n")

        for service in self.services:

            print(f"[START] {service.name}")

            service.start()

            service.running = True

        print("\nSentinel Running\n")

    # ------------------------------------------------

    def stop(self):

        print("\n========== STOPPING ==========\n")

        for service in reversed(self.services):

            print(f"[STOP] {service.name}")

            service.stop()

            service.running = False

    # ------------------------------------------------

    def shutdown(self):

        print("\n========== SHUTDOWN ==========\n")

        for service in reversed(self.services):

            print(f"[SHUTDOWN] {service.name}")

            service.shutdown()

            service.initialized = False

        print("\nSentinel Offline\n")