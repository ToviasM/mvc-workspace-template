from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AssetListView(QWidget):
    __label__ = "Asset List"
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Asset List View")
        layout.addWidget(label)