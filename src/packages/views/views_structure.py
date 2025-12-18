import enum


class QtResources(enum.StrEnum):
    pass


class PageStructure(enum.IntEnum):
    pass


class QtStyleResources(QtResources):
    MAIN_WINDOW_STYLE = ':/styles/main_window_style.qss'
    MAIN_MENU_STYLE = ':/styles/main_menu_style.qss'


class MainWindowPages(PageStructure):
    MAIN_MENU = 0
    REPORT_CREATION = 1
    PROTOCOL_CREATION = 2