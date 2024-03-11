from  .panels.asset_list_panel import PANEL_asset_list
from .panels.asset_team_panel import PANEL_asset_team
from .panels.inspector_panel import PANEL_inspector

class AssetBrowserController():

    def __init__(self) -> None:
        self.view_change = 0

    def change_view(self, model, view):
        model.set_view(model.__views__[view])