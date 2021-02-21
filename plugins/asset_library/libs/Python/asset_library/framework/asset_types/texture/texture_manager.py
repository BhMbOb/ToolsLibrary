import os
import functools
import json
import glob

import tools_library.utilities.pathing
import tools_library.utilities.json as json_utils

import asset_library


class __TextureManager(object):
    __instance__ = None

    def get_texture_types_map(self):
        """"""
        textures_config_path = os.path.join(asset_library.paths.root(), "content\\core\\textures\\.config\\texture_types.json")
        with open(textures_config_path, "r") as f:
            return json.load(f)
        return json_texture_types

    def get_unreal_compression_method(self, method_string):
        """Takes an Unreal Compression method string and returns the matchingunreal object
        Ie, "TC_MASKS" -> unreal.TextureCompressionSettings.TC_NORMALMAP"""
        if(tools_library.program_context() == "ue4"):
            import unreal
            return eval("unreal.TextureCompressionSettings." + method_string)
        return None

    def import_to_unreal(self):
        """Import all of the textures to unreal"""
        from asset_library.framework.asset_types.texture import Texture
        target_module_dirs = asset_library.paths.get_content_modules()
        for target_module_dir in target_module_dirs:
            target_module_textures_dir = os.path.join(target_module_dir, "textures")
            module_textures = glob.glob(target_module_textures_dir + "/**/*.tga", recursive=True)
            for i in module_textures:
                is_valid = "." not in os.path.dirname(i)
                if(is_valid):
                    tex = Texture(i)
                    tex.import_to_unreal()


if(__TextureManager.__instance__ is None):
    __TextureManager.__instance__ = __TextureManager()
TextureManager = __TextureManager.__instance__