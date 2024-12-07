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

        self.setup_edit_menu()
        self.setup_window_control_button_positions()
        self.setup_window_control_button_control()

    def setup_edit_menu(self):
        self.actionFont_12pt.triggered.connect(lambda: self.change_size(12))
        self.actionFont_18pt.triggered.connect(lambda: self.change_size(18))
        self.actionFont_24pt.triggered.connect(lambda: self.change_size(24))

    def change_size(self, size: int):
        self.textEdit.setFont(QFont('Arial', size))

    def setup_window_control_button_positions(self):
        # getting the right most of the window
        new_x = self.get_right_corner()

        # moving the buttons to top right of the screen
        self.minimizeButton.move(new_x - 70, 6)
        self.maximizeButton.move(new_x - 40, 6)
        self.closeButton.move(new_x - 10, 6)

    def setup_window_control_button_control(self):
        self.minimizeButton.clicked.connect(self.minimize_screen)
        self.maximizeButton.clicked.connect(self.maximize_screen)
        self.closeButton.clicked.connect(self.close_screen)

    def maximize_screen(self):
        self.showMaximized()

    def minimize_screen(self):
        self.showMinimized()

    def close_screen(self):
        self.close()

    def get_right_corner(self):
        # Get the size of the window
        window_width = self.width()

        # Get the size of the maximize button (this assumes you set it in the UI file)
        button_width = self.maximizeButton.width()

        # Calculate the new position for the top-right corner
        return window_width - button_width - 10  # 10px margin from the right


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()


if __name__ == '__main__':
    main()
