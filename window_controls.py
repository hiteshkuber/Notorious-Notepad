class WindowControls:
    def __init__(self, window):
        self.window = window
        self.minimizeButton = self.window.minimizeButton
        self.maximizeButton = self.window.maximizeButton
        self.closeButton = self.window.closeButton

    def setup_window_control_button_positions(self):
        """Position the window control buttons (minimize, maximize, close)."""
        self.update_button_positions()  # Initial positioning

    def update_button_positions(self):
        """Update button positions based on the window size."""
        new_x = self.get_right_corner()
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
        self.window.showMaximized()

    def minimize_screen(self):
        """Minimize the window."""
        self.window.showMinimized()

    def close_screen(self):
        """Close the window."""
        self.window.close()

    def get_right_corner(self):
        """Calculate the x-coordinate for positioning buttons at the top-right."""
        window_width = self.window.width()
        button_width = self.maximizeButton.width()
        return window_width - button_width - 10  # 10px margin from the right
