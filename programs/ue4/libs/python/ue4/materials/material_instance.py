try:
    import unreal
except:
    pass


def set_texture(material_instance, parameter_name, texture_path):
    """Set a texture path on a material instance
    All paths are unreal relative"""
    if(not unreal.EditorAssetLibrary.find_asset_data(texture_path).get_asset()):
        return False
    texture_asset = unreal.EditorAssetLibrary.find_asset_data(texture_path).get_asset()
    output = unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value(material_instance, parameter_name, texture_asset)
    return output

print("okokok")