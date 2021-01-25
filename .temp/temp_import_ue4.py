import tools_library
import tools_library.programs.unreal as unreal

source_path = "X:\\\\Content\\\\Common\\\\Materials\\\\Micro_Rubber\\\\T_Micro_Rubber_01_DA.tga"
dest_path = "/Game/Textures/"

command_lines = [
    "import program.importers.textures",
    "print(import program.importers.textures)",
    "print(\"start 1\")",
    "programs.importers.textures.import_texture(\"" + 
    source_path +
    "\", \"" +
    dest_path +
    "\", unreal_module=\"AssetLibrary\")",
    "print(\"done 1\")"
]

for i in command_lines:
    print(i)
    unreal.send_command(i)