"""
Browser Plugin
"""

import webbrowser


def initialize():
    print("Browser Plugin Initialized")


def execute(command: str):

    command = command.lower().strip()

    # ---------------------------
    # Google Search
    # ---------------------------

    if command.startswith("search "):

        query = command.replace("search", "", 1).strip()

        if not query:
            return "What should I search?"

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for '{query}'"

    # ---------------------------
    # Open Websites
    # ---------------------------

    websites = {

        "youtube": "https://youtube.com",

        "google": "https://google.com",

        "github": "https://github.com",

        "chatgpt": "https://chat.openai.com",

        "gmail": "https://mail.google.com",

        "linkedin": "https://linkedin.com",

        "instagram": "https://instagram.com",

        "facebook": "https://facebook.com",

        "reddit": "https://reddit.com",

        "twitter": "https://x.com",

    }

    for name, url in websites.items():

        if f"open {name}" in command:

            webbrowser.open(url)

            return f"Opening {name.title()}"

    # ---------------------------
    # Generic URL
    # ---------------------------

    if command.startswith("open "):

        site = command.replace("open", "", 1).strip()

        if "." not in site:

            site += ".com"

        webbrowser.open(f"https://{site}")

        return f"Opening {site}"

    return None