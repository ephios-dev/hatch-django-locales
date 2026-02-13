from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import subprocess
from pathlib import Path

class DjangoLocaleBuildHook(BuildHookInterface):
    PLUGIN_NAME = "django-locales"

    def initialize(self, version, build_data):
        # Search inside 'src/' for Django apps with locale folders
        root = Path(self.root) / "src"
        locale_dirs = list(root.glob("**/locale"))

        for loc in locale_dirs:
            try:
                subprocess.run(
                    ["django-admin", "compilemessages", "-v0"],
                    cwd=loc.parent,
                    check=True,
                )
            except Exception as e:
                raise RuntimeError(f"Failed to compile locales in {loc}: {e}")