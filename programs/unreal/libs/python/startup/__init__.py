import os

TOOLS_LIBRARY_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..\\..\\..\\..\\..\\"))
TOOLS_LIBRARY_PLUGINS_DIR = os.path.join(TOOLS_LIBRARY_ROOT_DIR, "plugins\\")

this__file__ = __file__

startup_dirs = []

# add base startup dir (in "/programs")
startup_dirs.append(os.path.dirname(__file__).replace("/", "\\"))

# add all plugin startup dirs (in "plugins/plugin_name/unreal/libs/python/startup")
for plugin_name in os.listdir(TOOLS_LIBRARY_PLUGINS_DIR):
    plugin_unreal_dir = os.path.join(TOOLS_LIBRARY_PLUGINS_DIR, plugin_name, "programs\\unreal\\")
    if(os.path.isdir(plugin_unreal_dir)):
        startup_dirs.append(os.path.join(plugin_unreal_dir, "libs\\python\\startup"))

# loop over all of the startup directories in order of their names (Ie, 0..1..2)
for startup_index in range(99):
    for startup_dir in startup_dirs:
        startup_folder = startup_dir + "/" + str(startup_index)

        # run python files
        if(os.path.isdir(startup_folder)):
            for file in os.listdir(startup_folder):
                if(file.endswith(".py")):
                    file_path = os.path.join(startup_folder, file)
                    __file__ = file_path
                    print("Tools Library: Ran Startup Script: \"" + file_path + "\".")
                    exec(open(file_path).read())
                    __file__ = this__file__

print("Tools Library: All startup scripts initialized.")
