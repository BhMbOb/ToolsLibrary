import os
import json


def getProperty(config_path, value):
    """Returns a top level property from a config path"""
    output = ""
    with open(config_path) as j:
        json_data = json.load(j)
        output = json_data[str(value)]
    return output