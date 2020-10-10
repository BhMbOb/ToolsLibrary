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
    """Loop over all startup scripts and run in order"""
    startup_scripts_dir = getProjectRoot() + "\\programs\\painter\\libs\\python\\startup\\"

    for i in range(99):
        startup_scripts_current_dir = startup_scripts_dir + str(i)

        if(os.path.isdir(startup_scripts_current_dir)):
            for file in os.listdir(startup_scripts_current_dir):
                script_path = os.path.join(startup_scripts_current_dir, file)
                exec(open(script_path).read())


def start_plugin():
    reg_path = r"Software\\ToolsLibrary"
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
    tools_library_project_root, regtype = winreg.QueryValueEx(registry_key, "path")

    sys.path.append(os.path.join(tools_library_project_root, "libs\\python"))
    sys.path.append(os.path.join(tools_library_project_root, "programs\\painter\\libs"))
    runStartupScripts()


def close_plugin():
    pass


if __name__ == "__main__":
    start_plugin()
