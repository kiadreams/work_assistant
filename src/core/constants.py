from enum import IntEnum, StrEnum


class PageStructure(IntEnum):
    pass


class QtResources(StrEnum):
    pass


class MainWindows(PageStructure):
    MAIN_MENU = 0
    REPORTS_WINDOW = 1
    PROTOCOLS_WINDOW = 2


class ReportsViews(PageStructure):
    DIVISIONS = 0
    STAFF = 1
    WORK_TYPES = 2
    WORKS = 3
    ORDERS = 4
    WORK_EVENTS = 5


class QtStyleResources(QtResources):
    MAIN_WINDOW_STYLE = ":/styles/main_window_style.qss"
    MAIN_MENU_STYLE = ":/styles/main_menu_style.qss"
    REPORT_WIDGET_STYLE = ":/styles/report_widget_style.qss"
    REPORT_GENERATION_WIDGET_STYLE = ":/styles/report_generation_widget_style.qss"


class DbTables(StrEnum):
    DIVISIONS = "divisions"
    DEPARTMENTS = "departments"
    EMPLOYEE_POSITIONS = "employee_positions"
    EMPLOYEES = "employees"
    EQUIPMENT_LOCATIONS = "equipment_locations"
    EQUIPMENTS = "equipment"
    WORK_TYPES = "work_types"
    WORKS = "works"
    WORK_TASKS = "work_tasks"
    WORK_ORDERS = "work_orders"
