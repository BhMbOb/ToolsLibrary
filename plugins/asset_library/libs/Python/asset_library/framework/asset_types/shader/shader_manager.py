import os
import functools
import glob
import json

import tools_library.framework.asset_management.types.parameter as parameter
import tools_library.utilities.json as json_utils
import tools_library.utilities.pathing as pathing_utils

import asset_library


class __ShaderManager(object):
    __instance__ = None

    @property
    @functools.lru_cache()
    def shaders_dir(self):
        """The absolute directory where all .shader files are stored"""
        return os.path.join(asset_library.paths.root(), "shaders")

    @property
    @functools.lru_cache()
    def shaders_unreal_dir(self):
        """The absolute directory where all Asset Library shaders are stored in the unreal plugin (as .uasset)"""
        return os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\content\\shaders")

    def get_shader_paths(self, ignore_abstract=False):
        """Return the path to all .shader files"""
        output = []
        for i in glob.glob(self.shaders_dir + "/**/*.shader"):
            shader_name = os.path.basename(i)
            if(not (ignore_abstract and shader_name.startswith("SHD_ABS"))):
                output.append(i.lower())
        return output

    def get_unreal_shader_paths(self, ignore_abstract=False):
        """Return the path to the .uasset files matching to all .shader files"""
        output = []
        for i in glob.glob(self.shaders_unreal_dir + "/**/SHD_*.uasset"):
            if(not ("SHD_ABS" in i and ignore_abstract)):
                output.append(i.lower())
        return output

    def find_shader_path(self, shader_name):
        """Attempt to find the path to a .shader from an input shader name"""
        shader_name = shader_name.lower()
        shader_paths = self.get_shader_paths()
        for i in shader_paths:
            if(pathing_utils.get_filename_only(i) == shader_name):
                return i
        return ""

    def get_shader_names(self):
        """Return the name of all .shader files"""
        return [pathing_utils.get_filename_only(i) for i in self.get_shader_paths()]

    def get_shader_hierachy_names(self, shader_name):
        """Returns the path to all .shader files referenced by the input shader"""
        output = [shader_name]
        current = shader_name
        current_path = self.find_shader_path(current)
        while current not in ["", None]:
            if(os.path.isfile(current_path)):
                current = json_utils.get_property(current_path, "properties.parent")
                current_path = self.find_shader_path(current)
                if(os.path.isfile(current_path)):
                    output.append(current)
        return output

    def get_parameter_dict(self, shader, param_name):
        """Recursively build a parameter in the current shader and its parents"""
        param_data_dict = {}
        param_name = param_name.lower()
        for i in self.get_shader_hierachy_names(shader.name):
            path = self.find_shader_path(i)
            with open(path, "r") as f:
                json_data = json.load(f)
            if("parameters" in json_data):
                for group in json_data["parameters"]:
                    for param in json_data["parameters"][group]:
                        if(param.lower() == param_name):
                            current_data_dict = json_data["parameters"][group][param]
                            current_data_dict["group"] = group
                            current_data_dict["name"] = param_name
                            current_data_dict.update(param_data_dict)
                            param_data_dict = current_data_dict
        return param_data_dict

    def get_parameter(self, shader, param_name):
        param_data_dict = self.get_parameter_dict(shader, param_name)
        return parameter.Parameter.from_dict(param_data_dict)



if(__ShaderManager.__instance__ is None):
    __ShaderManager.__instance__ = __ShaderManager()
ShaderManager = __ShaderManager.__instance__