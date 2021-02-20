import os

import tools_library.utilities.qt
import tools_library.utilities.json as json_utils
import tools_library.utilities.filemgr

import asset_library


# pick the current Asset Library
app = tools_library.utilities.qt.get_application()
asset_library_path = tools_library.utilities.filemgr.pick_file(title="Select Asset Library", file_types="Asset Library (*.assetlibrary)", start=asset_library.paths.root())
asset_library_path = asset_library_path.replace("/", "\\")
if(os.path.isfile(asset_library_path)):
    json_utils.set_file_property(tools_library.get_config("client_settings.json"), "plugins.asset_library.path", asset_library_path)
