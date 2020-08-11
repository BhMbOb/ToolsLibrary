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


def getConfig(name):
    '''Returns a config file from its path'''
    output = os.path.join(path(), "config", name)
    if(os.path.exists(output)):
        return output
    else:
        return None


def getDefaultAssetLibrary():
    '''TEMP: Returns the local location of the asset library'''
    return "X:\\Assets"