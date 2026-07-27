import subprocess
import sys
from pathlib import Path


def compile_qrc(*, qrc_file: Path, output_py_file: Path, pyside6_rcc: Path) -> None:
    """
    Запускает команду pyside6-rcc для компиляции QRC файла.
    """
    if not qrc_file.exists():
        print(f"Ошибка: Исходный файл ресурсов не найден: {qrc_file}")
        sys.exit(1)
    try:
        # Выполняем команду в операционной системе
        subprocess.run(
            [str(pyside6_rcc), str(qrc_file), "-o", str(output_py_file)],
            check=True,
            shell=False
        )
        print(f"\033[92mУСПЕШНО resources.rc скомпилирован -> {output_py_file}\033[0m\n")
    except FileNotFoundError:
        print("Ошибка: Утилита 'pyside6-rcc' не найдена.")
        print("Убедитесь, что PySide6 установлен и находится в переменной PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении команды компиляции: {e}")
        sys.exit(1)


def compile_ui(*, source_dir: Path, target_dir: Path, pyside6_uic: Path) -> None:
    """
    Запускает команду pyside6-uic для компиляции gui файла.
    """
    ui_files = source_dir.glob("**/*.ui")

    for ui_file in ui_files:
        # Пропуск файлов, если они уже находятся в целевой папке
        if target_dir in ui_file.parents:
            continue

        # Вычисление относительного пути и пути назначения
        rel_path_ui_file = ui_file.relative_to(source_dir)
        target_path_ui_py_file = target_dir / rel_path_ui_file.with_suffix(".py")  # или с суффиксом _ui.py

        # Создание подпапок, если они не существуют
        target_path_ui_py_file.parent.mkdir(parents=True, exist_ok=True)

        # Выполнение команды компиляции
        try:
            subprocess.run(
                [pyside6_uic, str(ui_file), "-o", str(target_path_ui_py_file)],
                check=True
            )
            print(f"\033[92mУСПЕШНО: {rel_path_ui_file} -> {target_path_ui_py_file}\033[0m\n")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Ошибка компиляции {rel_path_ui_file}: {e}")


if __name__ == "__main__":
    env_bin_path = Path(sys.executable).parent
    root_dir = env_bin_path.parent.parent

    QRC_FILE = root_dir / "src/presentation/assets/resources.qrc"
    OUTPUT_PY_FILE = root_dir / "src/presentation/gui/generated/resources_rc.py"
    PYSIDE6_RCC = env_bin_path / "pyside6-rcc"

    UI_FILES_DIR = root_dir / "src/presentation/assets/forms"
    UI_PY_FILES_DIR = root_dir / "src/presentation/gui/generated/ui"
    PYSIDE6_UIC = env_bin_path / "pyside6-uic"

    compile_ui(source_dir=UI_FILES_DIR, target_dir=UI_PY_FILES_DIR, pyside6_uic=PYSIDE6_UIC)
    compile_qrc(qrc_file=QRC_FILE, output_py_file=OUTPUT_PY_FILE, pyside6_rcc=PYSIDE6_RCC)
