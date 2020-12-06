import os
import json

import asset_library

asset_library_path = asset_library.path()
asset_library_config_path = os.path.join(asset_library_path, "config.json")

if(os.path.exists(asset_library_config_path)):
    with open(asset_library_config_path) as j:
        json_data = json.load(j)
        url = json_data["git-url"]
        os.system("start \"\" " + url)