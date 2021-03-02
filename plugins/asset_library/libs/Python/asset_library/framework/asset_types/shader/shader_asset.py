import os
import functools

import tools_library.utilities.json as json_utils
import tools_library.utilities.pathing as pathing_utils
import tools_library.decorators

from asset_library.framework.asset_types._asset import _Asset
from asset_library.framework.asset_types.shader.shader_manager import ShaderManager


class Shader(_Asset):
    def __init__(self, shader_path):
        super().__init__(shader_path)

    @tools_library.decorators.ue4_method
    def import_to_unreal(self):
        """Shaders cannot be imported to unreal - they are considered a sibling asset type"""
        pass

    @property
    @functools.lru_cache()
    def unreal_path(self):
        """Absolute path to the .uasset file for this shader
        :return <str:path> Absolute file path - Ie, "x:/project/unreal/content/shaders/the_shader.uasset"
        """
        unreal_shader_paths = ShaderManager.get_unreal_shader_paths()
        for i in unreal_shader_paths:
            i_name = pathing_utils.get_filename_only(i)
            if(i_name == self.name):
                return i
        return ""

    @property
    @functools.lru_cache()
    def unreal_relative_path(self):
        """Unreal project relative path to the asset
        :return <str:path> Unreal relative file path - Ie, "/AssetLibrary/shaders/the_shader"
        """
        output = "/AssetLibrary/" + self.asset_library_path
        output = output.split(".", 1)[0]
        output = output.replace("\\", "/")
        return output
        
    @property
    @functools.lru_cache()
    def parent(self):
        """Absolute path to the parent .shader for this shader
        :return <str:path> Absolute file path - Ie, "x:/shaders/parent_shader.shader"
        """
        return json_utils.get_property(self.real_path, "properties.parent")

    def get_parameter(self, param_name):
        """Get a parameter object by name for this shader
        :return <Parameter:param> The parameter reference - None if not found
        """
        return ShaderManager.get_parameter(self, param_name)
