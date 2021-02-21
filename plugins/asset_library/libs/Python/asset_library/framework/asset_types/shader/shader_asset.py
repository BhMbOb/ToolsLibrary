import os
import functools

import tools_library.utilities.json as json_utils
import tools_library.utilities.pathing as pathing_utils

from asset_library.framework.asset_types._asset import _Asset
from asset_library.framework.asset_types.shader.shader_manager import ShaderManager


class Shader(_Asset):
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

shd = Shader("X:\\Shaders\\Surface_Standard\\SHD_Surface_Standard.shader")
print(shd.get_parameter("AlbedoMap"))