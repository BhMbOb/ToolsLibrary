import os
import winreg
import json
from win32com.shell import shell, shellcon
import shutil

import tools_library


def copyStartup():
    """copy the "libs/install/tools_library.py" to the users "documents/allegorithmic/substance painter/python/startup" """
    shutil.copyfile(
        tools_library.finalizeString("$(ToolsLibraryPath)programs\\painter\\libs\\initialize\\tools_library.py"),
        tools_library.finalizeString("$(Documents)Allegorithmic\\Substance Painter\\python\\") + "startup\\tools_library.py"
    )


def addShelf(shelf_name, shelf_path, shelf_status):
    """Adds a new shelf to the painter registry

    shelf_name - name of the shelf to add, must be lower case
    shelf_path - absolute path to the shelf
    shelf_status - false = enabled, true = disabled
    """
    painter_reg_name = "Software\\Allegorithmic\\Substance Painter\\Shelf\\pathInfos"

    shelf_name = shelf_name.lower()
    shelf_path = shelf_path.replace("\\", "/")
    shelf_path = shelf_path if (shelf_path[-1] != "/") else shelf_path[0:-1]
    shelf_status = "false" if shelf_status else "true"


    # load the key "reg_name" and build the shelf registry path
    painter_config = tools_library.getConfig("Painter:program.json")
    painter_reg_name = ""

    with open(painter_config) as j:
        json_data = json.load(j)
        painter_reg_name = json_data["reg_name"] + "\\Shelf\\pathInfos"


    #
    reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

    key = winreg.OpenKey(reg_connection, painter_reg_name, winreg.KEY_READ)
    subkey_count = winreg.QueryInfoKey(key)[0]

    shelf_number = 0
    already_exists = False

    for x in range(subkey_count):
        subkey_name = winreg.EnumKey(key, x)

        target_key = winreg.OpenKey(key, subkey_name, 0, winreg.KEY_ALL_ACCESS)
        target_key_name = winreg.QueryValueEx(target_key, "name")[0]

        # if we find a key with the target name - update the path
        if(target_key_name == shelf_name):
            already_exists = True
            winreg.SetValueEx(target_key, "disabled", 0, winreg.REG_SZ, shelf_status)
            winreg.SetValueEx(target_key, "name", 0, winreg.REG_SZ, shelf_name)
            winreg.SetValueEx(target_key, "path", 0, winreg.REG_SZ, shelf_path)

        target_key.Close()

        if(int(subkey_name) > shelf_number):
            shelf_number = int(subkey_name)

    shelf_number += 1

    if(not already_exists):
        new_key = winreg.CreateKey(key, str(shelf_number))
        winreg.SetValueEx(new_key, "disabled", 0, winreg.REG_SZ, shelf_status)
        winreg.SetValueEx(new_key, "name", 0, winreg.REG_SZ, shelf_name)
        winreg.SetValueEx(new_key, "path", 0, winreg.REG_SZ, shelf_path)

        new_key.Close()
        key.Close()

    # increase shelf count if needed
    key = winreg.OpenKey(reg_connection, painter_reg_name, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "size", 0, winreg.REG_DWORD, winreg.QueryInfoKey(key)[0])
    key.Close()


def initializeShelves():
    """Add all shelves stored in the shelf_libraries config"""
    shelves_path = tools_library.finalizeString("$(AssetLibraryPath)Shelves\\Painter")
    for i in os.listdir(shelves_path):
        shelf_path = os.path.join(shelves_path, i)
        if(os.path.isdir(shelf_path)):
            shelf_name = "tl_" + i
            
            addShelf(shelf_name, shelf_path, "true")


copyStartup()
initializeShelves()
