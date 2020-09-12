import tools_library
import tools_library.asset_library

tools_library.asset_library.content_library.make_content_library(
    tools_library.finalizeString("$(UnrealProjectPath)Content\\"),
    "Common\\Content"
)

tools_library.asset_library.shader_library.make_shader_library(
    tools_library.finalizeString("$(UnrealProjectPath)Content\\"),
    "Common\\Shaders"
)
