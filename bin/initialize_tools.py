#
# Python 3
# Runs all "initialize_tools.py" files in "programs/program_name/bin/" folders
#


import os
import sys
import shutil
import pathlib
import stat
import glob
import winreg


root_folder = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "\\..")

# Add tools_library path to registry
try:
    reg_path = r"Software\\ToolsLibrary"
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "path", 0, winreg.REG_SZ, root_folder)
    winreg.CloseKey(registry_key)
    print("Successfully created key!")
except WindowsError:
    pass


# Initialize all programs
for i in os.listdir(root_folder + "\\programs"):
    initialize_tool_script_path = os.path.join(root_folder, "programs", i, "libs\\python\\install\\__init__.py")

    if(os.path.isfile(initialize_tool_script_path)):
        os.system("\"" + root_folder + "/bin/Python 3.8/python.exe\" " + initialize_tool_script_path)
