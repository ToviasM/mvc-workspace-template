
from PySide6.QtCore import Signal, QObject
from  .inspector_view import InspectorView
from  .asset_list_view import AssetListView
from .asset_browser_view import AssetBrowserView
from .asset_team_view import AssetTeamView

class AssetBrowserModel(QObject):
    __panels__ = {
        "PANEL_inspector" : InspectorView,
        "PANEL_asset_list" : AssetListView,
        "PANEL_team" : AssetTeamView,
    }

    __views__ = {
        "VIEW_asset_list" : {"RIGHT" : InspectorView, "CENTRAL" : AssetListView}
    }

    view_changed = Signal(dict)

    def __init__(self, view=None) -> None:
        super().__init__()
        self._view = view or self.__views__["VIEW_asset_list"]

    def set_view(self, view=None):
        self._view = view or self.__views__["VIEW_asset_list"]
        self.view_changed.emit(self._view)

    def get_view(self):
        return self._view