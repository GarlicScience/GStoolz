from PyQt5.QtWidgets import QTextEdit, QHBoxLayout
from PyQt5.QtGui import QTextDocument, QFont
from PyQt5.QtCore import QSize
from res.values import strings as _str


class Console(QHBoxLayout):

    def __init__(self):
        QHBoxLayout.__init__(self)

        self.setContentsMargins(0, 0, 0, 0)

        self.text = QTextEdit()
        self.addWidget(self.text)
        self.text.setText(_str.CONSOLE_DEFAULT_TEXT)
        self.text.setReadOnly(True)
        self.text.setStyleSheet("""
                .QTextEdit {
                    border-top: 1px solid grey;
                    }
                """)

        self.style_font()

    def style_font(self):
        doc = self.text.document()
        font = doc.defaultFont()
        font.setFamily("Courier")
        doc.setDefaultFont(font)
