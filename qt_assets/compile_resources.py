import subprocess
import sys

from pathlib import Path


def compile_qrc_to_py(qrc_file: Path, output_py_file: Path) -> None:
    """
    Запускает команду pyside6-rcc для компиляции QRC файла.
    """
    # Проверяем наличие входного файла
    if not qrc_file.exists():
        print(f"Ошибка: Исходный файл ресурсов не найден: {qrc_file}")
        sys.exit(1)

    # Формируем команду для выполнения
    # Мы используем 'pyside6-rcc' как имя исполняемого файла
    command = [
        "pyside6-rcc",
        qrc_file.as_posix(),
        "-o",
        output_py_file.as_posix(),
    ]

    print(f"Запуск команды: {' '.join(command)}")

    try:
        # Выполняем команду в операционной системе
        subprocess.run(command, check=True, shell=False)
        print(f"Успешно скомпилировано в файл: {output_py_file}")
        print()
    except FileNotFoundError:
        print(f"Ошибка: Утилита 'pyside6-rcc' не найдена.")
        print(f"Убедитесь, что PySide6 установлен и находится в переменной PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении команды компиляции: {e}")
        sys.exit(1)


def compile_ui_to_py(ui_files: Path, ui_py_files: Path) -> None:
    """
    Запускает команду pyside6-uic для компиляции ui файла.
    """
    # Проверяем наличие входного файла
    for elem in ui_files.iterdir():
        if not (elem.is_file() or elem.suffix == '.ui'):
            continue
        # Формируем команду для выполнения 'pyside6-uic' как имя исполняемого файла
        py_file = elem.with_suffix('.py').name
        output_py_path = ui_py_files / elem.with_suffix('.py').name
        command = [
            "pyside6-uic",
            elem.as_posix(),
            "-o",
            output_py_path.as_posix(),
        ]
        print(f"Запуск команды: {' '.join(command)}")
        try:
            # Выполняем команду в операционной системе
            subprocess.run(command, check=True, shell=False)
            print(f"Успешно скомпилировано в файл: {py_file}")
            print()
        except FileNotFoundError:
            print(f"Ошибка: Утилита 'pyside6-uic' не найдена.")
            print(f"Убедитесь, что PySide6 установлен и находится в переменной PATH.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Произошла ошибка при выполнении команды компиляции: {e}")
            sys.exit(1)


if '__main__' != __name__:
    ui_file_dir = Path('qt_assets/forms')
    ui_py_file_dir = Path('src/packages/qtviews/qtforms')
    compile_ui_to_py(ui_file_dir, ui_py_file_dir)

    qrc_file_path = Path('resources.qrc')
    output_py_file_path = Path('src/packages/qtviews/resources_rc.py')
    compile_qrc_to_py(qrc_file_path, output_py_file_path)
