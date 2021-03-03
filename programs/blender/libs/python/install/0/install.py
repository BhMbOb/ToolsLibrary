import os
import shutil
import winreg
import getpass


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
    blender_dir = "c:\\users\\" + getpass.getuser() + "\\Appdata\\Roaming\\Blender Foundation\\Blender"

    for i in os.listdir(blender_dir):
        blender_sub_dir = os.path.join(blender_dir, i)
        if(os.path.isdir(blender_sub_dir) and (i.replace(".", "").isdigit())):
            startup_folder = os.path.join(blender_sub_dir, "scripts\\startup")
            startup_script = os.path.join(tools_library_path, "programs\\blender\\libs\\python\\startup\\scripts\\startup.py")
            if(not os.path.isdir(startup_folder)):
                os.makedirs(startup_folder)
            shutil.copyfile(startup_script, os.path.join(startup_folder, "tools_library_startup.py"))
