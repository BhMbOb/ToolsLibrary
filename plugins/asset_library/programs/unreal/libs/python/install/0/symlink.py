import os

import tools_library
import tools_library.symlink

import asset_library


# symlink the current assetlibrary unreal plugin to the current unreal project
tools_library.symlink.link(
    tools_library.finalizeString("$(AssetLibraryDir)\\Shelves\\Unreal\\Common"), 
    tools_library.finalizeString("$(UnrealProjectPath)\\Plugins\\Common")
)
