import os
import glob

import asset_library.paths


class Uasset(object):
    def __init__(self, real_path):
        self.real_path = real_path.lower()

        self._unreal_plugin_content_dir = os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\content")
        self._asset_library_content_dir = os.path.join(asset_library.paths.root(), "content")

    @property
    def content_browser_path(self):
        """Path to the .uasset relative to the unreal content browser 
        (Ie, "/AssetLibrary/Common/Materials/Texture/File.png")"""
        plugin_root_dir = os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\content")
        output = "\\assetlibrary" + self.real_path.replace(self._unreal_plugin_content_dir, "")
        output = output.replace(".uasset", "")
        return output

    @property
    def source_file_type(self):
        prefix = os.path.basename(self.real_path).split(".")[0].lower().split("_")[0]
        if(prefix == "t"):
            return "tga"
        elif(prefix == "m"):
            return "material"
        elif(prefix == "sm"):
            return "fbx"
        return ""

    @property
    def source_file(self):
        file_path_assetlibrary = self.real_path.replace(self._unreal_plugin_content_dir, self._asset_library_content_dir)
        output = file_path_assetlibrary.replace(".uasset", "." + self.source_file_type)
        return output