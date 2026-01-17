import sys

from PySide6.QtWidgets import QApplication

from gui.coordinators.app_coordinator import AppCoordinator
from src.database.db_manager import DatabaseManager
from src.database.repositories import DivisionRepository
from src.services.employee_service import EmployeeService


def close_app() -> None:
    print("Closing app...")


if __name__ == "__main__":
    db_manager = DatabaseManager()
    employee_service = EmployeeService(DivisionRepository(db_manager))

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

    app = QApplication(sys.argv)
    coordinator = AppCoordinator(employee_service)
    coordinator.start_app()
    app.aboutToQuit.connect(close_app)
    sys.exit(app.exec())
