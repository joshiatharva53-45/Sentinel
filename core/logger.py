"""
core/logger.py

Central Logger.
"""

from __future__ import annotations

import logging
import sys


class Logger:

    def __init__(self):

        self.logger = logging.getLogger("Sentinel")

        if not self.logger.handlers:

            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter(

                "[%(asctime)s] "

                "%(levelname)s "

                "%(name)s: "

                "%(message)s",

                "%H:%M:%S",

            )

            console = logging.StreamHandler(sys.stdout)

            console.setFormatter(formatter)

            self.logger.addHandler(console)

    # ---------------------------------------------------------

    def debug(self, *args, **kwargs):

        self.logger.debug(*args, **kwargs)

    # ---------------------------------------------------------

    def info(self, *args, **kwargs):

        self.logger.info(*args, **kwargs)

    # ---------------------------------------------------------

    def warning(self, *args, **kwargs):

        self.logger.warning(*args, **kwargs)

    # ---------------------------------------------------------

    def error(self, *args, **kwargs):

        self.logger.error(*args, **kwargs)

    # ---------------------------------------------------------

    def exception(self, *args, **kwargs):

        self.logger.exception(*args, **kwargs)

    # ---------------------------------------------------------

    def critical(self, *args, **kwargs):

        self.logger.critical(*args, **kwargs)