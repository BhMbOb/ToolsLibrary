import os
import unreal


def import_texture(filepath, unreal_path, unreal_module=""):
    print("WARNING THIS FUNCTION IS DEPRECATED")
    print("start")
    print(filepath)
    if(os.path.isfile(filepath)):
        asset_import_task = unreal.AssetImportTask()
        asset_name = os.path.basename(filepath).split(".")[0]
        
        game_path = "\\Game\\"
        game_path += "\\Content\\" if unreal_module == "" else ("\\" + unreal_module + "\\")
        game_path += os.path.dirname(filepath.replace("\\", "/"))
        print("----")
        print(game_path)

        asset_import_task.set_editor_property("filename", filepath)
        asset_import_task.set_editor_property("destination_path", "/Game/Textures")
        asset_import_task.set_editor_property("replace_existing", True)
        asset_import_task.set_editor_property("replace_existing_settings", True)
        asset_import_task.set_editor_property("save", True)
        asset_import_task.set_editor_property("automated", True)

        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([asset_import_task])

        for i in asset_import_task.imported_object_paths:
            asset = unreal.AssetData(object_path=i)
            task = unreal.AssetRegistryHelpers.get_asset(asset)

            if(asset_name.endswith(("_S", "_F", "_M"))):
                compression_settings = unreal.TextureCompressionSettings.TC_MASKS
            elif(asset_name.endswith("_N")):
                compression_settings = unreal.TextureCompressionSettings.TC_NORMALMAP
            elif(asset_name.startswith("T_Cube_")):
                compression_settings = unreal.TextureCompressionSettings.TC_HRD
            else:
                compression_settings = unreal.TextureCompressionSettings.TC_DEFAULT

            task.compression_settings = compression_settings
            print("Imported " + asset_name + " as " + str(compression_settings))