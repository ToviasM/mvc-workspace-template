from  .asset_list_view import AssetListView
from .asset_team_view import AssetTeamView
from .inspector_view import InspectorView

class AssetBrowserController():
    def __init__(self) -> None:
        self.view_change = 0

    def change_view(self, model):
        if self.view_change == 0:
            model.set_view({"RIGHT" : AssetTeamView, "CENTRAL" : AssetListView})
            self.view_change = 1
        elif self.view_change == 1:
            model.set_view({"RIGHT" : InspectorView, "CENTRAL" : AssetListView})
            self.view_change = 2
        elif self.view_change == 2:
            model.set_view({"LEFT" : AssetTeamView, "RIGHT" : InspectorView, "CENTRAL" : AssetListView})
            self.view_change = 0