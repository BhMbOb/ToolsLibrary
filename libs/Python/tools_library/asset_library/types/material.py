import os
import sys
import json
import winreg

import tools_library
import tools_library.asset_library


class Material(object):
    def __init__(self):
        self.path = ""

    def load(self, relative_path):
        self.path = relative_path

    def abs_path(self):
        """Returns the absolute path to this .material file"""
        content_library = self.path.split(":")[0]
        asset_path = self.path.split(":")[1]
        return os.path.join(tools_library.asset_library.content_library.getPath(content_library),asset_path)

    def get_parameter(self, name, instance=None):
        """Returns a parameter if found - None if not

        name - name of the parameter
        instance - name of the instance to search from, default if not found
        """
        output = None
        with open (self.abs_path(), "r") as j:
            json_data = json.load(j)

            instance_name = "parameters:" + instance if instance is not None else "parameters"

            if(name in json_data[instance_name]):
                output = json_data[instance_name][name]

        if(type(output) is str):
            output = tools_library.finalizeString(output, file_context=self.path)

        return output

    def num_instances(self):
        """Returns the number of child instances this material has"""
        count = 0
        with open(self.abs_path(), "r") as j:
            json_data = json.load(j)
            for i in json_data:
                if((i == "parameters") or i.startswith("parameters:")):
                    count += 1
        return count
