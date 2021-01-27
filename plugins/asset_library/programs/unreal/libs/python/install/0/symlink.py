import os

import tools_library
import tools_library.filemgr

import asset_library


# symlink the current assetlibrary unreal plugin to the current unreal project
tools_library.filemgr.symlink(
    tools_library.finalizeString("$(AssetLibraryDir)\\Shelves\\Unreal\\Common"), 
    tools_library.finalizeString("$(UnrealProjectPath)\\Plugins\\Common")
)
