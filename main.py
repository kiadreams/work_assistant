import sys  # noqa

from PySide6.QtWidgets import QApplication

from src.di.app_factory import AppFactory
from src.data import DatabaseManager
from src.presentation.gui.views import MainWindow
from src.coordinators.app_coordinator import AppCoordinator


def close_app() -> None:
    print("Closing app...")


if __name__ == "__main__":
    # app_container = AppContainer()
    # db_manager = app_container.db_manager()
    # employee_service = EmployeeService(DivisionRepository(db_manager))

    # # Создание таблиц в базе данных
    # db_manager.create_db_tables()

    # # Экспорт записей всех таблиц в CSV файлы
    # db_manager.export_to_csv_files()
    # # Экспорт записей всех таблиц в JSON файлы
    # db_manager.export_to_json_files()

    # # Загрузка записей во все таблицы из CSV файлов
    # db_manager.import_from_csv_files()
    # # Загрузка записей во все таблицы из JSON файлов
    # db_manager.import_from_json_files()

    # Создаем приложение, его зависимости и запускаем главный цикл
    app = QApplication(sys.argv)

    db_manager = DatabaseManager()
    app_window = MainWindow()

    app_factory = AppFactory(db_connect=db_manager)
    app_coordinator = AppCoordinator(app_factory=app_factory, main_window=app_window)

    app_coordinator.start()

    app.aboutToQuit.connect(close_app)
    sys.exit(app.exec())
