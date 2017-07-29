from frontend.gui import page_balance_change as _page_balance_change
from res.values import strings as _str
from frontend.controller.controller import *
import openpyxl


class PageBalanceChangeController:

    def __init__(self):
        self.__Page = _page_balance_change.PageBalanceChange()
        self.__workbook = None

    def get_page(self):
        return self.__Page

    def read_workbook(self, path):
        wb = openpyxl.load_workbook(filename=path)
        if self.__workbook is None:
            Controller.ConsoleController.add_error_text(_str.BALANCE_CHANGE_ERROR_WRONG_WB)
        else:
            pass
