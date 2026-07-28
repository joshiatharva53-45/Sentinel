"""
core/logger.py

Central logging service for Sentinel V2.
"""

from __future__ import annotations

import logging
from pathlib import Path


class Logger:

    def __init__(
        self,
        name: str = "Sentinel",
        log_dir: str = "logs",
        level: int = logging.INFO,
    ):
        self.name = name
        self.level = level

        Path(log_dir).mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Prevent duplicate handlers
        if self.logger.handlers:
            return

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
            datefmt="%H:%M:%S",
        )

        # Console Handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        # File Handler
        logfile = Path(log_dir) / "sentinel.log"
        file_handler = logging.FileHandler(logfile, encoding="utf-8")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file_handler)

    # ---------------------------------------------------------

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

    def exception(self, message: str):
        self.logger.exception(message)