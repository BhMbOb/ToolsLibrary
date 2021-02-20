"""
Add/copy all the relevent files to the current unreal project
"""
import os
import shutil
import winreg
import json


def getProjectRoot():
    """Root to the tools library project"""
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


def getUnrealProjectRoot():
    """Root to the unreal project"""
    active_project_config_path = os.path.join(getProjectRoot(), "config\\client_settings.json")
    with open(active_project_config_path) as j:
        json_data = json.load(j)
        return json_data["programs"]["ue4"]["project_dir"]


tools_library_path = getProjectRoot()
unreal_project_root = getUnrealProjectRoot()


# copy the "programs/unreal/libs/python/install/scripts/startup.py/" to the unreal project
startup_script = os.path.join(tools_library_path, "programs\\ue4\\libs\\python\\install\\scripts\\startup.py")
target_path = os.path.join(unreal_project_root, "content\\python\\startup\\tools_library\\startup.py")
if(not os.path.isdir(os.path.dirname(target_path))):
    os.makedirs(os.path.dirname(target_path))
shutil.copyfile(startup_script, target_path)


# add the startup script line to the "DefaultEngine.ini"
default_engine_ini_path = os.path.join(unreal_project_root, "Config\\DefaultEngine.ini")
python_plugin_start_line_string = "[/Script/PythonScriptPlugin.PythonScriptPluginSettings]"
startup_script_string = "+StartupScripts=startup/tools_library/startup.py"

with open(default_engine_ini_path) as file:
    ini_file_data = file.read()

with open(default_engine_ini_path, "w") as file:
    if(python_plugin_start_line_string in ini_file_data):
        if(startup_script_string not in ini_file_data):
            ini_file_data = ini_file_data.replace(
                python_plugin_start_line_string,
                python_plugin_start_line_string + "\n" + startup_script_string
            )
    else:
        ini_file_data += str(
            "\n" + python_plugin_start_line_string + "\n" + startup_script_string
        )
    file.write(ini_file_data)
