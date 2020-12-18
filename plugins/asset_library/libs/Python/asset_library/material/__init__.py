import os
import json

import asset_library


class Material(object):
    def __init__(self):
        pass
        #textures = []
        #parameters = []
        #instances = []

    @staticmethod
    def from_file(path):
        """Create a new material object from a ".material" file"""
        material = Material()
        material.path = path
        return material

    def get_children(self):
        # TODO:
        pass

    def is_parent(self, possible_child):
        # TODO:
        return False

    def is_instance(self, possible_parent):
        # TODO:
        pass

    def get_source_sbs(self):
        """Returns the path to the parent ".sbs" file for this material (as stored in the .material file)"""
        with open(self.path, "r") as f:
            json_data = json.load(f)
            material_name = json_data["metadata"]["name"]
        return os.path.join(os.path.dirname(self.path), ".source", material_name + ".sbs")


def get_materials_from_files(module_names=[], prefixes=[]):
    """Return a list of materials which fit certain criteria"""
    materials = []

    if(type(module_names) is not tuple):
        module_names = (module_names)

    if(type(prefixes) is not tuple):
        prefixes = (prefixes)

    material_dirs = []
    for module in module_names:
        module_materials_dir = os.path.join(asset_library.path(), "content", module, "materials")
        if(os.path.isdir(module_materials_dir)):
            for material_name in os.listdir(module_materials_dir):
                material_dir = os.path.join(module_materials_dir, material_name)
                if(os.path.isdir(material_dir) and (material_name.lower().startswith(prefixes))):
                    material_dirs.append(material_dir)

    for material_dir in material_dirs:
        material_dirname = os.path.basename(material_dir)
        for i in os.listdir(material_dir):
            if(i.startswith("M_" + material_dirname) and (i.endswith(".material"))):
                materials.append(Material.from_file(os.path.join(material_dir, i)))

    return materials
