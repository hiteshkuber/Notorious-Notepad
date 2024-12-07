from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        self.setup_ui()
        self.setup_window_control_button_positions()
        self.setup_window_control_button_control()
        self.setup_edit_menu()

    def setup_ui(self):
        """Load the UI and setup initial window properties."""
        uic.loadUi('editor.ui', self)

        # Remove the title bar and border
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

    def setup_edit_menu(self):
        """Connect actions in the edit menu to the appropriate methods."""
        self.actionFont_12pt.triggered.connect(lambda: self.change_size(12))
        self.actionFont_18pt.triggered.connect(lambda: self.change_size(18))
        self.actionFont_24pt.triggered.connect(lambda: self.change_size(24))

    def change_size(self, size: int):
        """Change the font size of the text editor."""
        self.textEdit.setFont(QFont('Arial', size))

    def setup_window_control_button_positions(self):
        """Position the window control buttons (minimize, maximize, close)."""
        new_x = self.get_right_corner()

        # Position buttons at the top-right corner
        self.minimizeButton.move(new_x - 70, 6)
        self.maximizeButton.move(new_x - 40, 6)
        self.closeButton.move(new_x - 10, 6)

    def setup_window_control_button_control(self):
        """Connect window control buttons to their respective actions."""
        self.minimizeButton.clicked.connect(self.minimize_screen)
        self.maximizeButton.clicked.connect(self.maximize_screen)
        self.closeButton.clicked.connect(self.close_screen)

    def maximize_screen(self):
        """Maximize the window."""
        self.showMaximized()

    def minimize_screen(self):
        """Minimize the window."""
        self.showMinimized()

    def close_screen(self):
        """Close the window."""
        self.close()

    def get_right_corner(self):
        """Calculate the x-coordinate for positioning buttons at the top-right."""
        window_width = self.width()
        button_width = self.maximizeButton.width()
        return window_width - button_width - 10  # 10px margin from the right


def main():
    """Initialize and run the application."""
    app = QApplication([])
    window = MyGUI()
    app.exec()


if __name__ == '__main__':
    main()
