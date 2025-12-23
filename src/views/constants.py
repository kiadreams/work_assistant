import enum


class QtResources(enum.StrEnum):
    pass


class PageStructure(enum.IntEnum):
    pass


class QtStyleResources(QtResources):
    MAIN_WINDOW_STYLE = ':/styles/main_window_style.qss'
    MAIN_MENU_STYLE = ':/styles/main_menu_style.qss'
    REPORT_WIDGET_STYLE = ':/styles/report_widget_style.qss'
    REPORT_GENERATION_WIDGET_STYLE = ':/styles/report_generation_widget_style.qss'


class MainWindowPages(PageStructure):
    MAIN_MENU = 0
    REPORT_CREATION = 1
    PROTOCOL_CREATION = 2


class ReportGenerationPages(PageStructure):
    SERVICES_AND_GROUPS = 0
    STAFF = 1
    TYPES_OF_WORK = 2
    WORKS = 3
    ORDERS = 4
    WORK_EVENTS = 5
