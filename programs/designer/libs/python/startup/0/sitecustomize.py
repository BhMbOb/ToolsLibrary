import os
import sys
import winreg
import json


def path():
    '''Returns the stored tools library root path as stored in the registry'''
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


sys.path.append(os.path.join(path(), "libs\\Python"))
sys.path.append(os.path.join(path(), "libs\\External\\Python3.8"))
sys.path.append(os.path.join(path(), "programs\\designer\\Python"))

# loop over all plugins and add their python libs to sys path
for i in os.listdir(os.path.join(path(), "plugins")):
    sys.path.append(os.path.join(path(), "plugins", i, "libs\\Python"))
