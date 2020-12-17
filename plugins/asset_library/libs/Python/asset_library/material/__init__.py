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


'''def get_all_materials():
    output = []

    material_dirs = []
    for content_library_path in asset_library.content_library_paths():
        content_library_materials_dir = os.path.join(content_library_path, "materials")
        if(os.path.isdir(content_library_materials_dir)):
            for material_dirname in os.listdir(content_library_materials_dir):
                if(asset_library.is_valid_directory_name(material_dirname)):
                    material_dirs.append(os.path.join(content_library_materials_dir, material_dirname))

    for i in material_dirs:
        print(i)


get_all_materials()'''