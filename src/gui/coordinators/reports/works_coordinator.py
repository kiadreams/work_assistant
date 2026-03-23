from src.core.services import CompanyService
from src.gui.views.reports import WorkReportView


class WorksCoordinator:
    def __init__(self, company_service: CompanyService):
        self.company_service = company_service
        self._view = WorkReportView()

    def start(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> WorkReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass

    def teardown(self) -> None:
        pass
