import os
import sys
import winreg
import json

import tools_library


def getContentLibrary(identifier, raw_string=False):
    """Returns the content library from a given identifier"""
    output = ""
    config = tools_library.getConfig("asset_library\\content_libraries.json")

    with open(config, "r") as j:
        json_data = json.load(j)

        for i in json_data:
            if(i == identifier):
                output = json_data[identifier]["path"]

    if(not raw_string):
        output = tools_library.finalizeString(output)

    return output


def actualPath(relative_path):
    """Returns an absolute path from a content library relative path (Ie, "Common:Path/To/File.abc") """
    output = ""

    content_library_name = relative_path.split(":")[0] if (len(relative_path.split(":")) > 1) else "Common"
    path = relative_path.split(":")[1] if (len(relative_path.split(":")) > 1) else relative_path

    return os.path.join(
        getContentLibrary(content_library_name),
        path
    )
