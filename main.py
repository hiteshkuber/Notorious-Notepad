from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)

        # Remove the title bar and border
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.show()

        self.actionFont_12pt.triggered.connect(lambda: self.change_size(12))
        self.actionFont_18pt.triggered.connect(lambda: self.change_size(18))
        self.actionFont_24pt.triggered.connect(lambda: self.change_size(24))

    def change_size(self, size: int):
        print("debug statement 1")
        self.textEdit.setFont(QFont('Arial', size))
        print("debug statement 2")

        # Print the current font size for verification
        print("Current font size after applying:", self.textEdit.font().pointSize())


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()


if __name__ == '__main__':
    main()
