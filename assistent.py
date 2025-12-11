import os
import sys

from PySide6 import QtWidgets

from src.packages.forms.main_window import Ui_MainWindow
from src.packages.worksheets.worksheets import WorkSheets
from src.packages.models.employees import EmployeePosition, Employee, Department, Service
from src.packages.models.devices import DeviceLocation, Device
from src.packages.models.works import Work, WorkOrder, WorkEvent, TypeOfMaintenance
from src.packages.models.association_tables import devices_in_works
from src.packages.databases.database import create_db_tables


class MyApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем экземпляр сгенерированного интерфейса
        self.ui = Ui_MainWindow()

        # Инициализируем интерфейс, передавая ему текущее окно (self)
        self.ui.setupUi(self)

        # !!! Здесь добавляем всю нашу логику и обработчики событий !!!
        # Например, привязываем функцию к кнопке с objectName 'pushButton'
        # self.ui.pushButton.clicked.connect(self.handle_button_click)

    # def handle_button_click(self):
    #     """Метод, который вызывается при нажатии кнопки."""
    #     print("Кнопка была нажата!")
    #     # Меняем текст у виджета 'label' (если он есть в вашем UI файле)
    #     # self.ui.label.setText("Привет, мир!")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # Создаем экземпляр нашего приложения
    window = MyApplication()

    # Показываем главное окно
    window.show()

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
