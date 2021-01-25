import os
import json

import asset_library
from asset_library.asset_types._asset import Asset
from asset_library.asset_types.texture import Texture


class Material(Asset):
    """Base class for AssetLibrary Material Assets"""
    def __init__(self, real_path):
        super().__init__(real_path)

        self.data = self.get_data_dict()
        self.textures = self.get_textures()

    @property
    def unreal_path(self):
        """Returns the unreal project relative path to this material"""
        return ""

    def import_to_unreal(self):
        """Import the current material to unreal"""
        print("TODO: Import Material")
        for tex in self.textures:
            tex.import_to_unreal()

    def get_data_dict(self):
        """Returns this .material (json) file as a python dict"""
        if(os.path.isfile(self.real_path)):
            with open(self.real_path, "r") as f:
                return json.load(f)
        return {}

    def get_textures(self):
        """Returns the asset library relative paths to all textures used by this material"""
        textures = []
        
        if("textures" in self.data):
            for param_identifier in self.data["textures"]:
                tex_path = self.data["textures"][param_identifier]

                # if there are no "\\"'s then we're referencing a texture relative to this material
                if("\\" not in tex_path):
                    tex_path = os.path.join(
                        os.path.dirname(self.real_path),
                        tex_path + ".tga"
                    )

                # else we're using a path relative to the asset library
                else:
                    tex_path = os.path.join(
                        asset_library.paths.root(),
                        tex_path + ".tga"
                    )

                tex = Texture(tex_path)
                tex.add_metadata("parameter_identifier", param_identifier)
                textures.append(tex)
        return textures
