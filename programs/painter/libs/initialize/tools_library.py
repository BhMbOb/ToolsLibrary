"""
Runs the "startup/tools_library.py" - copied to the users documents/allegorithmic/python/startup folder
"""

import os
import sys
import shutil
import winreg


def start_plugin():
    reg_path = r"Software\\ToolsLibrary"
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
    tools_library_project_root, regtype = winreg.QueryValueEx(registry_key, "path")

    sys.path.append(os.path.join(tools_library_project_root, "libs\\python"))
    sys.path.append(os.path.join(tools_library_project_root, "programs\\painter\\libs"))
    from startup import startup


def close_plugin():
    pass


if __name__ == "__main__":
    start_plugin()
