import os
import sys
import imp

import tools_library
from tools_library.utilities import json as json_utils

if(tools_library.programContext() == "max"):
    import pymxs


class PythonFrameworkData(object):
    def __init__(self):
        self.directory = tools_library.paths.root()
        self.startup_dir = os.path.join(self.directory, "libs\\python\\startup")

    def run_startup(self, startup_index):
        base_python_startup_dir = os.path.join(self.startup_dir, str(startup_index))
        if(os.path.isdir(base_python_startup_dir)):
            for file in os.listdir(base_python_startup_dir):
                if(file.endswith(".py")):
                    tools_library.run_file(os.path.join(base_python_startup_dir, file))
                    print("[Tools Library][STARTUP] Ran Script -" + os.path.join(base_python_startup_dir, file))


class ProgramData(object):
    def __init__(self, program_name):

        self.program_name = program_name.lower()

        # returns whether the program is enabled in the context of the tools library
        enabled = json_utils.get_property(
            tools_library.getConfig("client_settings.json"),
            "programs." + program_name + ".enabled"
        )
        self.is_enabled = not (enabled == False)

        # returns whether the program is the one we're currently running from within
        self.is_current = (program_name.lower() == tools_library.programContext())

        self.directory = os.path.join(tools_library.paths.root(), "programs", self.program_name)
        self.startup_dir = os.path.join(self.directory, "libs\\python\\startup")

    def run_program_startup(self, startup_index):
        if(self.is_enabled):
            target_startup_dir = os.path.join(self.startup_dir, str(startup_index))
            if(os.path.isdir(target_startup_dir)):
                for file in os.listdir(target_startup_dir):
                    if(file.endswith(".py")):
                        tools_library.run_file(os.path.join(target_startup_dir, file))
                        print("[TOOLS LIBRARY][STARTUP] Ran Script: " + os.path.join(target_startup_dir, file))

            # if we're currently in Max it requires us to run the maxscripts
            dir_as_maxscript = target_startup_dir.replace("\\python", "\\maxscript")
            if(os.path.isdir(dir_as_maxscript)):
                for file in os.listdir(dir_as_maxscript):
                    if(file.endswith(".ms")):
                        file_path = os.path.join(dir_as_maxscript, file)
                        with open(file_path) as file:
                            file_lines = file.read()
                        pymxs.runtime.execute(file_lines)
                        print("[TOOLS LIBRARY][STARTUP] Ran Maxscript: " + file_path)

    def initialize_paths(self):
        if(self.is_current):
            sys.path.append(os.path.join(self.directory, "libs\\python"))

            # adds the current program as a module to the tools library (Ie, "tools_library.unreal")
            program_module_dir = os.path.join(tools_library.paths.root(), "programs", self.program_name, "libs\\python\\", self.program_name)
            if(os.path.isdir(program_module_dir)):
                module = imp.load_source("tools_library." + self.program_name, os.path.join(program_module_dir, "__init__.py"))
                exec("sys.modules[\"tools_library\"]." + self.program_name + " = module")


class PluginData(object):
    def __init__(self, plugin_name):
        
        self.plugin_name = plugin_name.lower()

        # returns whether this tools library plugin is enabled
        enabled = json_utils.get_property(
            tools_library.getConfig("client_settings.json"),
            "plugins." + plugin_name + ".enabled"
        )
        self.is_enabled = not (enabled == False)

        self.directory = os.path.join(tools_library.paths.root(), "plugins", self.plugin_name)
        self.startup_dir = os.path.join(self.directory, "libs\\python\\startup")
        self.current_program_dir = os.path.join(self.directory, "programs", tools_library.programContext())
        self.current_program_startup_dir = os.path.join(self.current_program_dir, "libs\\python\\startup")

    def run_plugin_startup(self, startup_index):
        if(self.is_enabled):
            target_startup_dir = os.path.join(self.startup_dir, str(startup_index))
            if(os.path.isdir(target_startup_dir)):
                for file in os.listdir(target_startup_dir):
                    if(file.endswith(".py")):
                        tools_library.run_file(os.path.join(target_startup_dir, file))
                        print("[TOOLS LIBRARY][STARTUP] Ran Script: " + os.path.join(target_startup_dir, file))

            # if we're currently in Max it requires us to run the maxscripts
            dir_as_maxscript = target_startup_dir.replace("\\python", "\\maxscript")
            if(os.path.isdir(dir_as_maxscript)):
                for file in os.listdir(dir_as_maxscript):
                    if(file.endswith(".ms")):
                        file_path = os.path.join(dir_as_maxscript, file)
                        with open(file_path) as file:
                            file_lines = file.read()
                        pymxs.runtime.execute(file_lines)
                        print("[TOOLS LIBRARY][STARTUP] Ran Maxscript: " + file_path)

    def run_program_startup(self, startup_index):
        if(self.is_enabled):
            target_startup_dir = os.path.join(self.current_program_startup_dir, str(startup_index))
            if(os.path.isdir(target_startup_dir)):
                for file in os.listdir(target_startup_dir):
                    if(file.endswith(".py")):
                        tools_library.run_file(os.path.join(target_startup_dir, file))
                        print("[TOOLS LIBRARY][STARTUP] Ran Script: " + os.path.join(target_startup_dir, file))

            # if we're currently in Max it requires us to run the maxscripts
            dir_as_maxscript = target_startup_dir.replace("\\python", "\\maxscript")
            if(os.path.isdir(dir_as_maxscript)):
                for file in os.listdir(dir_as_maxscript):
                    if(file.endswith(".ms")):
                        file_path = os.path.join(dir_as_maxscript, file)
                        with open(file_path) as file:
                            file_lines = file.read()
                        pymxs.runtime.execute(file_lines)
                        print("[TOOLS LIBRARY][STARTUP] Ran Maxscript: " + file_path)

    def initialize_paths(self):
        if(self.is_enabled):
            sys.path.append(os.path.join(self.directory, "libs\\python"))
            sys.path.append(os.path.join(self.directory, "programs", tools_library.programContext(), "libs\\python"))
            exec("import " + self.plugin_name)

            # adds the current plugin as a module to the main plugin module (Ie, "asset_library.unreal")
            plugin_module_dir = os.path.join(tools_library.paths.root(), "plugins", self.plugin_name, "programs", tools_library.programContext(), "libs\\python", tools_library.programContext())
            if(os.path.isdir(plugin_module_dir)):
                module = imp.load_source(self.plugin_name + "." + tools_library.programContext(), os.path.join(plugin_module_dir, "__init__.py"))
                exec("sys.modules[\"" + self.plugin_name + "\"]." + tools_library.programContext() + " = module")
