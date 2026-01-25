import shutil
import tomllib
from pathlib import Path


def create_clean_dir(dir_name: Path) -> None:
    # 1. Удаляем папку с указанным именем, если существует
    folder_name = Path(dir_name)
    if folder_name.exists() and folder_name.is_dir():
        try:
            shutil.rmtree(folder_name)
        except OSError as e:
            print(f"Ошибка при удалении папки {folder_name}: {e}")
    else:
        print(f"Папка '{folder_name}' не найдена или не является директорией.")

    # 2. Создаем новую пустую папку с тем же именем
    try:
        folder_name.mkdir()
    except OSError as e:
        print(f"Ошибка при создании папки {folder_name}: {e}")


def get_version_from_toml_file() -> str:
    """
    Читает версию напрямую из файла pyproject.toml.
    """
    # Находим корень проекта относительно текущего скрипта
    project_root = Path.cwd()
    print(project_root)
    toml_file = project_root / "pyproject.toml"

    if not toml_file.exists():
        return "N/A"

    with open(toml_file, "rb") as f:
        data = tomllib.load(f)

    # Извлекаем версию по ключам [project] и version
    version: str = data.get("project", {}).get("version", "N/A")
    return version
