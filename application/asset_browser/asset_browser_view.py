from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QDockWidget
from PySide6.QtGui import QAction
from .panels.panel import Panel

from .panels.asset_list_panel import PANEL_asset_list
from .panels.asset_team_panel import PANEL_asset_team
from .panels.inspector_panel import PANEL_inspector

class AssetBrowserView(QMainWindow):


    def __init__(self, model, controller) -> None:
        super().__init__()
        self.setWindowTitle("Asset Browser")
        self.setGeometry(100,100, 500, 500)

        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout(self.centralWidget)
        
        self.setCentralWidget(self.centralWidget)

        self.controller = controller
        self.model = model
        self.docks = {}
        self._central_widget = None

        self.draw()
    
    @property
    def central_widget(self):
        return self._central_widget
    
    @central_widget.setter
    def central_widget(self, widget):
        if self._central_widget is not None:
            self.centralLayout.removeWidget(self.central_widget)
            self._central_widget.deleteLater()
            self.centralWidget.update()
        self._central_widget = widget
        self.centralLayout.addWidget(self.central_widget)

    def draw(self): 
        self.setup_view()
        self.setup_menu_bar()
        self.model.view_changed.connect(self.update_view)
        self.model.panel_changed.connect(self.change_panel)
    
    def update_view(self, view):
        for dock in self.docks.values():
            self.removeDockWidget(dock)
        self.docks.clear()

        self.setup_view(view=view)

    def setup_view(self, view = None):
        current_view = view or self.model.get_view()
        for space, panel in current_view.items():
            widget = self.model.__panels__[panel](space, self.model)
            if space == 'CENTRAL':
                self.central_widget = widget
            else:
                dock = QDockWidget(widget.__label__)
                dock.setWidget(widget)
                self.docks[space] = dock
                self.addDockWidget(self.model.__docks__[space], dock)

    def change_panel(self, widget:Panel, panel:str):
        if widget.area == "CENTRAL":
            self.change_central(widget, panel)
        else: 
            self.change_dock(widget, panel)

    def change_dock(self, widget:Panel, panel:str):
        
        dock_area = widget.area
        self.removeDockWidget(self.docks[dock_area])
        
        
        widget = self.model.__panels__[panel](dock_area, self.model)
        
        new_dock = QDockWidget(widget.__label__)
        new_dock.setWidget(widget)
        self.docks[dock_area] = new_dock

        self.addDockWidget(self.model.__docks__[dock_area], new_dock)

    def change_central(self, widget, panel:str):
        widget = self.model.__panels__[panel](widget.area, self.model)
        self.central_widget = widget

    def setup_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        view_menu = menu_bar.addMenu('Workspace')

        asset_list_view_action = QAction('Asset List', self)
        asset_list_view_action.triggered.connect(lambda : self.controller.change_view(self.model, "VIEW_asset_list"))
        view_menu.addAction(asset_list_view_action)

        asset_list_view_action = QAction('Teams and Management', self)
        asset_list_view_action.triggered.connect(lambda : self.controller.change_view(self.model, "VIEW_management"))
        view_menu.addAction(asset_list_view_action)

        asset_list_view_action = QAction('Relationships', self)
        asset_list_view_action.triggered.connect(lambda : self.controller.change_view(self.model, "VIEW_relationships"))
        view_menu.addAction(asset_list_view_action)
        


