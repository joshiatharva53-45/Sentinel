"""
=========================================================
Plugin Manager
=========================================================
"""

from importlib import import_module
from pathlib import Path

from core.logger import info, warning


class PluginManager:

    def __init__(self):

        self.plugins = {}

    def load_plugins(self):

        plugin_dir = Path("plugins")

        if not plugin_dir.exists():

            warning("Plugin directory not found.")
            return

        for file in plugin_dir.glob("*.py"):

            if file.stem.startswith("__"):
                continue

            module_name = f"plugins.{file.stem}"

            try:

                module = import_module(module_name)

                if hasattr(module, "initialize"):
                    module.initialize()

                self.plugins[file.stem] = module

                info(f"Loaded Plugin: {file.stem}")

            except Exception as e:

                warning(f"Failed loading {file.stem}: {e}")

    def execute(self, text):

        text = text.lower()

        # ---------- Browser ----------

        if "open" in text or "browser" in text:

            plugin = self.plugins.get("browser")

            if plugin and hasattr(plugin, "execute"):

                return plugin.execute(text)

        # ---------- Calculator ----------

        if "calculator" in text or "calculate" in text:

            plugin = self.plugins.get("calculator")

            if plugin and hasattr(plugin, "execute"):

                return plugin.execute(text)

        # ---------- System ----------

        if any(word in text for word in [

            "shutdown",
            "restart",
            "lock",

        ]):

            plugin = self.plugins.get("system")

            if plugin and hasattr(plugin, "execute"):

                return plugin.execute(text)

        return "No plugin matched."

    def get(self, name):

        return self.plugins.get(name)

    def all_plugins(self):

        return list(self.plugins.keys())


plugin_manager = PluginManager()