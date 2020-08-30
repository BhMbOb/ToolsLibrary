import os

import tools_library
import tools_library.filemgr

project_content_dir = tools_library.finalizeString("$(UnrealProjectPath)Content")
asset_library_dir = tools_library.finalizeString("$(AssetLibraryPath)")

#tools_library.filemgr.makedir(os.path.join(project_content_dir, "Asset_Library"))

os.symlink(
    os.path.realpath(asset_library_dir), 
    os.path.realpath(os.path.join(project_content_dir, "Asset_Library")), 
    target_is_directory=True
)