import sys
from PySide6.QtWidgets import QApplication
from mvc_template.template_model import AssetBrowserModel
from mvc_template.template_view import AssetBrowserView
from mvc_template.template_controller import AssetBrowserController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = AssetBrowserModel()
    controller = AssetBrowserController()
    main_window = AssetBrowserView(model, controller)
    main_window.show()
    sys.exit(app.exec())


#March 9th
#Create a Main Window Application
#Get authentication through FB or Google, and check if their email is in the user database (local db for now)
#If it is, return viable application and create a usable token
#Create core database functions in server for test

#Open Asset List in main portion
#Open Inspector on the side
#Get Asset Metadata in asset_list
#Display in view
#Right click display, and have load in graph if type is group or scene, and test assets if the asset is of asset type

#Check Time

##Next
##Integrate job system for testing assets
##Fill out metadata
##Create Node Graph Viewer
##Lock Assets
#Download Assets
#Upload Assets
