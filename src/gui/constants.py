import enum

from src.core.constants import PageStructure


class QtResources(enum.StrEnum):
    pass


class MainWindowPages(PageStructure):
    MAIN_MENU = 0
    REPORTS_WINDOW = 1
    PROTOCOLS_WINDOW = 2


class ReportsWindowPages(PageStructure):
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
