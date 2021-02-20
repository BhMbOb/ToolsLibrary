import os
import functools
import glob
import datetime
import json

import tools_library
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
        """Shelves directory where all .shader files are stored"""
        return os.path.join(asset_library.paths.root(), "shelves\\source\\shaders")

    @staticmethod
    def get_shader_paths(ignore_abstract=True):
        """Returns the paths to all .shader files"""
        output = []
        all_shaders = [y for x in os.walk(ShaderManager.shaders_dir()) for y in glob.glob(os.path.join(x[0], '*.shader'))]
        if(ignore_abstract):
            for i in all_shaders:
                if(json_utils.get_property(i, "properties.abstract") != True):
                    output.append(i)
        else:
            output = all_shaders
        return output

    @staticmethod
    def get_shader_paths_uproject(ignore_abstract=False):
        """Returns the .uasset path to all shaders in the unreal project"""
        output = []
        all_shaders = []
        for i in glob.glob(asset_library.paths.root() + "\\**\\*.uasset", recursive=True):
            if(os.path.basename(i).lower().startswith("shd_")):
                if(not (ignore_abstract and "shd_abs" in i.lower())):
                    all_shaders.append(i)
        return all_shaders

    @staticmethod
    def get_shader_path(shader_name):
        """returns the path to a shader given an input name"""
        shader_paths = ShaderManager.get_shader_paths(ignore_abstract=False)
        for i in shader_paths:
            shader_name = os.path.basename(i).split(".")[0].lower()
            if(shader_name.lower() == shader_name):
                return i
        return ""

    @staticmethod
    def get_shader_names(ignore_abstract=False):
        """Returns the names of all .shader files"""
        return [(os.path.basename(i).split(".")[0]) for i in ShaderManager.get_shader_paths()]

    @staticmethod
    def get_property(shader_name, property_):
        """Recursively searches for a property in a shader and its parents"""
        output = ""
        shd = ShaderManager.get_shader_path(shader_name)
        if(os.path.isfile(shd)):
            prop = json_utils.get_property(shd, property_)
            if(prop == ""):
                parent_shader_name = json_utils.get_property(shd, "properties.parent")
                parent_shader_path = ShaderManager.get_shader_path(parent_shader_name)
                if(os.path.isfile(parent_shader_path)):
                    output = ShaderManager.get_property(
                        parent_shader_name,
                        property_
                    )
            else:
                output = prop
        return output


class Shader(Asset):
    def __init__(self, shader_path):
        super().__init__(shader_path)

    def import_to_unreal(self):
        pass

    def get_property(self, property_):
        return ShaderManager.get_property(self.name, property_)

    @property
    @functools.lru_cache()
    def unreal_path(self):
        return ShaderManager.get_property(self.name, "ue4.path")

    @property
    @functools.lru_cache()
    def unreal_path(self):
        unreal_shader_paths = ShaderManager.get_shader_paths_uproject()
        for i in unreal_shader_paths:
            i_name = os.path.basename(i).split(".")[0].lower()
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
