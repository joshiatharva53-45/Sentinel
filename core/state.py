"""
=========================================================
Assistant State
=========================================================
"""


class AssistantState:

    def __init__(self):

        self.is_running = False

        self.is_listening = False

        self.is_speaking = False

        self.last_command = ""

        self.last_response = ""

        self.current_mode = "IDLE"

        self.user_name = None

        self.session_memory = []

    def reset(self):

        self.last_command = ""

        self.last_response = ""

        self.current_mode = "IDLE"

        self.is_listening = False

        self.is_speaking = False


state = AssistantState()