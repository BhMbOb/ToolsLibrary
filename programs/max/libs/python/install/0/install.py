import os
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


tools_library_path = getProjectRoot()
if(os.path.exists(tools_library_path)):
    startup_folder = "C:\\Users\\bhmbo\\AppData\\Local\\Autodesk\\3dsMax\\2021 - 64bit\\ENU\\scripts\\startup"
    startup_script = os.path.join(tools_library_path, "programs\\max\\libs\\maxscript\\startup\\startup.ms")
    if(not os.path.isdir(startup_folder)):
        os.mkdir(startup_folder)
    shutil.copyfile(startup_script, os.path.join(startup_folder, "startup.ms"))
