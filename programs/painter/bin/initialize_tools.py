import winreg
import json

import tools_library

painter_reg_name = "Software\\Allegorithmic\\Substance Painter\\Shelf\\pathInfos"


def addShelf(shelf_name, shelf_path, shelf_status):
    """Adds a new shelf to the painter registry

    shelf_name - name of the shelf to add, must be lower case
    shelf_path - absolute path to the shelf
    shelf_status - false = enabled, true = disabled
    """
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


with open(tools_library.getConfig("asset_library\\shelf_libraries.json")) as j:
    json_data = json.load(j)

    for i in json_data:
        if(json_data[i]["type"] == "Painter"):
            shelf_name = json_data[i]["name"]
            shelf_path = tools_library.finalizeString(json_data[i]["path"])
            shelf_enabled = json_data[i]["enabled"]

            addShelf(shelf_name, shelf_path, shelf_enabled)