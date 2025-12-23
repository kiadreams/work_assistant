import subprocess
import sys
import tomllib

from pathlib import Path

from PySide6.QtCore import QFile, QIODevice, QTextStream, QStringConverter

from src.views.constants import QtResources, QtStyleResources


class ResourceLoader:
    def __init__(self, resource: QtResources) -> None:
        self.resource = resource
        self.__qfile = QFile(self.resource)

    def load_style(self) -> str | None:
        if not isinstance(self.resource, QtStyleResources):
            raise TypeError(f"Неверный тип ресурса, ожидался тип QtStyleResources, а передали {type(self.resource)}")
        if self.__check_qfile():
            stream = QTextStream(self.__qfile)
            stream.setEncoding(QStringConverter.Encoding.Utf8)
            stylesheet = stream.readAll()
            self.__qfile.close()
            return stylesheet
        else:
            return None

    def __check_qfile(self) -> bool:
        if not self.__qfile.open(QIODevice.OpenModeFlag.ReadOnly):
            print(f'Ошибка: Не удалось открыть QSS файл из ресурса по адресу {self.resource}')
            return False
        return True


def compile_qrc_to_py() -> None:
    """
    Запускает команду pyside6-rcc для компиляции QRC файла.
    """
    platform = sys.platform
    env_bin_path = Path(sys.executable).parent
    qrc_file = Path('resources.qrc')
    output_py_file = Path('src/packages/views/resources_rc.py')

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


def compile_ui_to_py() -> None:
    """
    Запускает команду pyside6-uic для компиляции ui файла.
    """
    platform = sys.platform
    env_bin_path = Path(sys.executable).parent
    ui_files = Path('qt_assets/qt_forms')
    ui_py_files = Path('src/packages/views/windows')

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
    version = data.get('project', {}).get('version', 'N/A')
    return version
