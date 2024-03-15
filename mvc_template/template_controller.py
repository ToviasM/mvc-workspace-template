class AssetBrowserController():

    def __init__(self) -> None:
        self.view_change = 0

    def change_view(self, model, view):
        model.set_view(model.__views__[view])