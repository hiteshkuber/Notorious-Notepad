from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from window_controls import WindowControls
from font_settings import FontSettings
from PyQt5.QtCore import Qt


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        self.setup_ui()
        self.setup_window_controls()
        self.setup_font_settings()

    def setup_ui(self):
        """Load the UI and setup initial window properties."""
        uic.loadUi('editor.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def setup_window_controls(self):
        """Setup window control buttons."""
        self.window_controls = WindowControls(self)
        self.window_controls.setup_window_control_button_positions()
        self.window_controls.setup_window_control_button_control()

    def setup_font_settings(self):
        """Setup font size settings."""
        self.font_settings = FontSettings(self)
        self.font_settings.setup_edit_menu()
