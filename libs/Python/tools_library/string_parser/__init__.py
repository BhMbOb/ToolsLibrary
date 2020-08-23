import os
import winreg
import json
from win32com.shell import shell, shellcon

import tools_library


def _parse__toolslibrarypath():
    return tools_library.path() + "\\"


def _parse__userdocuments():
    return shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0) + "\\"


def parse(input_):
    """Read an input string and parse in the values stored in "config\\string_parser_mappings.json" - run the defined function if required"""
    output = input_

    string_parser_mappings_path = tools_library.getConfig("string_parser_mappings.json")
    
    with open(string_parser_mappings_path) as j:
        json_data = json.load(j)

        for i in json_data:
            replace_value = "$(" + i + ")"
            replace_target = json_data[i]

            # a target value of $(some_text) defines a function - so run it to get the final value
            if("$(" in replace_target):
                replace_target = replace_target[2:-1]
                replace_target = eval(replace_target + "()")

            if(replace_value in output):
                output = output.replace(replace_value, replace_target)

    return output
