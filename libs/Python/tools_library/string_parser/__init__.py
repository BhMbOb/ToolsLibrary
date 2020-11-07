import os
import winreg
import json
import ctypes.wintypes

import tools_library


def _parse__toolslibrarypath(params):
    """Returns the path to the tools library root folder"""
    return tools_library.path() + "\\"


def _parse__localappdata(params):
    """Returns the users "appdata\\local" folder"""
    return os.getenv("LOCALAPPDATA") + "\\"


def _parse__unrealprojectpath(params):
    """Returns the path to the currently active unreal project"""
    output = ""
    active_project_config_path = tools_library.getConfig("Unreal:active_project.json")

    with open(active_project_config_path) as j:
        json_data = json.load(j)
        output = json_data["path"]

    return output


def _parse__unrealprojectname(params):
    """Returns the path to the currently active unreal projects name"""
    output = ""
    active_project_config_path = tools_library.getConfig("Unreal:active_project.json")

    with open(active_project_config_path) as j:
        json_data = json.load(j)
        output = json_data["path"]

    return os.path.basename(os.path.dirname(output))


def _parse__assetlibrarypath(params):
    """Returns the path to the currently active asset library project"""
    output = ""
    active_project_config_path = tools_library.getConfig("Asset_Library:active_project.json")

    with open(active_project_config_path) as j:
        json_data = json.load(j)
        output = json_data["path"]

    return output


def _parse__userdocuments(params):
    """Returns the path to the current users documents"""
    CSIDL_PERSONAL = 5
    SHGFP_TYPE_CURRENT = 0
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
    return str(buf.value)


def _parse__folderpath(params):
    """Returns the path to the file_context's parent folder - relative to its asset_library"""
    if(params["file_context"]):
        return (os.path.dirname(params["file_context"]) + "\\")
    return "$(RelativeFolderPath)"


def _parse__foldername(params):
    if(params["file_context"]):
        return os.path.basename(os.path.dirname(params["file_context"]))
    return "$(FolderName)"


def parse(input_, file_context=None):
    """Read an input string and parse in the values stored in "config\\string_parser_mappings.json" - run the defined function if required"""
    output = input_

    params = {
        "file_context": file_context
    }

    string_parser_mappings_path = tools_library.getConfig("string_parser_mappings.json")

    with open(string_parser_mappings_path) as j:
        json_data = json.load(j)

        for i in json_data:
            replace_value = "$(" + i + ")"
            replace_target = json_data[i]

            # a target value of $(some_text) defines a function - so run it to get the final value
            if("$(" in replace_target):
                replace_target = replace_target[2:-1]
                replace_target = eval(replace_target + "(params)")

            if(replace_value in output):
                output = output.replace(replace_value, replace_target)

    return output
