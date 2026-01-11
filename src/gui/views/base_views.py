from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget


class BaseView(QWidget):
    def init_content_view(self) -> None:
        pass

    def __setup_connections(self) -> None:
        pass


class SessionWindow(BaseView):
    back_main_menu_signal = Signal()


# class MainWindowAbstract(QMainWindow, ABC):
#     @abstractmethod
#     def add_window(self, index: PageStructure, window: QWidget) -> None:
#         pass
#
#     @abstractmethod
#     def change_window(self, index: PageStructure) -> None:
#         pass
#
#
# class MainMenuWindowAbstract(QWidget, BaseViewAbstract, ABC):
#     open_reports_window_signal = Signal()
#     open_protocols_window_signal = Signal()
#     close_app_signal = Signal()


# class ReportsWindowProtocol(SessionWindowAbstract, ABC):
#     open_divisions_view_signal = Signal()
#     open_staff_view_signal = Signal()
#     open_work_types_view_signal = Signal()
#     open_orders_view_signal = Signal()
#     open_works_view_signal = Signal()
#     open_work_events_view_signal = Signal()
#
#     @abstractmethod
#     def add_view(self, index: PageStructure, view: Any) -> None: ...
#
#     def change_view(self, index: PageStructure) -> None: ...
#
#
# class DivisionViewAbstract(BaseViewAbstract, Protocol):
#     pass
#
#
# class StaffViewAbstract(BaseViewAbstract, Protocol):
#     pass

#
# class WorkTypeViewAbstract(BaseViewAbstract, Protocol):
#     pass
#
#
# class WorksViewAbstract(BaseViewAbstract, Protocol):
#     pass
#
#
# class WorkEventViewAbstract(BaseViewAbstract, Protocol):
#     pass
#
#
# class OrderViewAbstract(BaseViewAbstract, Protocol):
#     pass
