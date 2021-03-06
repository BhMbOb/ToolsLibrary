"""
Library of json utility functions
"""
import os
import json


def get_property(file_path, value):
    """Gets a property in a json file multi layer deep\n
    :param <str:file_path> Path to the json file\n
    :param <str:value> The value to search for (Ie, "parent.child")\n
    :return <value:out> Value as stored in the json file, "" if not found\n
    """
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


def has_property(file_path, value):
    """Returns whether a json file contains a property\n
    :path <str:file_path> The value to search for (Ie, "parent.child")\n
    :param <str:value> The value to search for (Ie, "parent.child")\n
    :return <bool:out> True if found, false if not\n
    """
    search_list = value.split(".")
    with open(file_path) as j:
        json_data = json.load(j)
        prev_key = json_data
        for i in search_list:
            if(i in prev_key):
                prev_key = prev_key[i]
            else:
                return False
    return True


def get_property_recursive(file_paths, value):
    """The same as get_property() but searches recursively through a list of json files until found or complete\n
    :param <[str]:file_paths> List of file paths to search\n
    :param <str:value> The value to search for (Ie, "parent.child")\n
    :return <value:out> Value as stored in the json file, "" if not found\n
    """
    for i in file_paths:
        if(has_property(i, value)):
            return get_property(i, value)
    return None


def set_file_property(file_path, property_name, property_value):
    """Sets a file property in a json file and saves it out\n
    :param <str:file_path> The file path to set the property in\n
    :param <str:property_name> The name of the property to set\n
    :param <str:property_value> The value to set the property as\n
    """
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
