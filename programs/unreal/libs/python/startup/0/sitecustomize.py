import os
import sys
import _winreg as winreg
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
sys.path.append(os.path.join(path(), "libs\\External\\Python2.7"))
sys.path.append(os.path.join(path(), "programs\\unreal\\Python"))