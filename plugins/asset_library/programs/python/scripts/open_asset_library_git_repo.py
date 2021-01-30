"""
Open the current AssetLibrary git repo in web browser
"""
import os
import json

import tools_library

import asset_library


repo_path = tools_library.utilities.json.get_property(
    asset_library.paths.path(),
    "info.git_url"
)

os.system("start \"\" " + repo_path)