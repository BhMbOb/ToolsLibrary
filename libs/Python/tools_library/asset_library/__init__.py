import os
import sys
import winreg
import json

import tools_library


def getAssetLibrary(identifier):
    """Returns the asset library from a given identifier"""
    output = ""
    config = tools_library.getConfig("asset_library\\asset_libraries.json")

    with open(config, "r") as j:
        json_data = json.load(j)

        for i in json_data:
            if(i == identifier):
                output = json_data[identifier]["path"]

    return output


def actualPath(relative_path):
    """Returns an absolute path from an asset library relative path (Ie, "Common:Path/To/File.abc") """
    output = ""

    asset_library_name = relative_path.split(":")[0] if (len(relative_path.split(":")) > 1) else "Common"
    path = relative_path.split(":")[1] if (len(relative_path.split(":")) > 1) else relative_path

    return os.path.join(
        getAssetLibrary(asset_library_name),
        path
    )
