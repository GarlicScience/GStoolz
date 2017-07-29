from frontend.gui import page_main as _page_main


class PageMainController:

    def __init__(self):
        self.__Page = _page_main.PageMain()

    def get_page(self):
        return self.__Page
