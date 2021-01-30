import sys
import os
import json
import sd
from qtpy import QtWidgets, QtCore, uic, QtGui

import tools_library
from tools_library.templates import tool_window
import tools_library.filemgr
import program.instance

import asset_library
import asset_library.asset_types.material


class TMaterialLoader(tool_window.ToolWindow):
    def __init__(self):
        super(TMaterialLoader, self).__init__()

        self.target_module = ""
        self.target_material_types = ""

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
        for i in self.get_material_types():
            self.q_combo_type.addItem(i)
        self.target_material_types = self.q_combo_type.currentText()

        #
        self.switch_material_type()
        self.switch_module()

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.finalize()

    def should_show_instances(self):
        return self.q_chk_show_instances.isChecked()

    def get_material_types(self):
        output = []
        materials_config = os.path.join(asset_library.paths.root(), "materials_config.json")
        with open(materials_config, "r") as f:
            json_data = json.load(f)
            for t in json_data["material_types"]:
                output.append(t)
        return output

    def get_material_type_prefix(self, material_type):
        output = ""
        materials_config = os.path.join(asset_library.paths.root(), "materials_config.json")
        with open(materials_config, "r") as f:
            json_data = json.load(f)
            output = json_data["material_types"][material_type]
        return output

    def switch_module(self):
        self.target_module = self.q_combo_module.currentText()
        self.get_materials()

    def switch_material_type(self):
        self.target_material_types = self.q_combo_type.currentText()
        self.get_materials()

    def get_materials(self):
        modules = []
        prefix = self.get_material_type_prefix(self.target_material_types).lower()

        if(self.target_module == "All Modules"):
            for i in asset_library.paths.get_content_modules():
                modules.append(os.path.basename(i))
        else:
            modules = [self.target_module]

        materials = asset_library.asset_types.material.MaterialManager.get_materials(
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
                if(self.should_show_instances()):
                    self.q_materials_list.addItem(material.name)
                    self.q_materials_list.materials[material.name] = material
                    self.q_materials_list.itemDoubleClicked.connect(self.select_material)
                else:
                    if(material.source_sbs not in added_material_sbs_list):
                        added_material_sbs_list.append(material.source_sbs)
                        self.q_materials_list.addItem(material.outer_name)
                        self.q_materials_list.materials[material.outer_name] = material
                        self.q_materials_list.itemDoubleClicked.connect(self.select_material)


    def select_material(self, material_list_index):
        program.instance.load_sbs(self.q_materials_list.materials[material_list_index.text()].source_sbs)