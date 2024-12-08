from PyQt5.QtWidgets import *


class FileSettings:
    def __init__(self, window):
        self.window = window

    def setup_edit_menu(self):
        self.window.actionOpen.triggered.connect(self.open_file)
        self.window.actionSave.triggered.connect(self.save_file)

    def save_file(self):
        pass

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self.window, "Open File", "", "All Files (*);;Text Files (*.txt)")

        if filename != "":
            with open(filename, "r") as f:
                self.window.textEdit.setPlainText(f.read())

