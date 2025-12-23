import subprocess
import sys

from pathlib import Path


def compile_qrc() -> None:
    """
    Запускает команду pyside6-rcc для компиляции QRC файла.
    """
    platform = sys.platform
    env_bin_path = Path(sys.executable).parent
    print(env_bin_path)
    qrc_file = Path('resources.qrc')
    output_py_file = Path('src/views/generated/resources_rc.py')

    # Проверяем наличие входного файла
    path_to_pyside6_rcc = Path('pyside6-rcc')
    if platform.startswith('linux'):
        path_to_pyside6_rcc = env_bin_path / path_to_pyside6_rcc
    if not qrc_file.exists():
        print(f"Ошибка: Исходный файл ресурсов не найден: {qrc_file}")
        sys.exit(1)
    # Формируем команду для выполнения мы используем 'pyside6-rcc' как имя исполняемого файла
    command = [
        path_to_pyside6_rcc.as_posix(),
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


def compile_ui() -> None:
    """
    Запускает команду pyside6-uic для компиляции ui файла.
    """
    platform = sys.platform
    env_bin_path = Path(sys.executable).parent
    ui_files = Path('assets/qt_assets/forms')
    ui_py_files = Path('src/views/windows')

    path_to_pyside6_uic = Path('pyside6-uic')
    if platform.startswith('linux'):
        path_to_pyside6_uic = env_bin_path / path_to_pyside6_uic
    for elem in ui_files.iterdir():
        if not (elem.is_file() or elem.suffix == '.ui'):
            continue
        # Формируем команду для выполнения 'pyside6-uic' как имя исполняемого файла
        py_file = elem.with_suffix('.py').name
        output_py_path = ui_py_files / elem.with_suffix('.py').name
        command = [
            path_to_pyside6_uic.as_posix(),
            elem.as_posix(),
            '-o',
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
