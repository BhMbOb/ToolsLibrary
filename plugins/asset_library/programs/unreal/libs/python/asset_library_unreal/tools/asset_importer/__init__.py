import os
import sys
import glob
import datetime
import unreal

import tools_library

import asset_library
from asset_library import asset_manager
from asset_library.asset_types import texture, material, shader


class TAssetImporter(object):
    def __init__(self):
        self.target_module = 0  # 0 = All modules
        self.target_module_name = None

    def file_extension_from_prefix(self, prefix):
        prefix = prefix.lower()
        if(prefix == "t"):
            return "tga"
        elif(prefix == "m"):
            return "material"
        elif(prefix == "sm"):
            return "fbx"
        return ""

    def run_import(self):
        target_module_dirs = []

        if(self.target_module == 0):
            target_module_dirs = asset_library.paths.get_content_modules()
        else:
            target_module_dirs = asset_library.paths.get_content_module(self.target_module_name)

        # Import Textures
        for target_module_dir in target_module_dirs:
            target_module_textures_dir = os.path.join(target_module_dir, "textures")
            module_textures = glob.glob(target_module_textures_dir + "/**/*.tga", recursive=True)
            for i in  module_textures:
                is_valid = "." not in os.path.dirname(i)
                if(is_valid):
                    tex = texture.Texture(i)
                    tex.import_to_unreal()
            print(target_module_textures_dir)

        # Import Materials
        for target_module_dir in target_module_dirs:
            target_module_materials_dir = os.path.join(target_module_dir, "materials")
            module_textures = glob.glob(target_module_materials_dir + "/**/*.tga", recursive=True)
            for i in module_textures:
                is_valid = "." not in os.path.dirname(i)
                if(is_valid):
                    tex = texture.Texture(i)
                    tex.import_to_unreal()
            print(target_module_materials_dir)


importer = TAssetImporter()
importer.run_import()