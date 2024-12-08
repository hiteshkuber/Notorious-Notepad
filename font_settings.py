from PyQt5.QtGui import QFont


class FontSettings:
    def __init__(self, window):
        self.window = window

    def setup_edit_menu(self):
        """Connect actions in the edit menu to the appropriate methods."""
        self.window.actionFont_12pt.triggered.connect(lambda: self.change_size(12))
        self.window.actionFont_18pt.triggered.connect(lambda: self.change_size(18))
        self.window.actionFont_24pt.triggered.connect(lambda: self.change_size(24))

    def change_size(self, size: int):
        """Change the font size of the text editor."""
        self.window.textEdit.setFont(QFont('Arial', size))
