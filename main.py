import sys
from PyQt5.QtWidgets import QApplication
from ui import MyGUI


def main():
    """Initialize and run the application."""
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
