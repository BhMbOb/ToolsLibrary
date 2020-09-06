import os
import json

import tools_library

def getNames(context):
    """Returns the names of all available shelf libraries
    
    context - the program context to search for (Ie, "unreal")
    """
    output = []
    shelf_root = "$(AssetLibraryPath)Shelves\\" + context + "\\"
    shelf_root = tools_library.finalizeString(shelf_root)
    for i in os.listdir(shelf_root):
        if(os.path.isdir(os.path.join(shelf_root, i))):
            output.append(i)
    return output


def getPath(shelf_name, program_name, raw_string=False):
    """Returns the shelf library path from a given identifier"""
    output = ""
    output = "$(AssetLibraryPath)Shelves\\" + program_name + "\\" + shelf_name + "\\"
    output_abs = tools_library.finalizeString(output)

    if(not raw_string):
        output = output_abs

    if((not os.path.exists(output_abs))):
        output = ""

    return output


def absPath(relative_path):
    """Returns an absolute path from a shelf library relative path (Ie, "Common:Path/To/File.abc") """
    output = ""

    content_library_name = relative_path.split(":")[0] if (len(relative_path.split(":")) > 1) else "Common"
    path = relative_path.split(":")[1] if (len(relative_path.split(":")) > 1) else relative_path

    output = os.path.join(
        getPath(content_library_name),
        path
    )

    output = tools_library.string_parser.parse(output)

    return output
