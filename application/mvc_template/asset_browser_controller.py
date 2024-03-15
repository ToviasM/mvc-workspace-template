from  .panels.example1_panel import PANEL_asset_list
from .panels.example2_panel import PANEL_asset_team
from .panels.example3_panel import PANEL_inspector

class AssetBrowserController():

    def __init__(self) -> None:
        self.view_change = 0

    def change_view(self, model, view):
        model.set_view(model.__views__[view])