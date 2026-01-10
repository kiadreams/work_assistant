import sys

from PySide6.QtWidgets import QApplication

from src.database.db_manager import DatabaseManager
from src.database.repositories import DivisionRepository
from src.gui.coordinators.app_coordinator import AppCoordinator
from src.services.EmployeeService import EmployeeService


def close_app() -> None:
    print("Closing app...")


if __name__ == "__main__":
    db_manager = DatabaseManager()
    employee_service = EmployeeService(DivisionRepository(db_manager))

    db_manager.create_db_tables()

    app = QApplication(sys.argv)
    coordinator = AppCoordinator(employee_service)
    coordinator.start_app()
    app.aboutToQuit.connect(close_app)
    sys.exit(app.exec())
