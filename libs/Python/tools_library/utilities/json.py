"""
Library of json utility functions
"""
import os
import json


def get_property(file_path, value):
    """Returns a top level property from a config path"""
    search_list = value.split(".")

    with open(file_path) as j:
        json_data = json.load(j)

        prev_key = json_data
        for i in search_list:
            if(i in prev_key):
                prev_key = prev_key[i]
            else:
                return ""

    return prev_key


def set_file_property(file_path, property_name, property_value):
    """Sets a property in a config path"""
    keys_list = property_name.split(".")

    with open(file_path) as j:
        json_data = json.load(j)

    prev_key = json_data
    for i in range(len(keys_list)):
        if(keys_list[i] not in prev_key):
            prev_key[keys_list[i]] = {}
        if(i == len(keys_list) -1):
            prev_key[keys_list[i]] = property_value
        prev_key = prev_key[keys_list[i]]
    
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file, sort_keys=True, indent=True)
