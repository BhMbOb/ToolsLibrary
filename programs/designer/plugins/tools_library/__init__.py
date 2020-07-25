# copyright Allegorithmic. All rights reserved.

#TODO: UPDATE ME

from functools import partial
import os, sys

import sd

from PySide2 import QtCore, QtGui, QtWidgets, QtSvg

# Properties
tools_library_menu_name = "toolsLibrary"
tools_library_menu_identifier = "Tools Library"

# TODO: Replace this with a lib path
sys.path.append("X:/Tools/lib/python")
designer_path = "X:/Tools/programs/designer"


# Load a python script from its path
def loadScriptFromPath(path):
    global __name__            
    __name__ = "__main__"
    exec(open(path).read(), globals())

# Create and add a menu
def CreateMenu(sd_ui_manager, id_name, friendly_name):
    output = None

    if(sd_ui_manager):
        q_tools_menu = QtWidgets.QMenu(id_name, None)
        q_tools_menu.setObjectName(friendly_name)
        sd_ui_manager.newMenu(friendly_name, id_name)
        output = sd_ui_manager.findMenuFromObjectName(id_name)

    return output

# Initialize the tools library menu
def initializeToolsLibraryMenu(sd_ui_manager):

    if(sd_ui_manager):

        # delete the menu if it already exists
        if(sd_ui_manager.findMenuFromObjectName(tools_library_menu_name) != None):
            sd_ui_manager.deleteMenu(tools_library_menu_name)
        
        # create the 'Tools Menu'
        q_tools_menu = CreateMenu(sd_ui_manager, tools_library_menu_name, tools_library_menu_identifier)

        # loop over all tool folders and add them
        for folder in (os.listdir(designer_path + "/tools")):

            this_folder = designer_path + "/tools/" + folder

            # if there is a meta file...
            if(os.path.exists(this_folder + "/tools.meta")):
                pass

            if(os.path.exists(this_folder + "/main.py")):
                q_this_tool_submenu = q_tools_menu.addAction(folder)
                q_this_tool_submenu.folder = this_folder
                q_this_tool_submenu.triggered.connect(
                    partial( loadScriptFromPath, q_this_tool_submenu.folder + "/main.py" )
                )

# Initialize the tools library button collection
def initializeToolsLibraryButtons(sd_ui_manager):
    if(sd_ui_manager):
        pass
    
def initializeSDPlugin():
    sd_context = sd.getContext()
    sd_app = sd_context.getSDApplication()
    sd_ui_manager = sd_app.getQtForPythonUIMgr()

    if sd_ui_manager:
        initializeToolsLibraryMenu(sd_ui_manager)

#-- Uninitialize the plugin
def uninitializeSDPlugin():
    sd_context = sd.getContext()
    app = sd_context.getSDApplication()
    sd_ui_manager = app.getQtForPythonsd_ui_manager()

    if sd_ui_manager:
        sd_ui_manager.deleteMenu(tools_library_menu_name)
