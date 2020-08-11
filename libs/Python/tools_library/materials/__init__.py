import os
import sys
import json
import winreg

import tools_library

# TEMP:
materials_folder = os.path.join(tools_library.getDefaultAssetLibrary(), "Common\\Materials")
materials_json = tools_library.getConfig("materials\\properties.json")


def get_material_types():
    '''Returns the names of all valid material types'''
    output = []

    with open(materials_json, "r") as j:
        json_data = json.load(j)

        for i in range(len(json_data["material_types"])):
            output.append(list(json_data["material_types"])[i])

    return output


def get_texture_types():
    '''Returns the names of all valid texture types'''
    output = []

    with open(materials_json, "r") as j:
        json_data = json.load(j)

        for i in range(len(json_data["texture_types"])):
            output.append(list(json_data["texture_types"])[i])

    return output


def get_texture_type(path):
    '''Returns the material texture type if valid - None if not'''
    output = None

    texture_type = path.split("_")[-1].lower().replace(".tga", "").upper()

    with open(materials_json, "r") as j:
        json_data = json.load(j)

        if(texture_type in json_data["texture_types"]):
            output = texture_type

    return output


def is_valid_material_texture(path):
    '''Returns whether a material texture is valid - requirements:
     > Name begins with "T_"
     > File is a ".tga"
     > File exists
     > Texture is a valid material texture type (Ie, _D)'''
    output = False

    file_name = os.path.basename(path)

    if(
        os.path.exists(path) and
        file_name.startswith("T_") and
        path.lower().endswith(".tga") and
        get_texture_type(path) is not None
    ):
        output = True

    return output


def get_all_material_textures(material_name):
    '''Returns all valid material textures from a given material name'''
    output = []

    material_folder = os.path.join(materials_folder, material_name)

    if(os.path.exists(material_folder)):
        for i in os.listdir(material_folder):
            if(material_name in i):
                if(is_valid_material_texture(os.path.join(material_folder, i))):
                    output.append(i)

    return output


def get_texture_instance(texture_name, material_name=None):
    '''Returns the instance of a parent texture this texture is targeted towards'''
    split_data = texture_name.split(".")[0].split("_")

    possible_texture_instance = split_data[-2] if get_texture_variant(texture_name) is None else split_data[-3]

    texture_type = split_data[-1]
    texture_instance = split_data[-2] if split_data[-2].isdigit() else split_data[-3] if split_data[-3].isdigit() else None

    if(texture_instance is not None):
        texture_instance = int(texture_instance)

    return texture_instance


def get_texture_variant(texture_name):
    '''Returns the variant of a parent instance this texture is targeted towards'''
    split_data = texture_name.split(".")[0].split("_")
    abc_array = list("abcdefghijklmnopqrstuvwxyz")

    # if the variant is an "a, b, c" based type..
    if(split_data[-2] in abc_array):
        return split_data[-2]
    # if there is a valid instance number and an undefined variable after..
    elif(split_data[-3].isdigit()):
        return split_data[-2]
    else:
        return None


def get_final_material_texture(material_name, material_instance, material_variant, texture_type):
    output = None

    possible_textures = get_all_material_textures(material_name)

    for t in possible_textures:

        texture_instance = get_texture_instance(t)
        texture_variant = get_texture_variant(t)

        # if we've found a matching texture type..
        if(get_texture_type(t) == texture_type):

            # complete match
            if((material_variant == texture_variant) and (material_instance == texture_instance)):
                output = t

            # no instance or variant
            if((material_variant == None) and (material_instance == None) and (texture_instance == None) and (texture_variant == None)):
                output = t

            # instance but no variant
            elif((material_instance == texture_instance) and (material_variant is None) and (texture_variant is None)):
                output = t

            #  fallback - instance but no variant
            elif(material_variant is not None):
                fallback = get_final_material_texture(material_name, material_instance, None, texture_type)
                if(fallback is not None):
                    output = fallback

            # fallback - no instance and no variant
            elif(material_instance is not None):
                fallback = get_final_material_texture(material_name, None, None, texture_type)
                if(fallback is not None):
                    output = fallback

    return output


def get_material_textures(name, instance=None, variant=None):
    '''Returns all textures for a given material from the name, instance and variant'''
    output = []

    possible_textures = get_all_material_textures(name)

    for t in possible_textures:
        texture_instance = get_texture_instance(t)
        texture_variant = get_texture_variant(t)
        texture_type = get_texture_type(t)

        if((texture_instance in [instance, None]) and (texture_variant in [variant, None])):

            found_texture = get_final_material_texture(name, texture_instance, texture_variant, texture_type)
            if((found_texture is not None) and (found_texture not in output)):
                output.append(found_texture)

    return output


#TEMP:
print(get_material_textures("Wall_Brick_Standard", instance=1, variant="a"))