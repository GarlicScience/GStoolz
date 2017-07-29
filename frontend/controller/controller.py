from frontend.controller import (console_controller,
                                 page_main_controller as _p_main_controller,
                                 page_balance_change_controller as _p_balance_change_controller)
from res.values.enum import *


class Controller:

    MainWidget = None
    MainConsole = None
    ConsoleController = None
    PageMainController = None
    PageBalanceChangeController = None

    @classmethod
    def init(cls, main_widget, main_console):

        cls.MainWidget = main_widget
        cls.MainConsole = main_console
        cls.__set_sys_view_layout(main_console)

        cls.ConsoleController = console_controller.ConsoleController(main_console)

        cls.PageMainController = _p_main_controller.PageMainController()
        cls.PageBalanceChangeController = _p_balance_change_controller.PageBalanceChangeController()

    @classmethod
    def set_page(cls, page):
        if page == PAGES.MAIN:
            def event():
                cls.__set_view_layout(cls.PageMainController.get_page())
            return event
        elif page == PAGES.BALANCE_CHANGE:
            def event():
                cls.__set_view_layout(cls.PageBalanceChangeController.get_page())
            return event
        else:
            def event():
                pass
            return event

    @classmethod
    def __set_view_layout(cls, layout):
        cls.MainWidget.view.setLayout(layout)

    @classmethod
    def __set_sys_view_layout(cls, layout):
        cls.MainWidget.sys_view.setLayout(layout)
