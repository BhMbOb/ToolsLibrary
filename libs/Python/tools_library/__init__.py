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
    """Gets the current program context (Ie, "designer" or "python")\n
    :return <str:context> Program context as set in the startup scripts - defaults to "python"\n
    """
    if("PROGRAM_CONTEXT" in globals()):
        return PROGRAM_CONTEXT
    else:
        return "python"


def program_names():
    """Get a list of all tools library program names\n
    :return <[str]:names> Listy of all program names\n
    """
    output = []
    programs_dir = os.path.join(path(), "programs")
    for i in os.listdir(programs_dir):
        dir_ = os.path.join(programs_dir, i)
        if("." not in i and os.path.isdir(dir_)):
            output.append(i.lower())
    return output


def plugin_dirs():
    """Returns a list containing paths to all Tools Library plugin directories\n
    :return <[str]:path> List of paths to the plugin roots\n
    """
    output = []
    for i in os.listdir(os.path.join(path(), "plugins")):
        possible_dir = os.path.join(path(), "plugins", i)
        if(os.path.isdir(possible_dir)):
            output.append(possible_dir)
    return output


def get_config(name):
    """Returns the path to a config from a Tools Library relative path string\n
    :param <str:name> Name of the config file to find - formatted 'program:config/file/path.type' or 'config/file/path.type'\n
    :return <str:path> Absolute path to the config\n
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
    """Run a single file\n
    :param <str:file_path> Absolute pat to the file to run\n
    """
    path_ = file_path
    globals_ = globals()
    globals_["__file__"] = path_
    globals_["__package__"] = os.path.dirname(file_path)
    globals_["__name__"] = "__main__"
    exec(open(path_).read(), globals_)


def run_tool(file_path):
    """Run a tool, this can be from a direct script or a .toolptr filepath\n
    :param <str:file_path> Path to the script or toolptr to run\n
    """
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


def is_module_enabled(module_name, module_type="programs"):
    """Returns whether a "module" is enabled, modules are either Tools Library Plugins or Programs\n
    :param <str:module_name> Name of the module to check\n
    :param <str:module_type> Either "plugins" or "programs"\n
    :return <bool:enabled> True if the module is enabled, false if not\n
    """
    output = True
    client_settings_path = os.path.join(path(), "config\\client_settings.json")
    if(os.path.isfile(client_settings_path)):
        if(module_name != "python"):
            enabled = json_utils.get_property(client_settings_path, module_type + "." + module_name + ".enabled")
            if(enabled == False):
                output = False
    return output


finalizeString = string_parser.parse