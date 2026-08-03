"""
System Plugin
"""

import ctypes
import os
import platform


def initialize():
    print("System Plugin Initialized")


def execute(command: str):

    command = command.lower().strip()

    if platform.system() != "Windows":
        return "Only Windows is currently supported."

    # ---------------- Shutdown ----------------

    if "shutdown" in command:

        os.system("shutdown /s /t 0")

        return "Shutting down Windows."

    # ---------------- Restart ----------------

    if "restart" in command:

        os.system("shutdown /r /t 0")

        return "Restarting Windows."

    # ---------------- Log Off ----------------

    if "log off" in command or "logout" in command:

        os.system("shutdown /l")

        return "Logging off."

    # ---------------- Lock ----------------

    if "lock" in command:

        ctypes.windll.user32.LockWorkStation()

        return "Locking computer."

    # ---------------- Sleep ----------------

    if "sleep" in command:

        os.system(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        )

        return "Putting computer to sleep."

    return None