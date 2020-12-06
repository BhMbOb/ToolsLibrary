import os
import sys
import json

import tools_library
from asset_library import content_library, shelf_library, shader_library


def path():
    return tools_library.finalizeString("$(AssetLibraryPath)")
