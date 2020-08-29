import os
import json

import tools_library
import tools_library.filemgr


def getPath(identifier, raw_string=False):
    """Returns the content library path from a given identifier"""
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


def absPath(relative_path):
    """Returns an absolute path from a content library relative path (Ie, "Common:Path/To/File.abc") """
    output = ""

    content_library_name = relative_path.split(":")[0] if (len(relative_path.split(":")) > 1) else "Common"
    path = relative_path.split(":")[1] if (len(relative_path.split(":")) > 1) else relative_path

    output = os.path.join(
        getPath(content_library_name),
        path
    )

    output = tools_library.string_parser.parse(output)

    return output


def make_content_library(library_dir, library_name):
    """Make a new content library with the default folder structure"""
    if(os.path.isdir(library_dir)):
        content_library_dir = os.path.join(library_dir, library_name)
        tools_library.filemgr.makedir(content_library_dir)
        with open(tools_library.getConfig("asset_library\\content_library_structure.json"), "r") as j:
            json_data = json.load(j)
            for i in json_data:
                tools_library.filemgr.makesubdirs(os.path.join(content_library_dir, i), json_data[i])
