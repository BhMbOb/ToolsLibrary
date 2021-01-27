import os

from asset_library.asset_types import material

mat = material.Material("X:\\Content\\Common\\Materials\\Micro_Moss\\M_Micro_Moss_01.material")
print(os.path.isfile(mat.source_sbs))