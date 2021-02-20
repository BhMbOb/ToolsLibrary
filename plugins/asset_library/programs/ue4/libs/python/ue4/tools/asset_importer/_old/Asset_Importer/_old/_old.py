import sys
import os
from glob import glob
import unreal

unreal.log_flush
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

def log(str):
    unreal.log_error(str)

# TEMP:
asset_library_dir = "X:\\"

import_exclude_dirnames = [
    "\\.temp\\",
    "\\.source\\",
    "\\_source\\",
    "\\_temp\\",
    "\\.old\\",
    "\\_old\\"
]


def get_all_textures(dirname):
    """Returns the path of all textures within a directory"""
    output = []
    all_textures = [y for x in os.walk(dirname) for y in glob(os.path.join(x[0], "*.tga"))]
    for texture_path in all_textures:
        if not any(x in texture_path for x in import_exclude_dirnames):
            output.append(texture_path)
    return output


def import_texture(texture_path):
    if(os.path.exists(texture_path)):
        asset_import_task = unreal.AssetImportTask()
        asset_name = os.path.basename(texture_path).replace(".tga", "")
        game_path = os.path.dirname("\\Game\\Asset_Library_Unreal\\" + texture_path.replace(asset_library_dir, "")).replace("\\", "/")

        asset_import_task.set_editor_property("filename", texture_path)
        asset_import_task.set_editor_property("destination_path", game_path.replace("\\", "/"))
        asset_import_task.set_editor_property("replace_existing", True)
        asset_import_task.set_editor_property("replace_existing_settings", True)
        asset_import_task.set_editor_property("save", True)
        asset_import_task.set_editor_property("automated", True)
        asset_tools.import_asset_tasks([asset_import_task])

        for i in asset_import_task.imported_object_paths:
            a = unreal.AssetData(object_path=i)
            t = unreal.AssetRegistryHelpers.get_asset(a)
            compression_setting = unreal.TextureCompressionSettings.TC_DEFAULT

            if(asset_name.endswith("_S") or asset_name.endswith("_F") or asset_name.endswith("_M")):
                compression_setting = unreal.TextureCompressionSettings.TC_MASKS
            elif(asset_name.endswith("_N")):
                compression_setting = unreal.TextureCompressionSettings.TC_NORMALMAP
            t.compression_settings = compression_setting
            print("Imported " + asset_name + " as " + str(compression_setting))


for i in get_all_textures(asset_library_dir):
    import_texture(i)