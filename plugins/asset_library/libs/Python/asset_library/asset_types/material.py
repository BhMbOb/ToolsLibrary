import os
import json

import tools_library.utilities.json as json_utils

import asset_library
from asset_library.asset_types._asset import Asset
from asset_library.asset_types.texture import Texture


class MaterialManager(object):
    @staticmethod
    def get_materials(module_names=[], prefixes=[]):
        """Returns a list of materials fitting certain criteria"""
        output = []

        if(type(module_names) is not tuple):
            module_names = (module_names)

        if(type(prefixes) is not tuple):
            prefixes = (prefixes)

        material_dirs = []

        for module in module_names:
            module_materials_dir = os.path.join(asset_library.paths.root(), "content", module, "materials")
            if(os.path.isdir(module_materials_dir)):
                for material_name in os.listdir(module_materials_dir):
                    material_dir = os.path.join(module_materials_dir, material_name)
                    if(os.path.isdir(material_dir) and (material_name.lower().startswith(prefixes))):
                        material_dirs.append(material_dir)

        for material_dir in material_dirs:
            material_dirname = os.path.basename(material_dir)
            for i in os.listdir(material_dir):
                if(i.startswith("M_" + material_dirname) and (i.endswith(".material"))):
                    output.append(Material(os.path.join(material_dir, i)))

        return output


class Material(Asset):
    """Base class for AssetLibrary Material Assets"""
    def __init__(self, real_path):
        super().__init__(real_path)

        self.data = self.get_data_dict()
        self.textures = self.get_textures()

    @property
    def source_sbs(self):
        """Returns the path to the source .sbs for this material"""
        mat_name = json_utils.get_property(self.path, "metadata.name")
        sbs_path = os.path.join(os.path.dirname(self.path), ".source", mat_name + ".sbs")
        return sbs_path

    @property
    def outer_name(self):
        """Outer name is the name of the parent material - with instance/variant identifiers removed"""
        output = json_utils.get_property(self.path, "metadata.name")
        return output

    @property
    def instance(self):
        """Gets the instance part of the material name (Ie, moss_01_a -> 01)"""
        output = json_utils.get_property(self.path, "metadata.instance")
        return output

    @property
    def variant(self):
        """Gets the variant part of the material name (Ie, moss_01_a -> a)"""
        output = json_utils.get_property(self.path, "metadata.variant")
        return output

    @property
    def unreal_path(self):
        """Returns the unreal project relative path to this material"""
        return ""

    @property
    def name(self):
        output = ""
        name = self.outer_name
        instance = self.instance
        variant = self.variant
        output = name
        output += ("_" * int(len(instance) > 0)) + instance
        output += ("_" * int(len(variant)> 0)) + variant
        return output

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
