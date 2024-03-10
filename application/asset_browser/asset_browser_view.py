from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton

class AssetBrowserView(QMainWindow):
    def __init__(self, model, controller) -> None:
        super().__init__()
        self.setWindowTitle("Asset Browser")

        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout(self.centralWidget)
        
        self.setCentralWidget(self.centralWidget)

        self.controller = controller
        self.model = model
        self.draw()
    
    def draw(self): 
        self.label = QLabel("{model}".format(model=self.model.get_view()))
        button = QPushButton("Update View")
        button.clicked.connect(lambda:self.controller.change_view(self.model))
        
        self.centralLayout.addWidget(self.label)
        self.centralLayout.addWidget(button)
        self.model.view_changed.connect(self.update_view)
    
    def update_view(self, view):
        print("Test")
        self.label.setText("{model}".format(model=view))

    def initialize_view():
        pass

    def update_view():
        pass



