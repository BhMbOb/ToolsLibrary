"""
This file is copied to the max startup directory and ran on startup
It is in charge of running all sub-startup scripts
"""
import os
import sys
import winreg
import json

this__file__ = __file__

def path():
    '''Returns the stored tools library root path as stored in the registry'''
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


def run_file_(file_path):
    path_ = file_path
    globals_ = globals()
    globals_["__file__"] = path_
    globals_["__package__"] = os.path.dirname(file_path)
    globals_["__program_context__"] = "blender"
    exec(open(path_).read(), globals_)

run_file_(path() + "\\scripts\\startup\\__init__.py")
