
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget
from .panels.panel import Panel
from PySide6.QtCore import Qt

from  .panels.example3_panel import PANEL_example3
from .panels.example2_panel import PANEL_example2
from  .panels.example1_panel import PANEL_example1
from .template_view import AssetBrowserView

class AssetBrowserModel(QObject):
    
    "Panels defined by the classes we create"
    __panels__ = {
        PANEL_example3.__id__ : PANEL_example3,
        PANEL_example2.__id__ : PANEL_example2,
        PANEL_example1.__id__ : PANEL_example1,
    }

    "Preset views that we can create and display to the user"
    __views__ = {
        "VIEW_example1" : {"RIGHT" : PANEL_example1.__id__ , "CENTRAL" : PANEL_example3.__id__},
        "VIEW_example2" : {"RIGHT" : PANEL_example2.__id__, "CENTRAL" : PANEL_example1.__id__},
        "VIEW_example3" : {"RIGHT" : PANEL_example2.__id__, "CENTRAL" : PANEL_example3.__id__, "LEFT" : PANEL_example1.__id__},
        "CUSTOM" : {},
    }

    "The main windows dock areas associated with DockWidgetArea"
    __docks__ = {
        "RIGHT" : Qt.DockWidgetArea.RightDockWidgetArea,
        "LEFT" : Qt.DockWidgetArea.LeftDockWidgetArea,
        "BOTTOM" : Qt.DockWidgetArea.BottomDockWidgetArea,
    }

    view_changed = Signal()
    panel_changed = Signal(Panel, str)

    def __init__(self, view=None) -> None:
        super().__init__()
        self._view = view or self.__views__["VIEW_example1"]

    def set_view(self, view):
        self._view = view
        self.view_changed.emit()

    def update_panel(self, current_panel, panel):
        """
        Updates stored view and sends signal to update UI
        
        args:
        widget (Panel): this is the current panel we are displaying
        panel (str) : This is the ID of the panel we would like to create
        """

        self.__views__["CUSTOM"] = self._view.copy()
        self._view = self.__views__["CUSTOM"]
        self._view[current_panel.area] = panel
        self.panel_changed.emit(current_panel, panel)

    def get_view(self):
        return self._view