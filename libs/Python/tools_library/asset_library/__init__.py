import os
import sys
import winreg
import json

#TEMP:
sys.path.append("Y:\\Development\\ToolsLibrary\\libs\\Python")
import tools_library


def assetsPath(identifier):
    '''Returns the assets library from a given identifier'''
    output = ""
    config = tools_library.getConfig("asset_library\\paths.json")

    with open(config, "r") as j:
        json_data = json.load(j)

        for i in json_data["assets"]:
            if(i == identifier):
                output = json_data["assets"][i]

    return output