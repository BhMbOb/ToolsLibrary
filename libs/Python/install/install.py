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

this__file__ = __file__

root_folder = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "\\..\\..\\..")

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

    install_scripts_dir = os.path.join(root_folder, "programs", i, "libs\\python\\install") + "\\"

    for subfolder_index in range(99):
        install_scripts_current_dir = install_scripts_dir + str(subfolder_index)

        if(os.path.isdir(install_scripts_current_dir)):
            for file in os.listdir(install_scripts_current_dir):
                current_script_path = install_scripts_current_dir + "\\" + file
                __file__ = current_script_path
                print("Ran Script: " + current_script_path)
                exec(open(current_script_path).read())
                __file__ = this__file__
