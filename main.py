import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from src.database.db_manager import DatabaseManager
from src.database.repositories import DivisionRepository
from src.gui.coordinators.app_coordinator import AppCoordinator
from src.services.EmployeeService import EmployeeService
from src.utils.database_data import export_data_to_json_files, import_from_json_files


def close_app() -> None:
    print("Closing app...")


if __name__ == "__main__":
    db_manager = DatabaseManager()
    employee_service = EmployeeService(DivisionRepository(db_manager))

    # Создание таблиц в базе данных
    # db_manager.create_db_tables()

    # Целевая директория хранения базы данных
    target_dir = Path(__file__).parent / "instance"

    # Запись данных всех таблиц в json файлы
    # export_data_to_json_files(db_manager.get_all_data_from_db(), target_dir)
    # Загрузка данных всех таблиц из json файлов
    import_from_json_files(target_dir, db_manager)

    app = QApplication(sys.argv)
    coordinator = AppCoordinator(employee_service)
    coordinator.start_app()
    app.aboutToQuit.connect(close_app)
    sys.exit(app.exec())
