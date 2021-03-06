import os
import json
import shutil
import xml.etree.ElementTree

import tools_library
import tools_library.programs.designer
import asset_library


# add all asset library shelves to designer
designer_shelves_dir = os.path.join(asset_library.paths.root(), "shelves\\designer")
for i in os.listdir(designer_shelves_dir):
    designer_shelf_dir = os.path.join(designer_shelves_dir, i)
    if(os.path.isdir(designer_shelf_dir)):
        designer_shelf_sbsprj_path = os.path.join(designer_shelf_dir, "config\\shelf.sbsprj")
        if(os.path.isfile(designer_shelf_sbsprj_path)):
            tools_library.programs.designer.add_sbsprj(designer_shelf_sbsprj_path)
