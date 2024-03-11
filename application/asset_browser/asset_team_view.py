from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AssetTeamView(QWidget):
    __label__ = "Asset Team"
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Asset Team")
        layout.addWidget(label)