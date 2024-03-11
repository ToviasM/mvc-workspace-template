from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QDockWidget

class AssetBrowserView(QMainWindow):
    def __init__(self, model, controller) -> None:
        super().__init__()
        self.setWindowTitle("Asset Browser")

        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout(self.centralWidget)
        
        self.setCentralWidget(self.centralWidget)

        self.controller = controller
        self.model = model
        self.docks = []
        self.central_widget = None

        self.draw()
    
    def draw(self): 
        
        button = QPushButton("Update View")
        button.clicked.connect(lambda : self.controller.change_view(self.model))
        self.centralLayout.addWidget(button)

        self.setup_view()
        self.model.view_changed.connect(self.update_view)
    
    def update_view(self, view):

        for dock in self.docks:
            self.removeDockWidget(dock)
        self.docks.clear()

        self.centralLayout.removeWidget(self.central_widget)
        self.central_widget.deleteLater()
        self.centralWidget.update()

        self.setup_view(view=view)

    def setup_view(self, view = None):
        current_view = view or self.model.get_view()
        for item in current_view.keys():
            widget = current_view[item]()
            if item == 'CENTRAL':
                self.central_widget = widget
                self.centralLayout.addWidget(self.central_widget)
            else:
                dock = QDockWidget(widget.__label__)
                dock.setWidget(widget)
                self.docks.append(dock)

                if item == 'RIGHT':
                    self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
                elif item == 'LEFT':
                    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock) 
                elif item == 'BOTTOM':
                    self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock)

        

        


