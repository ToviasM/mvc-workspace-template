
from PySide6.QtCore import Signal, QObject
from  .panels.inspector_panel import PANEL_inspector
from  .panels.asset_list_panel import PANEL_asset_list
from .asset_browser_view import AssetBrowserView
from .panels.asset_team_panel import PANEL_asset_team
from PySide6.QtWidgets import QWidget
from .panels.panel import Panel

from PySide6.QtCore import Qt
class AssetBrowserModel(QObject):
    
    __panels__ = {
        PANEL_inspector.__id__ : PANEL_inspector,
        PANEL_asset_list.__id__ : PANEL_asset_list,
        PANEL_asset_team.__id__ : PANEL_asset_team,
    }

    __views__ = {
        "VIEW_asset_list" : {"RIGHT" : PANEL_inspector.__id__ , "CENTRAL" : PANEL_asset_list.__id__},
        "VIEW_management" : {"RIGHT" : PANEL_asset_team.__id__, "CENTRAL" : PANEL_asset_list.__id__},
        "VIEW_relationships" : {"RIGHT" : PANEL_inspector.__id__, "CENTRAL" : PANEL_inspector.__id__, "LEFT" : PANEL_asset_list.__id__},
        "CUSTOM" : {},
    }
    __docks__ = {
        "RIGHT" : Qt.DockWidgetArea.RightDockWidgetArea,
        "LEFT" : Qt.DockWidgetArea.LeftDockWidgetArea,
        "BOTTOM" : Qt.DockWidgetArea.BottomDockWidgetArea,
    }
    view_changed = Signal(dict)
    panel_changed = Signal(Panel, str)

    def __init__(self, view=None) -> None:
        super().__init__()
        self._view = view or self.__views__["VIEW_asset_list"]

    def set_view(self, view):
        self._view = view
        self.view_changed.emit(self._view)

    def update_panel(self, widget, id):
        self.__views__["CUSTOM"] = self._view.copy()
        self._view = self.__views__["CUSTOM"]
        self._view[widget.area] = id
        self.panel_changed.emit(widget, id)

    def get_view(self):
        return self._view