from  .asset_list_view import AssetListView
from .asset_team_view import AssetTeamView

class AssetBrowserController():
    def __init__(self) -> None:
        pass

    def change_view(self, model):
        model.set_view({"RIGHT" : AssetTeamView, "MAIN" : AssetListView})