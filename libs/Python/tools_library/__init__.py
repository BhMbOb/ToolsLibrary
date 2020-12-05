import os
import sys
import json

from tools_library import *
from tools_library import string_parser
from tools_library import aliases

winreg = aliases.winreg


def path():
    '''Returns the stored tools library root path as stored in the registry'''
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


def show_in_explorer():
    """Opens the root to the Tools Library in windows explorer"""
    os.startfile(path())


def open_github_repo():
    """Opens the Github repo for the Tools Library in the web browser"""
    with open(getConfig("tools_library.json")) as j:
        json_data = json.load(j)
        url = json_data["url"]
        os.system("start \"\" " + url)


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


def pluginDirs():
    output = []
    for i in os.listdir(os.path.join(path(), "plugins")):
        possible_dir = os.path.join(path(), "plugins", i)
        if(os.path.isdir(possible_dir)):
            output.append(possible_dir)
    return output


def getConfig(name):
    '''Returns a config file from its path

    name    --  name of the config file to find, formatted "program:config/file/path.type" or ("config/file/path.type" for common)
    '''
    output = ""

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
    """Run a file"""
    path_ = file_path
    globals_ = {
        "__file__": path_,
        "__package__": os.path.dirname(file_path)
    }
    exec(open(path_).read(), globals_)


def run_tool(file_path):
    """Run a tool - adds the tool dir to sys.path temporarily"""
    path_ = file_path
    globals_ = {
        "__file__": path_,
        "__package__": os.path.dirname(file_path)
    }
    sys.path.append(os.path.dirname(file_path))
    exec(open(path_).read(), globals_)
    sys.path.remove(os.path.dirname(file_path))


finalizeString = string_parser.parse
