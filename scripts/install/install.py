"""
Runs all "initialize_tools.py" files in "programs/program_name/bin/" folders
"""
import os
import json
import sys
import shutil
import pathlib
import stat
import glob
import winreg


this__file__ = __file__


class Install(object):
    def __init__(self):
        self.root_folder = os.path.abspath(os.path.dirname(os.path.realpath(this__file__)) + "\\..\\..")
        self.add_to_registry()
        sys.path.append(os.path.join(self.path(), "libs\\python"))
        sys.path.append(os.path.join(self.path(), "libs\\external\\python3.8"))

        self.tools_library_root_dir = self.path()
        self.tools_library_plugins_dir = os.path.join(self.tools_library_root_dir, "plugins")
        self.tools_library_programs_dir = os.path.join(self.tools_library_root_dir, "programs")

        self.enabled_program_names = []

        # install directories to add
        self.install_dirs = []

        # root install dir
        self.install_dirs.append(os.path.dirname(this__file__).replace("/", "\\"))

        # program install directories
        for program_name in os.listdir(self.tools_library_programs_dir):
            self.enabled_program_names.append(program_name)
            if(self.is_module_enabled(program_name, module_type="programs")):
                program_install_dir = os.path.join(self.tools_library_programs_dir, program_name, "scripts\\install")
                if(os.path.isdir(program_install_dir)):
                    self.install_dirs.append(program_install_dir)

        # plugin install directories
        for plugin_name in os.listdir(self.tools_library_plugins_dir):
            if(self.is_module_enabled(plugin_name, module_type="plugins")):
                plugin_install_dir = os.path.join(self.tools_library_plugins_dir, plugin_name, "scripts\\install")
                if(os.path.isdir(plugin_install_dir)):
                    self.install_dirs.append(plugin_install_dir)
                for program_name in self.enabled_program_names:
                    program_install_dir = os.path.join(self.tools_library_plugins_dir, plugin_name, "programs", program_name, "scripts\\install")
                    if(os.path.isdir(program_install_dir)):
                        self.install_dirs.append(program_install_dir)

        for i in self.install_dirs:
            print(i)


        # run all files
        for install_index in range(99):
            for install_dir in self.install_dirs:
                install_folder = os.path.join(install_dir, str(install_index))

                if(os.path.isdir(install_folder)):
                    for file in os.listdir(install_folder):
                        if(file.endswith(".py")):
                            file_path = os.path.join(install_folder, file)
                            print("[Tools Library][Install] Ran Install Script: \"" + file_path + "\"")
                            self.run_file(file_path)

        print("[Tools Library][Install] Complete!")

    def add_to_registry(self):
        """Add the path to the tools library to the registry"""
        try:
            reg_path = r"Software\\ToolsLibrary"
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, "path", 0, winreg.REG_SZ, self.root_folder)
            winreg.CloseKey(registry_key)
            print("Successfully created key!")
        except WindowsError:
            pass

    def path(self):
        """Returns the path to the tools library"""
        try:
            reg_path = r"Software\\ToolsLibrary"
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, "path")
            return value
        except WindowsError:
            return ""

    def get_json_property(self, file_path, value):
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

    def is_module_enabled(self, module_name, module_type="programs"):
        """Returns whether a module is enabled in the "config\\client_settings.json" file"""
        output = True
        client_settings_path = os.path.join(self.path(), "config\\client_settings.json")
        if(os.path.isfile(client_settings_path)):
            if(module_name != "python"):
                enabled = self.get_json_property(client_settings_path, module_type + "." + module_name + ".enabled")
                if(enabled == False):
                    output = False
        return output

    def run_file(self, file_path):
        """Run a single file"""
        path_ = file_path
        globals_ = globals()
        globals_["__file__"] = path_
        globals_["__package__"] = os.path.dirname(file_path)
        globals_["__name__"] = "__main__"
        exec(open(path_).read(), globals_)


install = Install()
