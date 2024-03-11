from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class Panel(QWidget):
    __label__ = "Base Panel"
    __id__ = "PANEL_id"

    def __init__(self, area, model):
        super().__init__()
        self.area = area
        self.model = model

        self._layout = QVBoxLayout(self)
        self._central_widget = QWidget(self)
        self.core_layout = QVBoxLayout()
        self._central_widget.setLayout(self.core_layout)

        self._layout.addWidget(self._central_widget)
        self._draw_core()
        self.draw()
    
    def _draw_core(self):
        button = QPushButton("Change This Dock")
        button.clicked.connect(self.change_dock)
        self._layout.addWidget(button)

    def change_dock(self):
        self.model.update_panel(self, "PANEL_inspector")

    def draw(self):
        pass
