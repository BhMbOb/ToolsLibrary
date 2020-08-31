import os
import sys
import json
import winreg

import tools_library
from tools_library import asset_library


def list_texture_types():
    """Returns the names of all valid texture types as defined in "config/materials/properties.json" """
    output = []

    materials_json = tools_library.getConfig("materials\\properties.json")

    with open(materials_json, "r") as j:
        json_data = json.load(j)

        for i in range(len(json_data["texture_types"])):
            output.append(list(json_data["texture_types"])[i])

    return output