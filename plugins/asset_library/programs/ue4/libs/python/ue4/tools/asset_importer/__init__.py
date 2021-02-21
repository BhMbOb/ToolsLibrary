import os
import sys
import glob
import datetime
import json
import imp
import unreal

import tools_library

import asset_library
from asset_library.framework.asset_types import texture, material, shader

imp.reload(material)
imp.reload(texture)
imp.reload(shader)


class TAssetImporter(object):
    def __init__(self):
        self.target_module = 0  # 0 = All modules
        self.target_module_name = None

    def run_import(self):
        target_module_dirs = []

        if(self.target_module == 0):
            target_module_dirs = asset_library.paths.get_content_modules()
        else:
            target_module_dirs = asset_library.paths.get_content_module(self.target_module_name)

        material.MaterialManager.import_to_unreal()
        #texture.TextureManager.import_to_unreal()


importer = TAssetImporter()
importer.run_import()

shader.ShaderManager.get_shader_paths_uproject()