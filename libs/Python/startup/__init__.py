import os
import sys
import importlib
import imp
import json
import winreg


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


# append the tools_library to sys.path
def path():
    """Returns the stored tools library root path as stored in the registry"""
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


def is_module_enabled(module_name, module_outer_dir="programs"):
    output = True
    client_settings_path = os.path.join(path(), "config\\client_settings.json")
    if(os.path.isfile(client_settings_path)):
        if(module_name != "python"):
            enabled = get_property(client_settings_path, module_outer_dir + "." + module_name + ".enabled")
            if(enabled == False):
                output = False
    return output


if(is_module_enabled(__program_context__.lower(), module_outer_dir="programs")):

    # base libs
    sys.path.append(os.path.join(path(), "libs\\Python"))

    # current python version as stored in configs
    python_version = get_property(
        os.path.join(path(), "config\\client_settings.json"),
        "programs." + __program_context__ + ".python_version"
    )
    if(python_version == ""):
        python_version = 3.8

    sys.path.append(os.path.join(path(), "libs\\External\\Python" + str(python_version)))

    # add all plugin dirs to path
    import tools_library

    # global value stores the current program that this python instance is ran within
    # (Ie, "unreal", "max", "python")
    tools_library.PROGRAM_CONTEXT = __program_context__
    program_context = tools_library.programContext()

    # Add all of the individual programs to their parent plugins
    #program_module_dir = os.path.join(path(), "programs", __program_context__, "libs\\python\\", __program_context__)
    #if(os.path.isdir(program_module_dir)):
    #    module = imp.load_source("tools_library." + __program_context__, os.path.join(program_module_dir, "__init__.py"))
    #    exec("sys.modules[\"tools_library\"]." + __program_context__ + " = module")



    from tools_library.types.framework.module import ProgramData, PythonFrameworkData, PluginData

    program = ProgramData(program_context)
    python_framework = PythonFrameworkData()
    program.initialize_paths()

    plugins = [PluginData(os.path.basename(plugin_dir)) for plugin_dir in tools_library.pluginDirs()]
    for plugin in plugins:
        plugin.initialize_paths()



    # loop / run all of the startup scripts in the order:
    # Python -> Plugins -> Core Program -> Plugin Program
    for i in range(99):

        # Run Core Python
        python_framework.run_startup(i)

        # Run Plugins
        for plugin in plugins:
            plugin.run_plugin_startup(i)

        # Run Programs
        program.run_program_startup(i)

        # Run Plugin Program
        for plugin in plugins:
            plugin.run_program_startup(i)

