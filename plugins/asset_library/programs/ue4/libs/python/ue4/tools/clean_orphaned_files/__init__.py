'''"""
An orphaned file is a .uasset file contained within an "imported" folder which does not map to an
existing source asset in the asset library

These files are considered dirty and unsafe to delete - so are instead moved to the "orphaned" folder
"""
import os
import glob
import unreal

import tools_library.programs.unreal

import asset_library.paths
from asset_library.types.uasset import Uasset


def find_orphaned_uassets():
    """Returns a list containing all orphaned (sourceless) uasset file paths"""
    output = []

    module_dirs = asset_library.paths.get_content_modules()
    for module_dir in module_dirs:
        asset_library_unreal_content_dir = os.path.join(asset_library.paths.root(), "shelves\\unreal\\common\\")
        module_dir_unreal = module_dir.replace(asset_library.paths.root(), asset_library_unreal_content_dir)

        if(os.path.isdir(module_dir_unreal)):
            module_dir_unreal_imported = os.path.join(module_dir_unreal, "imported")
            all_files = glob.glob(module_dir_unreal_imported + "/**/*.uasset", recursive=True)
            for i in all_files:
                file_path_unreal = i
                file_path_assetlibrary = file_path_unreal.replace(module_dir_unreal_imported, module_dir)
                uasset = Uasset(file_path_unreal)
                if(not os.path.isfile(uasset.source_file)):
                    output.append(uasset)
    return output



if __name__ == "__main__":
    for i in find_orphaned_uassets():
        unreal.EditorAssetLibrary.rename_asset(
            i.content_browser_path,
            i.content_browser_path.replace("\\imported\\", "\\Orphaned\\")            
        )
        print("Moved file to orphaned folder: " + i.content_browser_path)
'''