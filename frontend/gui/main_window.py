from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
from frontend.controller.controller import *
from res.values.enum import *
from res.values import strings as _str


class MainWindow(QMainWindow):

    menu_bar = None
    file = None
    tools = None

    def __init__(self, width, height):
        QMainWindow.__init__(self)

        self.resize(width, height)
        self.setWindowTitle(_str.MAIN_WINDOW_TITLE)
        self.statusBar()
        self.init_menu_bar()

    def init_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("""
        .QMenuBar {
                background: #EEEEEE;
                border-bottom: 1px solid #c5c5c5;
            }
        """)
        # File
        self.file = self.menu_bar.addMenu(_str.MAIN_WINDOW_MENU_BAR_FILE)

        file_action_exit = QAction(QIcon(), _str.MAIN_WINDOW_MENU_BAR_FILE_EXIT, self)
        file_action_exit.setShortcut(_str.MAIN_WINDOW_MENU_BAR_FILE_EXIT_SHORTCUT)
        file_action_exit.setStatusTip(_str.MAIN_WINDOW_MENU_BAR_FILE_EXIT_STATUS)
        file_action_exit.triggered.connect(qApp.quit)

        self.file.addAction(file_action_exit)

        # Tools
        self.tools = self.menu_bar.addMenu(_str.MAIN_WINDOW_MENU_BAR_TOOLS)

        tools_action_balance_change = QAction(QIcon(), _str.MAIN_WINDOW_MENU_BAR_TOOLS_BALANCE, self)
        tools_action_balance_change.setStatusTip(_str.MAIN_WINDOW_MENU_BAR_TOOLS_BALANCE_STATUS)
        tools_action_balance_change.triggered.connect(Controller.set_page(PAGES.BALANCE_CHANGE))

        self.tools.addAction(tools_action_balance_change)

