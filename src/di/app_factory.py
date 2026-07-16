from __future__ import annotations

from typing import TYPE_CHECKING

from di.base_factory import BaseFactory
from presentation.gui import MainMenuWidget
from presentation.presenters import MainMenuPresenter

if TYPE_CHECKING:
    from db_manager import DatabaseManager

    from presentation.gui import MainWindow



class AppFactory(BaseFactory):
    def __init__(self, db_manager: DatabaseManager, main_window: MainWindow) -> None:
        super().__init__(db_manager)
        self.main_window = main_window

    def create_main_menu_widget(self):
        main_menu_widget = MainMenuWidget(self.main_window)
        main_menu_presenter = MainMenuPresenter(self.main_window)
