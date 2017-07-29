from PyQt5.QtWidgets import QSplitter, QVBoxLayout, QWidget
from PyQt5 import QtCore


class TemplateMain(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        splitter_main = QSplitter(QtCore.Qt.Vertical)

        self.view = QWidget()

        self.sys_view = QWidget()

        self.sys_view.setStyleSheet("""
        .QWidget {
            border-top: 1px solid grey;
            border-bottom: 1px solid grey;
            }
        """)
        self.view.setStyleSheet("""
            .QWidget {
                border-bottom: 1px solid grey;
                }
        """)

        splitter_main.addWidget(self.view)
        splitter_main.addWidget(self.sys_view)
        splitter_main.setStretchFactor(0, 5)
        splitter_main.setStretchFactor(1, 4)
        splitter_main.setStyleSheet("""
        .QSplitter {
            background-color: rgb(255, 255, 255);
            }
        """)

        layout_main = QVBoxLayout()
        layout_main.addWidget(splitter_main)
        layout_main.setSpacing(0)
        layout_main.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout_main)