import os

from tools_library.utilities import json as json_utils
from tools_library import filemgr
from tools_library.utilities import qt as qt_utils

import asset_library

app = qt_utils.get_application()

def pick_shader(material_filepath):
    title = str(
        "Select Shader For: " +
        os.path.basename(material_filepath)
    )
    target_shader = filemgr.pick_file(title=title, start="x:\\shelves\\source\\shaders", file_types="Asset Library Shader (*.shader)")

    if(target_shader != ""):
        json_utils.set_file_property(material_filepath, "shader", asset_library.paths.map_path(target_shader))



current_material_dir = "X:\\Content\\Common\\Materials\\Terrain_Concrete"

all_materials = []
for i in os.listdir(current_material_dir):
    if(i.endswith(".material")):
        all_materials.append(os.path.join(current_material_dir, i))

# test for getting shaders
for i in all_materials:
    pick_shader(i)
    '''print(i)
    shd = json_utils.get_property(i, "shader")
    print(shd)
    print("-----")'''


