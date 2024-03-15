from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .panel import Panel
class PANEL_example3(Panel):
    __label__ = "Example 3"
    __id__ = "PANEL_example3"

    def __init__(self, area, model):
        super().__init__(area, model)
    
    def draw(self):
        label = QLabel("Example 3 Panel")
        self.core_layout.addWidget(label)