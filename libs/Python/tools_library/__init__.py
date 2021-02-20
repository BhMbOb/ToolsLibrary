import os
import sys
import json

from tools_library import string_parser
from tools_library.utilities import aliases
from tools_library import programs
from tools_library import paths
from tools_library.utilities import json as json_utils

winreg = aliases.winreg


current_tool_path = ""
path = paths.root


def program_context():
    """Returns the current program context name - defaults to "python" """
    if("PROGRAM_CONTEXT" in globals()):
        return PROGRAM_CONTEXT
    else:
        return "python"


def plugin_dirs():
    """Returns the absolute paths to all plugin directories for the tools library"""
    output = []
    for i in os.listdir(os.path.join(path(), "plugins")):
        possible_dir = os.path.join(path(), "plugins", i)
        if(os.path.isdir(possible_dir)):
            output.append(possible_dir)
    return output


def get_config(name):
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
    globals_["__name__"] = "__main__"
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
    globals_["__name__"] = "__main__"

    global current_tool_path
    current_tool_path = file_path

    if(file_path.endswith(".toolptr")):
        with open(file_path) as j:
            json_data = json.load(j)
            url = os.path.join(path(), json_data["path"])
            globals_["__file__"] = url
            globals_["__package__"] = os.path.dirname(url)
            current_tool_path = url
            exec(open(url).read(), globals_)

    elif(file_path.endswith(".ms")):
        if(program_context() == "max"):
            import pymxs
            with open(file_path) as file:
                file_lines = file.read()
                pymxs.runtime.execute(file_lines)

    else:
        sys.path.append(os.path.dirname(file_path))
        exec(open(path_).read(), globals_)
        sys.path.remove(os.path.dirname(file_path))

    current_tool_path = ""


def is_module_enabled(module_name, module_outer_dir="programs"):
    output = True
    client_settings_path = os.path.join(path(), "config\\client_settings.json")
    if(os.path.isfile(client_settings_path)):
        if(module_name != "python"):
            enabled = json_utils.get_property(client_settings_path, module_outer_dir + "." + module_name + ".enabled")
            if(enabled == False):
                output = False
    return output


finalizeString = string_parser.parse