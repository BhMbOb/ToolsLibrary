import os
import sys
import json

import tools_library


def format_path(input_path):
    """Formats an input path string to match the standards"""
    output = input_path.replace("/", "\\")
    output = output.lower()
    output = output.rstrip("\\")
    if(output.endswith(":")):
        output += "\\"
    return output


def root():
    """Returns the path to the root of the current Asset Library"""
    return format_path(tools_library.finalizeString("$(AssetLibraryDir)"))


def path():
    """Returns the path to the current Asset Library .assetlibrary file"""
    return tools_library.utilities.json.get_property(
        tools_library.get_config("client_settings.json"),
        "plugins.asset_library.path"
    )


def get_content_modules():
    """Returns paths to all content modules (Ie, "asset_library/content/common" """
    output = []
    for i in os.listdir(os.path.join(root(), "content")):
        dirname = os.path.join(root(), "content", i)
        if(not i[0] in [".", "_"] and os.path.isdir(dirname)):
            output.append(format_path(dirname))
    return output


def get_content_module(module_name):
    """Returns the path to a specific content module - given an input module name"""
    for i in get_content_modules():
        folder_name = os.path.basename(i).lower()
        if(folder_name == module_name.lower()):
            return format_path(i)
    return ""


def get_content_module_names():
    """Returns the names of all content modules (Ie, common, env_01, env_02)"""
    output = []
    for i in get_content_modules():
        output.append(os.path.basename(i))
    return output


def map_path(real_path):
    """Takes an input filepath and maps it to be relative to the current asset library"""
    real_path = format_path(real_path)
    return format_path(real_path.lstrip(root() + "\\"))


def unmap_path(mapped_path):
    """Takes an input AssetLibrary relative filepath and returns the absolute file path"""
    mapped_path = format_path(mapped_path)
    return format_path(os.path.join(root(), mapped_path))


def module_name_from_path(mapped_path):
    """"""
    return mapped_path.split("\\")[1]