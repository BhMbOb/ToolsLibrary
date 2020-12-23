import os
import sys
import json

import tools_library


def path():
    return tools_library.finalizeString("$(AssetLibraryDir)")


def content_library_paths():
    output = []
    for i in os.listdir(os.path.join(path(), "content")):
        dirname = os.path.join(path(), "content", i)
        if(not i[0] in [".", "_"] and os.path.isdir(dirname)):
            output.append(dirname)
    return output


def is_valid_directory_name(name):
    output = True

    if("." in name):
        output = False

    if(name.startswith("_")):
        output = False

    return output
