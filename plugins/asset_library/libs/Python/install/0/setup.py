import os

import tools_library.utilities.qt
import tools_library.utilities.json as json_utils
import tools_library.filemgr

import asset_library

print(asset_library.path())
print("---")

app = tools_library.utilities.qt.get_application()

asset_library_path = tools_library.filemgr.pick_file(title="Select Asset Library", file_types="Asset Library (*.assetlibrary)", start=asset_library.path())
asset_library_path = asset_library_path.replace("/", "\\")

if(os.path.isfile(asset_library_path)):
    json_utils.set_file_property(tools_library.getConfig("client_settings.json"), "plugins.asset_library.path", asset_library_path)
