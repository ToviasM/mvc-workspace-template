from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .panel import Panel
class PANEL_inspector(Panel):
    __label__ = "Inspector"
    __id__ = "PANEL_inspector"

    def __init__(self, area, model):
        super().__init__(area, model)
    
    def draw(self):
        label = QLabel("Asset Inspector View")
        self.core_layout.addWidget(label)