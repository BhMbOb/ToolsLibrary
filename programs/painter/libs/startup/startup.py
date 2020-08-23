import os
import sys
import shutil
import winreg


def getProjectRoot():
    try:
        reg_path = r"Software\\ToolsLibrary"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "path")
        return value
    except WindowsError:
        return ""


def runStartupScripts():
    """Loop over all sub-startup folders and run all scripts contained"""
    startup_dir = os.path.join(getProjectRoot(), "programs\\painter\\libs\\startup\\")

    for startup_dir_name in (os.listdir(startup_dir)):
        actual_dir = os.path.join(startup_dir, startup_dir_name)

        if((os.path.isdir(actual_dir)) and (startup_dir_name.startswith("startup_"))):

            for target_startup_script_name in os.listdir(actual_dir):

                if(target_startup_script_name.endswith(".py")): 
                    actual_script_path = os.path.join(actual_dir, target_startup_script_name)
                    exec("from startup." + startup_dir_name + " import " + target_startup_script_name[0:-3])


runStartupScripts()
print("Tools Library: Startup Scripts Initialized")
