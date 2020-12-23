"""
Responsible for creating and storing instances of all maxscript modules
"""
import os
import pymxs


# class used to store all maxscript modules
class tools_library(object):
    def add_library(self, mxs_module):
        """Takes an input maxscript struct and adds it as a new module"""
        setattr(self, mxs_module.module_name, mxs_module)

    @staticmethod
    def create():
        pymxs.runtime.execute("tools_library = undefined")
        pymxs.runtime.tools_library = tools_library()


tools_library.create()


# loop over all files in the "python/startup/x" folders and run them
for i in range(99):

    modules_folder_ms = os.path.dirname(__file__) + "\\..\\" + str(i)
    modules_folder_ms = modules_folder_ms.replace("python", "maxscript")
    modules_folder_ms = modules_folder_ms.replace("startup", "modules")

    # run maxscript files
    if(os.path.isdir(modules_folder_ms)):
        for file in os.listdir(modules_folder_ms):
            print(os.path.join(modules_folder_ms, file))
            if(file.endswith(".ms")):
                file_path = os.path.join(modules_folder_ms, file)
                with open(file_path) as file:
                    file_lines = file.read()
                    pymxs.runtime.execute(file_lines)

        print("Maxscript Modules " + str(i) + " initialized.")