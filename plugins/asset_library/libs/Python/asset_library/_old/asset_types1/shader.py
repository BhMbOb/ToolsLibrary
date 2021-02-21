import os
import functools
import glob
import datetime
import json

import tools_library
import tools_library.framework.asset_management.types.parameter as parameter
import tools_library.programs.unreal
import tools_library.utilities.json as json_utils
import tools_library.utilities.pathing as pathing_utils

import asset_library

from asset_library.asset_types._asset import Asset


class ShaderManager(object):
    def __init__(self):
        pass

    @staticmethod
    def shaders_dir():
        """Directory where all .shader files are stored in the asset library"""
        return os.path.join(asset_library.paths.root(), "shaders")

    @staticmethod
    def shaders_unreal_dir():
        """Directory where all .uasset matching .shader files are stored in the asset library ue4 plugin"""
        return os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\content\\shaders")

    @staticmethod
    def get_shader_paths(ignore_abstract=False):
        """Return the path to all .shader files"""
        output = []
        for i in glob.glob(ShaderManager.shaders_dir() + "/**/*.shader"):
            shader_name = os.path.basename(i)
            if(not (ignore_abstract and shader_name.startswith("SHD_ABS"))):
                output.append(i.lower())
        return output

    @staticmethod
    def get_unreal_shader_paths(ignore_abstract=False):
        """Return the path to the .uasset files matching to all .shader files"""
        output = []
        for i in glob.glob(ShaderManager.shaders_unreal_dir() + "/**/SHD_*.uasset"):
            if(not ("SHD_ABS" in i and ignore_abstract)):
                output.append(i.lower())
        return output

    @staticmethod
    def find_shader_path(shader_name):
        """Attempt to find the path to a .shader from an input shader name"""
        shader_name = shader_name.lower()
        shader_paths = ShaderManager.get_shader_paths()
        for i in shader_paths:
            if(pathing_utils.get_filename_only(i) == shader_name):
                return i
        return ""

    @staticmethod
    def get_shader_names():
        """Return the name of all .shader files"""
        return [pathing_utils.get_filename_only(i) for i in ShaderManager.get_shader_paths()]

    @staticmethod
    def get_shader_hierachy_names(shader_name):
        """Returns the path to all .shader files referenced by the input shader"""
        output = [shader_name]
        current = shader_name
        current_path = ShaderManager.find_shader_path(current)
        while current not in ["", None]:
            if(os.path.isfile(current_path)):
                current = json_utils.get_property(current_path, "properties.parent")
                current_path = ShaderManager.find_shader_path(current)
                if(os.path.isfile(current_path)):
                    output.append(current)
        return output

    @staticmethod
    def get_parameter_dict(shader, param_name):
        """Recursively build a parameter in the current shader and its parents"""
        param_data_dict = {}
        param_name = param_name.lower()
        for i in ShaderManager.get_shader_hierachy_names(shader.name):
            path = ShaderManager.find_shader_path(i)
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

    @staticmethod
    def get_parameter(shader, param_name):
        param_data_dict = ShaderManager.get_parameter_dict(shader, param_name)
        return parameter.Parameter.from_dict(param_data_dict)


class Shader(Asset):
    def __init__(self, shader_path):
        super().__init__(shader_path)

    def import_to_unreal(self):
        pass

    @property
    @functools.lru_cache()
    def unreal_path(self):
        unreal_shader_paths = ShaderManager.get_unreal_shader_paths()
        for i in unreal_shader_paths:
            i_name = pathing_utils.get_filename_only(i)
            if(i_name == self.name):
                return i
        return ""

    @property
    @functools.lru_cache()
    def unreal_relative_path(self):
        output = "/AssetLibrary/" + self.asset_library_path
        output = output.split(".", 1)[0]
        output = output.replace("\\", "/")
        return output
        
    @property
    @functools.lru_cache()
    def parent(self):
        """Returns the path to the parent shader for this .shader"""
        return json_utils.get_property(self.real_path, "properties.parent")

    def get_parameter(self, param_name):
        return ShaderManager.get_parameter(self, param_name)

