import subprocess
import sys

from pathlib import Path


def compile_qrc_to_py(qrc_file: Path, output_py_file: Path,  env_bin_path: Path, platform: str) -> None:
    """
    Запускает команду pyside6-rcc для компиляции QRC файла.
    """
    # Проверяем наличие входного файла
    path_to_pyside6_rcc = 'pyside6-rcc'
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


def compile_ui_to_py(ui_files: Path, ui_py_files: Path, env_bin_path: Path, platform: str) -> None:
    """
    Запускает команду pyside6-uic для компиляции ui файла.
    """
    path_to_pyside6_uic = 'pyside6-uic'
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


if '__main__' != __name__:
    path_bin_env= Path(sys.executable).parent
    ui_file_dir = Path('qt_assets/forms')
    ui_py_file_dir = Path('src/packages/qtviews/qtforms')
    compile_ui_to_py(ui_file_dir, ui_py_file_dir, path_bin_env, sys.platform)

    qrc_file_path = Path('resources.qrc')
    output_py_file_path = Path('src/packages/qtviews/resources_rc.py')
    compile_qrc_to_py(qrc_file_path, output_py_file_path, path_bin_env, sys.platform)
