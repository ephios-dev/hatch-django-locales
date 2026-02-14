import itertools

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.plugin import hookimpl
import subprocess
from pathlib import Path

class DjangoLocaleBuildHook(BuildHookInterface):
    PLUGIN_NAME = "django-locales"

    def initialize(self, version, build_data):
        # Search inside 'src/' for Django apps with locale folders
        locale_dirs = itertools.chain(*(
            (Path(self.root)/search_directory).glob("**/locale")
            for search_directory in self.config.get("search-directories", ["."])
        ))

        for loc in locale_dirs:
            try:
                subprocess.run(
                    ["django-admin", "compilemessages", "-v0"],
                    cwd=loc.parent,
                    check=True,
                )
            except Exception as e:
                raise RuntimeError(f"Failed to compile locales in {loc}: {e}")

@hookimpl
def hatch_register_build_hook():
    return DjangoLocaleBuildHook