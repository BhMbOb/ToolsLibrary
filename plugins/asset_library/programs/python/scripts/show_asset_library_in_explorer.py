"""
Open a new explorer window at the current asset library root directory
"""
import os

import asset_library


os.startfile(asset_library.paths.root())
