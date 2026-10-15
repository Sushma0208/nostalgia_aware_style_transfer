"""Small standard-library configuration loader for YAML-free test environments."""

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass(frozen=True)
class ProjectConfig:
    name: str
    version: str
    python_requires: str


def load_project_config(path: str | Path) -> ProjectConfig:
    """Read the project's pyproject.toml metadata and validate required fields."""
    with Path(path).open("rb") as handle:
        document = tomllib.load(handle)
    try:
        project = document["project"]
        result = ProjectConfig(
            name=project["name"],
            version=project["version"],
            python_requires=project["requires-python"],
        )
    except (KeyError, TypeError) as exc:
        raise ValueError("missing required [project] metadata") from exc
    if not all((result.name.strip(), result.version.strip(), result.python_requires.strip())):
        raise ValueError("project metadata values must be non-empty")
    return result
