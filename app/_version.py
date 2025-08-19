import tomllib
from pathlib import Path


def get_project_version() -> str:
    """Reads the project version from the pyproject.toml file."""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"

    try:
        with open(pyproject_path, "rb") as f:
            pyproject_data = tomllib.load(f)

        return pyproject_data["project"]["version"]
    except (FileNotFoundError, KeyError):
        # Handle cases where the file or key doesn't exist
        return "0.0.0-dev"


# You can now use this version in your application
__version__ = get_project_version()
