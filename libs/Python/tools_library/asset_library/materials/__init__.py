import os
import sys
import json
import winreg

import tools_library
from tools_library import asset_library


def list_material_types():
    """Returns the names of all valid material types as defined in "config/materials/properties.json" """
    output = []

    materials_json = tools_library.getConfig("materials\\properties.json")

    with open(materials_json, "r") as j:
        json_data = json.load(j)

        for i in range(len(json_data["material_types"])):
            output.append(list(json_data["material_types"])[i])

    return output


def list_texture_types():
    """Returns the names of all valid texture types as defined in "config/materials/properties.json" """
    output = []

    materials_json = tools_library.getConfig("materials\\properties.json")

    with open(materials_json, "r") as j:
        json_data = json.load(j)

        for i in range(len(json_data["texture_types"])):
            output.append(list(json_data["texture_types"])[i])

    return output


class Texture(object):
    """Class containing data for a material based texture"""
    def __init__(self, path):

        # if the asset_path is formatted "asset_library:path/to/the/asset.asset" then extract, else use "Common" by default
        self.asset_library = path.split(":")[0] if (len(path.split(":")) > 1) else "Common"

        # if the asset_path is formatted "asset_library:path/to/the/asset.asset" then extract, else use asset_path
        self.base_path = path.split(":")[1] if (len(path.split(":")) > 1) else path

        #self.path = path

    def type(self):
        """Returns the material texture type if valid - None if not"""
        output = None

        texture_type = self.texname().split("_")[-1].lower().replace(".tga", "").upper()

        materials_json = tools_library.getConfig("materials\\properties.json")

        with open(materials_json, "r") as j:
            json_data = json.load(j)

            if(texture_type in json_data["texture_types"]):
                output = texture_type

        return output

    def texname(self):
        return os.path.basename(self.path())

    def path(self, relative=True):
        """"""
        output = self.asset_library + ":" + self.base_path

        if(not relative):
            output = asset_library.actualPath(output)

        return output

    def variant(self):
        """Returns the variant of a parent instance this texture is targeted towards"""
        split_data = self.texname().split("_")
        abc_array = list("abcdefghijklmnopqrstuvwxyz")

        # if the variant is an "a, b, c" based type..
        if(split_data[-2] in abc_array):
            return split_data[-2]
        # if there is a valid instance number and an undefined variable after..
        elif(split_data[-3].isdigit()):
            return split_data[-2]
        else:
            return None

    def instance(self):
        """Returns the instance of a parent texture this texture is targeted towards"""
        split_data = self.path().split(":")[-1].split("_")

        possible_texture_instance = split_data[-2] if (self.texname() is None) else split_data[-3]

        texture_type = split_data[-1]
        texture_instance = split_data[-2] if split_data[-2].isdigit() else split_data[-3] if split_data[-3].isdigit() else None

        if(texture_instance is not None):
            texture_instance = int(texture_instance)

        return texture_instance

    def is_valid(self):
        """Returns whether a material texture is valid"""
        output = False

        if(
            # path must exist
            os.path.exists(self.path(relative=False)) and
            #os.path.exists(self.path) and
            # must begin with "T_"
            self.texname().startswith("T_") and
            # must be a TGA
            self.path().lower().endswith(".tga") and
            # must have a valid type (Ie, _D)
            self.type() is not None
        ):
            output = True

        return output


