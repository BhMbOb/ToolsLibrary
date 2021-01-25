import os
import sys
import winreg

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

# base libs
sys.path.append(os.path.join(path(), "libs\\Python"))
sys.path.append(os.path.join(path(), "libs\\External\\Python3.7"))

# add all plugin dirs to path
import tools_library

# global value stores the current program that this python instance is ran within
# (Ie, "unreal", "max", "python")
tools_library.PROGRAM_CONTEXT = __program_context__
program_context = tools_library.programContext()

sys.path.append(os.path.join(tools_library.path(), "programs", program_context, "libs\\python"))

for plugin_dir in tools_library.pluginDirs():
    sys.path.append(
        os.path.join(
            tools_library.path(), 
            "plugins", 
            os.path.basename(plugin_dir), 
            "libs\\python"
        )
    )

    sys.path.append(
        os.path.join(
            tools_library.path(), 
            "plugins", 
            os.path.basename(plugin_dir), 
            "programs", 
            program_context, 
            "libs\\python"
        )
    )

# loop / run all of the startup scripts in the order:
# Python -> Plugins -> Core Program -> Plugin Program
for i in range(99):

    target_dirs = []

    # Core Python
    base_python_startup_dir = os.path.dirname(__file__) + "/" + str(i)
    if(os.path.isdir(base_python_startup_dir)):
        target_dirs.append(base_python_startup_dir)

    # Plugins
    for plugin_name in tools_library.pluginDirs():
        plugin_python_startup_dir = os.path.join(tools_library.path(), "plugins", plugin_name, "libs\\python\\startup", str(i))
        if(os.path.isdir(plugin_python_startup_dir)):
            target_dirs.append(plugin_python_startup_dir)

    # Programs
    program_python_startup_dir = os.path.join(tools_library.path(), "programs", program_context, "libs\\python\\startup", str(i))
    if(os.path.isdir(program_python_startup_dir)):
        target_dirs.append(program_python_startup_dir)

    # Plugin Programs
    for plugin_name in tools_library.pluginDirs():
        plugin_program_dir = os.path.join(tools_library.path(), "plugins", plugin_name, "programs", program_context, "libs\\python\\startup", str(i))
        if(os.path.isdir(plugin_program_dir)):
            target_dirs.append(plugin_program_dir)

    for startup_dir in target_dirs:
        for file in os.listdir(startup_dir):
            if(file.endswith(".py")):
                tools_library.run_file(os.path.join(startup_dir, file))
                print("[Tools Library][Startup] Ran script -" + os.path.join(startup_dir, file))
        
        # additional startup/libs for maxscript when in 3DS Max
        dir_as_maxscript = startup_dir.replace("\\python", "\\maxscript")
        if(os.path.isdir(dir_as_maxscript)):
            for file in os.listdir(dir_as_maxscript):
                if(file.endswith(".ms")):
                    import pymxs
                    file_path = os.path.join(dir_as_maxscript, file)
                    with open(file_path) as file:
                        file_lines = file.read()
                    pymxs.runtime.execute(file_lines)
                    print("[Tools Library][Startup] Ran maxscript - " + file_path)
