import os
import glob
import unreal

import tools_library.ue4

import asset_library


shaders_dir = os.path.join(
    asset_library.paths.root(),
    "shelves\\unreal\\content\\shaders"
)

shader_uasset_paths = []
for i in glob.glob(shaders_dir + "\\**\\*.uasset", recursive=True):
    shd_name = os.path.basename(i)
    if(shd_name.lower().startswith("shd_")):
        shader_uasset_paths.append(i.lower())

print(shader_uasset_paths)