class Material(object):
    """Class containing info on a material"""
    def __init__(self, material_name):

        # if material_name is formatted "asset_library_name:material_name" then extract, else use "Common" by default"
        self.asset_library = material_name.split(":")[0] if (len(material_name.split(":")) > 1) else "Common"

        # if material_name is formatted "asset_library_name:material_name" then extract, else use material_name
        self.base_name = material_name.split(":")[1] if (len(material_name.split(":")) > 1) else material_name

    def _get_asset_file_path(self, relative=True):
        """Returns the path to the material.asset file if it exists"""
        output = ""

        asset_file_path = os.path.join(
            self.path(),
            "M_" + self.base_name + ".asset"
        )

        if(os.path.isfile(asset_library.actualPath(asset_file_path))):
            output = asset_file_path
            if(not relative):
                output = asset_library.actualPath(output)

        return output

    def path(self, relative=True):
        """Returns the absolute path for this material folder"""
        output = os.path.join(
            self.asset_library + ":Materials",
            self.base_name
        )

        if(not relative):
            output = asset_library.actualPath(output)

        return output

    def _get_source_sbs_path(self, is_sbsar=False):
        """Attempts to find a source sbs file for this material"""
        output = ""

        source_sbs_path = os.path.join(self.path(), ".source", self.base_name + ".sbs")
        if(is_sbsar):
            source_sbs_path += "ar"

        if(os.path.isfile(asset_library.actualPath(source_sbs_path))):
            output = source_sbs_path

        return output

    def _get_all_textures(self):
        """Returns all valid material textures from a given material name"""
        output = []

        target_asset_library_path = os.path.join(
            tools_library.asset_library.getAssetLibrary(self.asset_library),
            "Materials"
        )

        material_folder = os.path.join(target_asset_library_path, self.base_name)

        if(os.path.exists(material_folder)):
            for i in os.listdir(material_folder):
                if(self.base_name in i):
                    tex = Texture(self.asset_library + ":Materials\\" + self.base_name + "\\" + i)
                    if(tex.is_valid()):
                        output.append(i)

        return output

    def _get_instance_texture(self, material_instance, material_variant, texture_type):
        """Returns the final target texture of a specific type for a material

        material_instance   --  instance id, if instance isn't found will default to the base instance
        material_variant    --  variant id, if variant isn't found will default to the base variant
        texture_type        --  type of texture to search for as defined in "config/materials/properties.json" (Ie "_DA")
        """
        output = None

        possible_textures = self._get_all_textures()

        for t in possible_textures:
            tex = Texture(t)

            # if we've found a matching texture type..
            if(tex.type() == texture_type):

                # complete match
                if((material_variant == tex.variant()) and (material_instance == tex.instance())):
                    output = t

                # no instance or variant
                if((material_variant is None) and (material_instance == None) and (tex.instance() == None) and (tex.variant() == None)):
                    output = t

                # instance but no variant
                elif((material_instance == tex.instance()) and (material_variant is None) and (tex.variant() is None)):
                    output = t

                #  fallback - instance but no variant
                elif(material_variant is not None):
                    fallback = self._get_instance_texture(material_instance, None, texture_type)
                    if(fallback is not None):
                        output = fallback

                # fallback - no instance and no variant
                elif(material_instance is not None):
                    fallback = self._get_instance_texture(None, None, texture_type)
                    if(fallback is not None):
                        output = fallback

        return output

    def _get_instance_textures(self, instance=1, variant="a"):
        """Returns all textures for a given material from the name, instance and variant"""
        output = []

        possible_textures = self._get_all_textures()

        for t in possible_textures:
            tex = Texture(os.path.join(self.path(), t))

            if((tex.instance() in [instance, None]) and (tex.variant() in [variant, None])):

                found_texture = self._get_instance_texture(tex.instance(), tex.variant(), tex.type())
                if((found_texture is not None) and (found_texture not in output)):
                    output.append(found_texture)

        return output

    def _get_type(self):
        """Attempts to find a matching material type from the final textures
        TODO:
        """
        types = list_material_types()


def list_materials(target_asset_library):
    """Lists all valid material names found in a target asset library"""
    output = []

    asset_library_path = asset_library.getAssetLibrary(target_asset_library)
    material_dirs = os.listdir(os.path.join(asset_library_path, "Materials"))

    for i in material_dirs:
        # we can be sure it's a folder if there's no "."
        if("." not in i):
            mat = Material(i)
            # check for an "01_a" variant as this falls back to check for none
            # if either return true then it is valid
            if(mat._get_instance_textures(1, "a") is not []):
                output.append(i)

    return output
