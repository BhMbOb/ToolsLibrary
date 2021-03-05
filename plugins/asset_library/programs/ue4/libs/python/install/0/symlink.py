import os

import tools_library
import tools_library.utilities.filemgr

import asset_library


# symlink the current assetlibrary unreal plugin to the current unreal project
tools_library.utilities.filemgr.symlink(
    tools_library.finalizeString("$(AssetLibraryDir)\\Shelves\\Unreal"), 
    tools_library.finalizeString("$(UnrealProjectDir)\\Plugins\\Common")
)
