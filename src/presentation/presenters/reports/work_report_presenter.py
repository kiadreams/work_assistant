from src.domain.services import EmployeeService
from src.gui.views.reports import WorkReportWidget


class WorkReportPresenter:
    def __init__(self, company_service: EmployeeService):
        self.company_service = company_service
        self._view = WorkReportWidget()

    def start(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> WorkReportWidget:
        return self._view

    def _connect_signals(self) -> None:
        pass

    def teardown(self) -> None:
        pass
