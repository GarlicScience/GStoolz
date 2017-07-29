from res.values import strings as _str


class ConsoleController:
    def __init__(self, console):
        self.ConsoleLayout = console

    def clear_text(self):
        self.ConsoleLayout.text.setText(_str.CONSOLE_DEFAULT_TEXT)

    def add_default_text(self, text):
        text = self.ConsoleLayout.text.toHtml() + self.__wrap(text, _str.HTML_CONSOLE_COLOR_DEFAULT)
        self.ConsoleLayout.text.setHtml(text)

    def add_notify_text(self, text):
        text = self.ConsoleLayout.text.toHtml() + self.__wrap(text, _str.HTML_CONSOLE_COLOR_NOTIFY)
        self.ConsoleLayout.text.setHtml(text)

    def add_error_text(self, text):
        text = self.ConsoleLayout.text.toHtml() + self.__wrap(text, _str.HTML_CONSOLE_COLOR_ERROR)
        self.ConsoleLayout.text.setHtml(text)

    def __wrap(self, text, color):
        return _str.HTML_CONSOLE_STRING_TAG.format(color, text)