import os

import tools_library
import tools_library.filemgr
import asset_library

project_content_dir = tools_library.finalizeString("$(UnrealProjectPath)Content")
project_source_dir = tools_library.finalizeString("$(UnrealProjectPath)Source")
asset_library_dir = tools_library.finalizeString("$(AssetLibraryPath)")
project_name = tools_library.finalizeString("$(UnrealProjectName)")


def symlink(src, dest):
    try:
        tools_library.filemgr.makedir(os.path.dirname(dest))

        if(os.path.isdir(src)):
            if(os.path.islink(dest)):
                os.unlink(dest)
            os.symlink(
                os.path.realpath(src),
                os.path.realpath(dest),
                target_is_directory=True
            )
    except OSError as error:
        if(os.path.isdir(dest)):
            print("[Asset Library][Symlink] Warning: Destination directory already exists!")
        elif(not os.path.isdir(src)):
            print("[Asset Library][Symlink] Warning: Source directory does not exist!")
        else:
            print("[Asset Library][Symlink] Error: Symlink failed!")
            print(error)


symlink(
    tools_library.finalizeString("$(AssetLibraryPath)\\Shelves\\Unreal\\Common"), 
    tools_library.finalizeString("$(UnrealProjectPath)\\Plugins\\Common")
)