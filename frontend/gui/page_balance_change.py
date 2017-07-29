from PyQt5.QtWidgets import QVBoxLayout, QToolBar, QAction, QFileDialog, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


from res.values import strings as _str


class PageBalanceChange(QVBoxLayout):

    def __init__(self):
        QVBoxLayout.__init__(self)
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        self.setAlignment(Qt.AlignTop)
        toolbar = self.create_toolbar()

        self.addWidget(toolbar)

    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setStyleSheet("""
                .QToolBar {
                     background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #EEEEEE, stop: 1.0 #DDDDDD);
                     border-bottom: 1px solid #9a9a9a;
                     }
                """)

        add_xl_action = QAction(QIcon(_str.BALANCE_CHANGE_ICON_ADD_XL_PATH), _str.BALANCE_CHANGE_ICON_ADD_XL_TEXT, self)
        add_xl_action.triggered.connect(self.add_xl_action)

        toolbar.addAction(add_xl_action)

        return toolbar

    def add_xl_action(self):
        try:
            file_name = QFileDialog.getOpenFileName(QWidget(), _str.BALANCE_CHANGE_ICON_ADD_XL_TEXT, '/',
                                                    "Excel file (*.xlsx *.xls)")[0]
        except IOError as ioe:
            pass

