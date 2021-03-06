"""
Responsible for running the startup scripts and initializing the Tools Library workspace
"""
import os
import sys
import winreg
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets
import sd


def getProjectRoot():
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


designer_path = os.path.join(getProjectRoot(), "programs\\designer\\")


def initializeSDPlugin():

    def run_file_(file_path):
        path_ = file_path
        globals_ = globals()
        globals_["__file__"] = path_
        globals_["__package__"] = os.path.dirname(file_path)
        globals_["__program_context__"] = "designer"
        exec(open(path_).read(), globals_)

    run_file_(getProjectRoot() + "\\scripts\\startup\\__init__.py")


def uninitializeSDPlugin():
    sd_ui_mgr = sd.getContext().getSDApplication().getQtForPythonUIMgr()
    sd_ui_mgr.deleteMenu("tools_library")
