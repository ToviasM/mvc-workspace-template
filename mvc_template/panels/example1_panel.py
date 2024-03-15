from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .panel import Panel
class PANEL_example1(Panel):
    __label__ = "Example 1"
    __id__ = "PANEL_example1"
    def __init__(self, area, model):
        super().__init__(area, model)
    
    def draw(self):
        label = QLabel("Example 1 Panel")
        self.core_layout.addWidget(label)