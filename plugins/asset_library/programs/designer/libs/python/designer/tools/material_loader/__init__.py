import os
import json
from qtpy import QtCore

import tools_library
from tools_library.types import _tool_window
import tools_library.designer.instance
import tools_library.designer.package

import asset_library
import asset_library.framework.asset_types.material

MaterialManager = asset_library.framework.asset_types.material.material_manager.MaterialManager


class TMaterialLoader(_tool_window.ToolWindow):
    """Tool widget used for loading in Asset Library materials to Designer directly"""
    def __init__(self):
        super(TMaterialLoader, self).__init__()

        self.q_combo_module.activated.connect(self.switch_module)
        self.q_combo_type.activated.connect(self.switch_material_type)
        self.q_chk_show_instances.stateChanged.connect(self.get_materials)

        # add an entry to the combo box for each asset library module
        self.q_combo_module.addItem("All Modules")
        for i in asset_library.paths.get_content_modules():
            module_name = os.path.basename(i)
            self.q_combo_module.addItem(module_name)
        self.target_module = self.q_combo_module.currentText()

        # add all material types to the combo box
        for i in MaterialManager.material_types:
            self.q_combo_type.addItem(i)
        self.target_material_types = self.q_combo_type.currentText()

        self.switch_material_type()
        self.switch_module()

        self.finalize()

    def switch_module(self):
        """Set the current target module to view materials from"""
        self.target_module = self.q_combo_module.currentText()
        self.get_materials()

    def switch_material_type(self):
        """Set the current target material types to show"""
        self.target_material_types = self.q_combo_type.currentText()
        self.get_materials()

    def get_materials(self):
        """Return a list of materials respecting the current module/type settings"""
        modules = []
        prefix = MaterialManager.material_types[self.target_material_types]["prefix"].lower()

        if(self.target_module == "All Modules"):
            for i in asset_library.paths.get_content_modules():
                modules.append(os.path.basename(i))
        else:
            modules = [self.target_module]

        materials = asset_library.framework.asset_types.material.MaterialManager.get_materials(
            module_names=tuple(modules),
            prefixes=prefix
        )

        self.q_materials_list.clear()
        self.q_materials_list.materials = {}
        added_material_sbs_list = []
        for material in materials:
            material_path = material.path
            material_name = material.name

            if(os.path.isfile(material.path)):
                if(self.q_chk_show_instances.isChecked()):
                    self.q_materials_list.addItem(material.name)
                    self.q_materials_list.materials[material.name] = material
                    self.q_materials_list.itemDoubleClicked.connect(self.load_material)
                else:
                    if(material.source_sbs not in added_material_sbs_list):
                        added_material_sbs_list.append(material.source_sbs)
                        self.q_materials_list.addItem(material.outer_name)
                        self.q_materials_list.materials[material.outer_name] = material
                        self.q_materials_list.itemDoubleClicked.connect(self.load_material)

    def load_material(self, material_list_index):
        """Load the currently selected material"""
        tools_library.designer.package.load(self.q_materials_list.materials[material_list_index.text()].source_sbs)


if __name__ == "__main__":
    win = TMaterialLoader()