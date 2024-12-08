from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class LineNumberWidget(QWidget):
    def __init__(self, text_edit):
        super(LineNumberWidget, self).__init__()
        self.text_edit = text_edit
        self.setFixedWidth(50)  # Set a fixed width for the line number area

        # Layout for the line number
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Initial update of line numbers
        self.update_line_numbers()

        # Connect events
        self.text_edit.textChanged.connect(self.update_line_numbers)
        self.text_edit.verticalScrollBar().valueChanged.connect(self.update_line_numbers)

    def update_line_numbers(self):
        """Update the line numbers displayed in the widget."""
        text = self.text_edit.toPlainText()
        lines = text.splitlines()

        # Clear the current layout
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Add line numbers to the layout
        for i, line in enumerate(lines):
            line_number_label = QLabel(str(i + 1))
            line_number_label.setAlignment(Qt.AlignRight)
            self.layout.addWidget(line_number_label)
