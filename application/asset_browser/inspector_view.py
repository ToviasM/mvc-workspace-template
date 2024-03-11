from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class InspectorView(QWidget):
    __label__ = "Inspector"
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Inspector View")
        layout.addWidget(label)