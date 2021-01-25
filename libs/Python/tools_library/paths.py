import os
import sys
import json
import winreg


def root():
    """Returns the stored tools library root path as stored in the registry"""
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value.lower()
    except WindowsError:
        return ""