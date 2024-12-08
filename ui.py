from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from window_controls import WindowControls
from font_settings import FontSettings
from PyQt5.QtCore import Qt, QPoint


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

        # Enable dragging functionality for the menu bar
        self.menubar.mousePressEvent = self.menuBarMousePressEvent
        self.menubar.mouseMoveEvent = self.menuBarMouseMoveEvent
        self.menubar.mouseReleaseEvent = self.menuBarMouseReleaseEvent

        # Track dragging state
        self.dragging = False
        self.drag_start_position = QPoint()

    def menuBarMousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def menuBarMouseMoveEvent(self, event):
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def menuBarMouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    def setup_window_controls(self):
        """Setup window control buttons."""
        self.window_controls = WindowControls(self)
        self.window_controls.setup_window_control_button_positions()
        self.window_controls.setup_window_control_button_control()

    def setup_font_settings(self):
        """Setup font size settings."""
        self.font_settings = FontSettings(self)
        self.font_settings.setup_edit_menu()

    def resizeEvent(self, event):
        """Override resize event to update button positions."""
        self.window_controls.update_button_positions()
        super(MyGUI, self).resizeEvent(event)  # Call the base class resize event
