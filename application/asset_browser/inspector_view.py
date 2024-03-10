from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class InspectorView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple")
        self.setGeometry(100,100,400,400)

        layout = QVBoxLayout(self)
        label = QLabel("Test")
        layout.addWidget(label)