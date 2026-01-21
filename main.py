import sys

from PySide6.QtWidgets import QApplication

from di.app_container import AppContainer
from src.core.services import EmployeeService
from src.gui.coordinators.app_coordinator import AppCoordinator
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.repositories import DivisionRepository


def close_app() -> None:
    print("Closing app...")


if __name__ == "__main__":
    # db_manager = DatabaseManager()
    # employee_service = EmployeeService(DivisionRepository(db_manager))

    # Создание таблиц в базе данных
    # db_manager.create_db_tables()

    # Экспорт записей всех таблиц в CSV файлы
    # db_manager.export_to_csv_files()
    # Экспорт записей всех таблиц в JSON файлы
    # db_manager.export_to_json_files()

    # Загрузка записей во все таблицы из CSV файлов
    # db_manager.import_from_csv_files()
    # Загрузка записей во все таблицы из JSON файлов
    # db_manager.import_from_json_files()

    app_container = AppContainer()

    report_session_1 = app_container.report_session_factory(main_container=app_container)
    d1 = report_session_1.employee_service()
    d2 = report_session_1.employee_service()
    print(d1 is d2)

    report_session_2 = app_container.report_session_factory(main_container=app_container)
    mn = report_session_2.main_container().employee_service()
    d3 = report_session_2.main_container
    # d4 = report_session_2.employee_service()
    print(d3 is d4)
    print(d1 is d4)
    print(report_session_1 is report_session_2)

    # app = QApplication(sys.argv)
    # coordinator = AppCoordinator(employee_service)
    # coordinator.start_app()
    # app.aboutToQuit.connect(close_app)
    # sys.exit(app.exec())
