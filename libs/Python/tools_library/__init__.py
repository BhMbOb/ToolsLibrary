import os
import sys
import json

from tools_library import *
from tools_library import string_parser
from tools_library import aliases
from tools_library import programs

winreg = aliases.winreg


def path():
    """Returns the stored tools library root path as stored in the registry"""
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


def programContext():
    if("PROGRAM_CONTEXT" in globals()):
        return PROGRAM_CONTEXT
    else:
        return "python"


def pluginDirs():
    """Returns the absolute paths to all plugin directories for the tools library"""
    output = []
    for i in os.listdir(os.path.join(path(), "plugins")):
        possible_dir = os.path.join(path(), "plugins", i)
        if(os.path.isdir(possible_dir)):
            output.append(possible_dir)
    return output


def getConfig(name):
    """Returns a config file from its path

    name    --  name of the config file to find, formatted "program:config/file/path.type" or ("config/file/path.type" for common)
    """
    output = ""

    valid_program_names = []
    for i in os.listdir(os.path.join(path(), "programs")):
        path_ = os.path.join(path(), "programs", i)
        if(os.path.isdir(path_)):
            valid_program_names.append(i.lower())

    valid_plugin_names = []
    for i in os.listdir(os.path.join(path(), "plugins")):
        plugin = os.path.join(path(), "plugins", i)
        if(os.path.isdir(plugin)):
            valid_plugin_names.append(i.lower())

    if(len(name.split(":")) == 2):
        path_context = name.split(":")[0].lower()
        if(path_context in valid_program_names):
            output = os.path.join(path(), "programs", name.split(":")[0], "config", name.split(":")[1])
        elif(path_context in valid_plugin_names):
            output = os.path.join(path(), "plugins", name.split(":")[0], "config", name.split(":")[1])
    else:
        output = os.path.join(path(), "config", name)

    if(not os.path.exists(output)):
        output = ""

    return output


def run_file(file_path):
    """Run a single file"""
    path_ = file_path
    globals_ = globals()
    globals_["__file__"] = path_
    globals_["__package__"] = os.path.dirname(file_path)
    exec(open(path_).read(), globals_)


def run_tool(file_path):
    """
    Run a tool, adds the tool dir to sys.path temporarily
    If the input is a ".toolptr" then the stored tool will be ran instead"""
    if(not os.path.exists(file_path)):
        file_path = os.path.join(path(), file_path)
    path_ = file_path
    globals_ = globals()
    globals_["__file__"] = path_
    globals_["__package__"] = os.path.dirname(file_path)
    if(file_path.endswith(".toolptr")):
        with open(file_path) as j:
            json_data = json.load(j)
            url = os.path.join(path(), json_data["path"])
            exec(open(url).read(), globals_)
    else:
        sys.path.append(os.path.dirname(file_path))
        exec(open(path_).read(), globals_)
        sys.path.remove(os.path.dirname(file_path))


finalizeString = string_parser.parse