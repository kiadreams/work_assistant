from PySide6.QtWidgets import QDialog

# from src.gui.generated import Ui_DialogEditData
from src.gui.views.dialogs.base_dialog_view import BaseDialogView


class DialogEditView(BaseDialogView):
    def __init__(self) -> None:
        super().__init__()
        self.init_content_widget()
        self.__setup_connections()

    def init_content_widget(self) -> None:
        pass
        # self.setupUi(self)  # type: ignore[no-untyped-call]
        # self._init_widget_style(QtStyleResources.REPORT_WIDGET_STYLE)

    def __setup_connections(self) -> None:
        pass
