import os
import sys
import sd
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets
import subprocess

import tools_library
import tools_library.utilities.string as string_utils
from tools_library.framework.module import PluginData, ProgramData


designer_path = os.path.join(tools_library.path(), "programs\\designer")
designer_tools_path = os.path.join(designer_path, "tools\\")


#
branch_menus = {}


def add_menu_branch(parent_menu, branch_string, script_path=""):
    """Adds a new menu branch from a path string (Ie, "a\\b\\c")"""
    branch_string_split = branch_string.split("\\")
    current_branch_full = ""

    for current_branch_name in branch_string_split:
        current_branch_full = os.path.join(current_branch_full, current_branch_name)
        current_branch_upper = os.path.dirname(current_branch_full)

        if(current_branch_upper in list(branch_menus)):
            q_menu_parent = branch_menus[current_branch_upper]
        else:
            q_menu_parent = parent_menu

        if(current_branch_full == branch_string):
            # if we're adding the final one (the script which will be launched)
            q_new_menu = q_menu_parent.addAction(string_utils.format.snake_to_name(current_branch_name))
            q_new_menu.script_path = script_path
            q_new_menu.triggered.connect(partial(tools_library.run_tool, q_new_menu.script_path))
        elif(current_branch_full not in list(branch_menus)):
            # if we're just adding a submenu
            q_new_menu = q_menu_parent.addMenu(string_utils.format.snake_to_name(current_branch_name))
            branch_menus[current_branch_full] = q_new_menu


def add_dir_as_branch(path_, parent_menu=None):
    """Loops over all subdirectories in a path and adds them as menus or actions"""
    possible_tool_dirs = [x[0] for x in os.walk(path_)]
    tool_paths = []
    tool_menu_branches = []

    for dir_ in possible_tool_dirs:
        if(os.path.isfile(os.path.join(dir_, "main.py"))):
            tool_menu_branches.append(dir_.replace(path_, ""))
            tool_paths.append(os.path.join(dir_, "main.py"))
        for dir_child in os.listdir(dir_):
            if(dir_child.endswith(".toolptr")):
                tool_menu_branches.append(os.path.join(dir_, dir_child.split(".")[0]).replace(path_, ""))
                tool_paths.append(os.path.join(dir_, dir_child))
    for i in range(len(tool_menu_branches)):
        add_menu_branch(parent_menu, tool_menu_branches[i], script_path=tool_paths[i])


def load_script_from_path(path):
    """Loads a python script from the input path"""
    path_ = path
    globals_ = {"__file__": path_}
    print(path_)
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

    # loop over all base designer tools and add them
    add_dir_as_branch(designer_tools_path, parent_menu=q_tools_menu)

    # loop over all separate plugins and add them and their branches
    q_tools_menu.addSeparator()
    for plugin_dir in tools_library.plugin_dirs():
        plugin_dir_tools_designer_dir = os.path.join(plugin_dir, "programs\\designer\\tools\\")
        plugin_name = os.path.basename(plugin_dir)
        if(PluginData(plugin_name).is_enabled):
            plugin_menu_branch = q_tools_menu.addMenu(string_utils.format.snake_to_name(plugin_name))
            if(os.path.exists(plugin_dir_tools_designer_dir)):
                add_dir_as_branch(plugin_dir_tools_designer_dir, parent_menu=plugin_menu_branch)

    # helper / additional
    q_tools_menu.addSeparator()

    q_show_in_explorer = q_tools_menu.addAction("Show In Explorer")
    q_show_in_explorer.triggered.connect(partial(tools_library.run_tool, "programs\\python\\scripts\\show_in_explorer.py"))

    q_open_git_repo = q_tools_menu.addAction("Github Repo")
    q_open_git_repo.triggered.connect(partial(tools_library.run_tool, "programs\\python\\scripts\\open_git_repo.py"))


sd_ui_mgr = sd.getContext().getSDApplication().getQtForPythonUIMgr()
initialize_tools_library_menu(sd_ui_mgr)
