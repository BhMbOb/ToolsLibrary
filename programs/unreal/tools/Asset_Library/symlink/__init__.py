import os

import tools_library
import tools_library.filemgr
import tools_library.asset_library

project_content_dir = tools_library.finalizeString("$(UnrealProjectPath)Content")
project_source_dir = tools_library.finalizeString("$(UnrealProjectPath)Source")
asset_library_dir = tools_library.finalizeString("$(AssetLibraryPath)")
project_name = tools_library.finalizeString("$(UnrealProjectName)")


def symlink(src, dest):
    try:
        tools_library.filemgr.makedir(os.path.dirname(dest))

        os.symlink(
            os.path.realpath(src), 
            os.path.realpath(dest),
            target_is_directory=True
        )
    except:
        print("Could not create symlink: ")
        print(src)
        print(dest)
        print("---")


# add the whole asset library to the content folder
symlink(asset_library_dir, os.path.join(project_content_dir, "Asset_Library"))


# loop over all unreal shelves and add them
# public = "Project/Source/Project/Public/Asset_Library/ShelfName"
# private = "Project/Source/Project/Private/Asset_Library/ShelfName"
for shelf_name in (tools_library.asset_library.shelf_library.getNames("Unreal")):
    shelf_path = os.path.abspath(tools_library.asset_library.shelf_library.getPath(shelf_name, "Unreal"))
    shelf_path_source_private = os.path.join(shelf_path, "Source\\Private\\")
    shelf_path_source_public = os.path.join(shelf_path, "Source\\Public\\")

    shelf_path_destination_private = os.path.join(project_source_dir, project_name, "Private\\Asset_Library", shelf_name)
    shelf_path_destination_public = os.path.join(project_source_dir, project_name, "Public\\Asset_Library", shelf_name)

    if(os.path.exists(shelf_path_source_private)):
        symlink(shelf_path_source_private, shelf_path_destination_private)

    if(os.path.exists(shelf_path_source_public)):
        symlink(shelf_path_source_public, shelf_path_destination_public)