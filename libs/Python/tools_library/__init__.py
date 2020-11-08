import os
import sys
import winreg
import json

from tools_library import *
from tools_library import string_parser


def path():
    '''Returns the stored tools library root path as stored in the registry'''
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


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


finalizeString = string_parser.parse
