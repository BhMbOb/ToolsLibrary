import os
import functools
import json
import glob

import tools_library.utilities.pathing
import tools_library.utilities.json as json_utils

import asset_library
from asset_library.framework.asset_types.material.material_asset import Material


class __MaterialManager(object):
    __instance__ = None

    def get_materials(self, module_names=[], prefixes=[]):
        """Returns a list of materials fitting certain criteria"""
        output = []

        if(type(module_names) is not tuple):
            module_names = (module_names)

        if(type(prefixes) is not tuple):
            prefixes = (prefixes)

        material_dirs = []

        for module in module_names:
            module_materials_dir = os.path.join(asset_library.paths.root(), "content", module, "materials")
            if(os.path.isdir(module_materials_dir)):
                for material_name in os.listdir(module_materials_dir):
                    material_dir = os.path.join(module_materials_dir, material_name)
                    if(os.path.isdir(material_dir) and (material_name.lower().startswith(prefixes))):
                        material_dirs.append(material_dir)

        for material_dir in material_dirs:
            material_dirname = os.path.basename(material_dir)
            for i in os.listdir(material_dir):
                if(i.startswith("M_" + material_dirname) and (i.endswith(".material"))):
                    output.append(Material(os.path.join(material_dir, i)))

        return output

    def import_to_unreal(self):
        """Import all of the materials to unreal"""
        target_module_dirs = asset_library.paths.get_content_modules()
        for target_module_dir in target_module_dirs:
            target_module_materials_dir = os.path.join(target_module_dir, "materials")
            module_materials = glob.glob(target_module_materials_dir + "/**/*.material", recursive=True)
            for i in module_materials:
                is_valid = "." not in os.path.dirname(i)
                if(is_valid):
                    mat = Material(i)
                    mat.import_to_unreal()

    def get_material_parameters(self, target_material):
        materials_hierachy = []
        shader_hierachy = []

    def get_parent_shader_name(self, mat):
        """Return the name of the parent shader for this material"""
        self_shader = json_utils.get_property(mat.real_path, "metadata.shader")
        if(self_shader is not ""):
            return self_shader
        

    def get_parent_material_name(self, mat):
        """Return the name of the parent material for this material if it is an instance"""
        return json_utils.get_property(mat.real_path, "metadata.parent")


if(__MaterialManager.__instance__ is None):
    __MaterialManager.__instance__ = __MaterialManager()
MaterialManager = __MaterialManager.__instance__
