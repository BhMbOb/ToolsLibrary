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


def getConfig(name):
    '''Returns a config file from its path
    
    name    --  name of the config file to find, formatted "program:config/file/path.type" or ("config/file/path.type" for common)
    '''
    output = ""

    if(len(name.split(":")) == 2):
        output = os.path.join(path(), "programs", name.split(":")[0], "config", name.split(":")[1])
    else:
        output = os.path.join(path(), "config", name)

    if(not os.path.exists(output)):
        output = ""

    return output


def finalizeString(string_):
    """Takes an input string with custom data identifiers (Ie, "$(ToolsLibraryPath)" ) and outputs the target string"""
    return string_parser.parse(string_)
