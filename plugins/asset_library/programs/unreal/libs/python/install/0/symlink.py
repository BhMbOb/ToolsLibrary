import os

import tools_library
import tools_library.symlink

import asset_library

tools_library.symlink.link(
    tools_library.finalizeString("$(AssetLibraryPath)\\Shelves\\Unreal\\Common"), 
    tools_library.finalizeString("$(UnrealProjectPath)\\Plugins\\Common")
)