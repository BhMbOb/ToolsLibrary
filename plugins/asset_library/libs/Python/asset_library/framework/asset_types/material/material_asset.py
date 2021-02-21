import os
import functools
import glob
import datetime
import json
import program_context

import tools_library
import tools_library.framework.asset_management.types.parameter as parameter
import tools_library.programs.unreal
import tools_library.utilities.json as json_utils
import tools_library.utilities.pathing as pathing_utils

import asset_library
from asset_library.framework.asset_types._asset import _Asset
from asset_library.framework.asset_types.texture import Texture
from asset_library.framework.asset_types.shader import Shader

if(program_context == "ue4"):
    import unreal
    import tools_library.ue4.materials.material_instance


class Material(_Asset):
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
    def unreal_relative_path(self):
        """Path to the .uasset relative to the unreal project"""
        output = "/AssetLibrary/" + self.asset_library_path
        output = output.split(".", 1)[0]
        output = output.replace("\\", "/")
        return output

    @property
    def unreal_path(self):
        """Absolute path to the current .uasset file"""
        output = os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\content", self.unreal_relative_path.replace("/AssetLibrary/", "") + ".uasset")
        output = output.replace("/", "\\")
        return output

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
        textures = self.textures
        for tex in self.textures:
            tex.import_to_unreal()
        
        # create unreal material
        mat_unreal_path = self.unreal_relative_path
        mi_name = os.path.basename(mat_unreal_path)
        mi_dir = os.path.dirname(mat_unreal_path)
        if(unreal.EditorAssetLibrary.does_asset_exist(mat_unreal_path)):
            new_mi = unreal.EditorAssetLibrary.find_asset_data(mat_unreal_path).get_asset()
        else:
            asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
            new_mi = asset_tools.create_asset(mi_name, mi_dir, unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
        target_shader = Shader("X:\\Shaders\\Surface_Object\\SHD_ABS_Surface_Object.shader")
        upath = target_shader.unreal_relative_path
        parent_mat = unreal.EditorAssetLibrary.find_asset_data(upath)
        unreal.MaterialEditingLibrary.set_material_instance_parent(new_mi, parent_mat.get_asset())
        for i in textures:
            param_name = ""
            if(i.texture_type in ("D", "DA")):
                param_name = "AlbedoMap"
            if(i.texture_type == "S"):
                param_name = "SurfaceMap"
            if(i.texture_type == "N"):
                param_name = "NormalMap"
            if(param_name != ""):
                tools_library.ue4.materials.material_instance.set_texture(new_mi, param_name, i.unreal_relative_path)

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