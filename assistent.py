import sys
import tomllib

from pathlib import Path

from PySide6 import QtWidgets

from src.packages.views.resource_loader import compile_ui_to_py, compile_qrc_to_py

# from src.packages.views.main_window import Ui_MainWindow
# from src.packages.worksheets.worksheets import WorkSheets
# from src.packages.models.employees import EmployeePosition, Employee, Department, Service
# from src.packages.models.devices import DeviceLocation, Device
# from src.packages.models.works import Work, WorkOrder, WorkEvent, TypeOfMaintenance
# from src.packages.models.association_tables import devices_in_works
# from src.packages.databases.database import create_db_tables


def get_version_from_file() -> str:
    """
    Читает версию напрямую из файла pyproject.toml.
    """
    # Находим корень проекта относительно текущего скрипта
    project_root = Path(__file__).resolve().parent
    toml_file = project_root / 'pyproject.toml'

    if not toml_file.exists():
        return 'N/A'

    with open(toml_file, 'rb') as f:
        data = tomllib.load(f)

    # Извлекаем версию по ключам [project] и version
    version = data.get('project', {}).get('version', 'N/A')
    return version


if __name__ == '__main__':
    compile_ui_to_py()
    compile_qrc_to_py()

    from src.packages.views.managers import main_window as mw

    app = QtWidgets.QApplication(sys.argv)
    work_assistent = mw.MainWindow(get_version_from_file())

    # Показываем главное окно
    work_assistent.show()

    # Запускаем основной цикл обработки событий
    sys.exit(app.exec())

    # create_db_tables()
    # b_title = 'Ведомость_работ.xlsx'
    # ws_first_title = 'Страница_1 V05110______'
    # ws_second_title = 'Страница_2 V05110______'
    # ws_third_title = 'Страница_2 V05110______'
    # if os.path.exists(b_title):
    #     os.remove(b_title)
    # work_sheet = WorkSheets(title=b_title)
    # work_sheet.set_content_of_active_ws()
    # work_sheet.change_active_ws_title(ws_first_title)
    # work_sheet.create_new_sheet(ws_second_title)
    # work_sheet.create_new_sheet(ws_third_title)
    # work_sheet.save_work_sheet()
