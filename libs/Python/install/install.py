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


#
TOOLS_LIBRARY_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..\\..\\..\\"))
TOOLS_LIBRARY_PLUGINS_DIR = os.path.join(TOOLS_LIBRARY_ROOT_DIR, "plugins\\")
install_dirs = []

# add base startup dir (in "/programs")
install_dirs.append(os.path.dirname(__file__).replace("/", "\\"))

# add all base programs
for program_name in os.listdir(os.path.join(TOOLS_LIBRARY_ROOT_DIR, "programs")):
    program_install_dir = os.path.join(TOOLS_LIBRARY_ROOT_DIR, "programs", program_name, "libs\\python\\install")
    if(os.path.isdir(program_install_dir)):
        install_dirs.append(program_install_dir)

# add all plugin startup dirs (in "plugins/plugin_name/unreal/libs/python/startup")
for plugin_name in os.listdir(TOOLS_LIBRARY_PLUGINS_DIR):
    plugin_dir = os.path.join(TOOLS_LIBRARY_PLUGINS_DIR, plugin_name)
    install_dirs.append(os.path.join(plugin_dir, "libs\\python\\install"))
    for plugin_program_name in os.listdir(os.path.join(plugin_dir, "programs")):
        plugin_program_dir = os.path.join(plugin_dir, "programs", plugin_program_name, "libs\\python\\install")
        install_dirs.append(plugin_program_dir)

# loop over all of the startup directories in order of their names (Ie, 0..1..2)
for install_index in range(99):
    for install_dir in install_dirs:
        install_folder = install_dir + "/" + str(install_index)

        # run python files
        if(os.path.isdir(install_folder)):
            for file in os.listdir(install_folder):
                if(file.endswith(".py")):
                    file_path = os.path.join(install_folder, file)
                    __file__ = file_path
                    print("Tools Library: Ran Install Script: \"" + file_path + "\".")
                    exec(open(file_path).read())
                    __file__ = this__file__

print("Tools Library: All install scripts initialized.")
