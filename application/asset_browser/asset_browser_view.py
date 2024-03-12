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

        self.controller = controller
        self.model = model
        self.docks = {}
        self._central_widget = QWidget()
        
        self.draw()
    
    @property
    def central_widget(self):
        return self._central_widget
    
    @central_widget.setter
    def central_widget(self, widget):
        self._central_widget = widget
        self.setCentralWidget(self._central_widget)

    def draw(self): 
        self.create_view()
        self.create_menu_bar()
        self.model.view_changed.connect(self.update_view)
        self.model.panel_changed.connect(self.change_panel)
    
    def update_view(self):
        "This function updates the current view by updating the cached docks, then updating the view"
        for dock in self.docks.values():
            self.removeDockWidget(dock)
        self.docks.clear()

        self.create_view()

    def create_view(self):
        """
        Creates the view based on the models stored view
        """
        current_view = self.model.get_view()
        for space, panel in current_view.items():
            widget = self.model.__panels__[panel](space, self.model)
            if space == 'CENTRAL':
                self.central_widget = widget
            else:
                dock = QDockWidget(widget.__label__)
                dock.setWidget(widget)
                self.docks[space] = dock
                self.addDockWidget(self.model.__docks__[space], dock)

    def change_panel(self, current_panel:Panel, panel:str):
        """
        Changes the current panel based on if it's a docked panel, or central widget
        
        args:
        widget (Panel): this is the current panel we are displaying
        panel (str) : This is the ID of the panel we would like to create
        """

        if current_panel.area == "CENTRAL":
            self.change_central_panel(current_panel, panel)
        else: 
            self.change_dock_panel(current_panel, panel)

    def change_dock_panel(self, current_panel:Panel, panel:str):
        """
        Changes & Updates the dock at the selected location, with the correct panel
        
        args:
        widget (Panel): this is the current panel we are displaying
        panel (str) : This is the ID of the panel we would like to create
        """
        space = current_panel.area
        self.removeDockWidget(self.docks[space])
        
        widget = self.model.__panels__[panel](space, self.model)
        
        new_dock = QDockWidget(current_panel.__label__)
        new_dock.setWidget(current_panel)
        self.docks[space] = new_dock

        self.addDockWidget(self.model.__docks__[space], new_dock)

    def change_central_panel(self, current_panel, panel:str):
        widget = self.model.__panels__[panel](current_panel.area, self.model)
        self.central_widget = widget

    def create_menu_bar(self):
        "Creates the menu bar at the top of the screen"
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
        


