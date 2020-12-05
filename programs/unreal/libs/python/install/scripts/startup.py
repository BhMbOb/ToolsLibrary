"""
This file is copied to the unreal project directory and ran on startup
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


def run_file(file_path):
    path_ = file_path
    globals_ = {"__file__": path_}
    exec(open(path_).read(), globals_)


run_file(path() + "\\programs\\unreal\\libs\\python\\startup\\__init__.py")
