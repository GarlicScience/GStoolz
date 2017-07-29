import sys
from frontend.gui import main_window as _main_window, template_main as _template_main, console as _console
from res.values import dim as _dim
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from res.values.enum import *
from frontend.controller.controller import *


def main():
    app = QApplication(sys.argv)

    main_window = _main_window.MainWindow(_dim.main_window_width, _dim.main_window_height)
    main_window.setWindowState(QtCore.Qt.WindowMaximized)

    main_widget = _template_main.TemplateMain()
    main_console = _console.Console()

    main_window.setCentralWidget(main_widget)
    Controller.init(main_widget, main_console)
    Controller.set_page(PAGES.MAIN)

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
