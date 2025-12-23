import tomllib
from email.policy import default

from pathlib import Path


def get_version_from_file() -> str:
    """
    Читает версию напрямую из файла pyproject.toml.
    """
    # Находим корень проекта относительно текущего скрипта
    project_root = Path.cwd()
    print(project_root)
    toml_file = project_root / 'pyproject.toml'

    if not toml_file.exists():
        return 'N/A'

    with open(toml_file, 'rb') as f:
        data = tomllib.load(f)

    # Извлекаем версию по ключам [project] и version
    version: str = data.get('project', {}).get('version', 'N/A')
    return version
