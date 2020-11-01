import os
import sys
import sd
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets

import tools_library


designer_path = tools_library.path() + "programs\\designer"
designer_tools_path = "D:\\Data\\projects\\Development\\ToolsLibrary\\programs\\designer\\tools\\"


def load_script_from_path(path, q_action):
    """Loads a python script from the input path"""
    path_ = os.path.join(designer_tools_path, path)
    globals_ = {"__file__": path_}
    exec(open(path_).read(), globals_)


def create_menu(sd_ui_mgr, id_name, friendly_name):
    if(sd_ui_mgr):
        q_tools_menu = QtWidgets.QMenu(id_name, None)
        q_tools_menu.setObjectName(friendly_name)
        sd_ui_mgr.newMenu(friendly_name, id_name)
        return sd_ui_mgr.findMenuFromObjectName(id_name)
    return None


def initialize_tools_library_menu(sd_ui_mgr):
    if(sd_ui_mgr.findMenuFromObjectName("tools_library")):
        sd_ui_mgr.deleteMenu("tools_library")

    q_tools_menu = create_menu(sd_ui_mgr, "tools_library", "Tools Library")

    possible_tool_dirs = [x[0] for x in os.walk(designer_tools_path)]
    tool_dirs = []

    for dir_ in possible_tool_dirs:
        if(os.path.isfile(os.path.join(dir_, "main.py"))):
            tool_dirs.append(dir_.replace(designer_tools_path, ""))

    tool_menus = {}

    for current_dir_full in tool_dirs:
        current_dir = ""
        for current_dir_name in current_dir_full.split("\\"):
            current_dir = os.path.join(current_dir, current_dir_name)
            upper_dir = os.path.dirname(current_dir)

            if(upper_dir in list(tool_menus)):
                q_menu_parent = tool_menus[upper_dir]
            else:
                q_menu_parent = q_tools_menu

            if(current_dir == current_dir_full):
                q_menu_parent.addAction(os.path.basename(current_dir))
                q_new_menu.folder = current_dir
                q_new_menu.triggered.connect(partial(load_script_from_path, q_new_menu.folder + "/main.py"))
            else:
                q_new_menu = q_menu_parent.addMenu(os.path.basename(current_dir))
                tool_menus[current_dir] = q_new_menu

    q_tools_menu.addSeparator()
    q_tools_menu.addAction("Show In Explorer..")
    q_tools_menu.addAction("Github Repo")


sd_ui_mgr = sd.getContext().getSDApplication().getQtForPythonUIMgr()
initialize_tools_library_menu(sd_ui_mgr)


print("tools library startup")