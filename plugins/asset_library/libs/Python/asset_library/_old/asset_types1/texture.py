import os
import stat
import datetime
import json
import glob

try:
    import unreal
except:
    pass

import tools_library
import tools_library.programs.unreal
import tools_library.utilities.json as json_utils
import tools_library.utilities.pathing as pathing_utils

import asset_library

from asset_library.asset_types._asset import Asset


class TextureManager(object):
    def __init__(self):
        pass

    @staticmethod
    def get_texture_types_map():
        """"""
        textures_config_path = os.path.join(asset_library.paths.root(), "content\\core\\textures\\.config\\texture_types.json")
        with open(textures_config_path, "r") as f:
            return json.load(f)
        return json_texture_types

    @staticmethod
    def get_unreal_compression_method(method_string):
        """Takes an Unreal Compression method string and returns the matchingunreal object
        Ie, "TC_MASKS" -> unreal.TextureCompressionSettings.TC_NORMALMAP"""
        if(tools_library.program_context() == "ue4"):
            import unreal
            return eval("unreal.TextureCompressionSettings." + method_string)
        return None

    @staticmethod
    def import_to_unreal():
        """Import all of the textures to unreal"""
        target_module_dirs = asset_library.paths.get_content_modules()
        for target_module_dir in target_module_dirs:
            target_module_textures_dir = os.path.join(target_module_dir, "textures")
            module_textures = glob.glob(target_module_textures_dir + "/**/*.tga", recursive=True)
            for i in module_textures:
                is_valid = "." not in os.path.dirname(i)
                if(is_valid):
                    tex = Texture(i)
                    tex.import_to_unreal()


class Texture(Asset):
    """Base class for all AssetLibrary Texture Assets"""
    @property
    def unreal_relative_path(self):
        """Path to the .uasset relative to the unreal project"""
        output = "/AssetLibrary/" + self.asset_library_path
        output = output.split(".", 1)[0]
        output = output.replace("\\", "/")
        return output

    @property
    def texture_type(self):
        """Returns the textures type from its suffix - if the suffx is invalid we return None"""
        suffix = self.name.split("_")[-1].upper()
        json_texture_types = TextureManager.get_texture_types_map()

        if(suffix in json_texture_types):
            return suffix
        return None

    @property
    def texture_type_identifier(self):
        """Friendly/descriptive name for the current texture's texture type"""
        texture_type = self.texture_type
        if(texture_type is not None):
            json_texture_types = TextureManager.get_texture_types_map()
            return json_texture_types[texture_type]["identifier"]
        return None

    @property
    def unreal_texture_compression_settings(self):
        """Unreal compression settings from texture type"""
        texture_type = self.texture_type
        if(texture_type):
            json_texture_types = TextureManager.get_texture_types_map()
            return TextureManager.get_unreal_compression_method(
                json_texture_types[texture_type]["unreal_compression_method"]
            )
        return None

    @property
    def use_srgb(self):
        """Should this texture use SRGB?"""
        if(self.unreal_texture_compression_settings == unreal.TextureCompressionSettings.TC_MASKS):
            return False
        return True 

    @property
    def unreal_path(self):
        """Absolute path to the current .uasset file"""
        output = os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\content", self.unreal_relative_path.replace("/AssetLibrary/", "") + ".uasset")
        output = output.replace("/", "\\")
        return output

    @property
    def unreal_meta_path(self):
        """Returns the path to the .meta file for the UASSET"""
        return pathing_utils.set_path_file_type(self.unreal_path, "meta")

    def import_to_unreal(self):
        """Import this texture to unreal"""
        unreal_path = self.unreal_path
        if(os.path.isfile(unreal_path)):
            os.chmod(unreal_path, stat.S_IWRITE)

        if(tools_library.program_context() == "ue4"):
            import unreal
            import_task = unreal.AssetImportTask()
            import_task.set_editor_property("filename", self.real_path)
            import_task.set_editor_property("destination_path", os.path.dirname(self.unreal_relative_path))
            import_task.set_editor_property("save", True)
            import_task.set_editor_property("replace_existing", True)
            import_task.set_editor_property("replace_existing_settings", True)
            import_task.set_editor_property("automated", True)


            unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

            for i in import_task.imported_object_paths:
                a = unreal.AssetData(object_path=i)
                t = unreal.AssetRegistryHelpers.get_asset(a)
                if(self.unreal_texture_compression_settings):
                    t.compression_settings = self.unreal_texture_compression_settings

            if(not self.use_srgb):
                t.srgb = False
            
            # create the metadata file
            metadata = {
                "last_import":str(datetime.datetime.now().timestamp()),
                "source_path":self.asset_library_path
            }

            os.chmod(unreal_path, stat.S_IREAD)



            #with open(self.unreal_meta_path, "w") as f:
            #    json.dump(metadata, f)

        else:
            print("Not in unreal!")
            print(tools_library.program_context())
