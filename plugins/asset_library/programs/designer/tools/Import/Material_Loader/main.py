import sys
import os
import json
import sd
from qtpy import QtWidgets, QtCore, uic


import tools_library.filemgr
import tools_library
import asset_library
import asset_library.material
import program.instance


class ExampleWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ExampleWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "main.ui"), self)

        self.target_module = ""
        self.target_material_types = ""

        self.q_combo_module.activated.connect(self.switch_module)
        self.q_combo_type.activated.connect(self.switch_material_type)

        # add an entry to the combo box for each module
        self.q_combo_module.addItem("All Modules")
        for i in asset_library.content_library_paths():
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
        self.show()

    def get_material_types(self):
        output = []
        materials_config = os.path.join(asset_library.path(), "materials_config.json")
        with open(materials_config, "r") as f:
            json_data = json.load(f)
            for t in json_data["material_types"]:
                output.append(t)
        return output

    def get_material_type_prefix(self, material_type):
        output = ""
        materials_config = os.path.join(asset_library.path(), "materials_config.json")
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
        output = []
        material_dirs = []

        modules = []
        material_prefix = self.get_material_type_prefix(self.target_material_types).lower()

        if(self.target_module == "All Modules"):
            for i in asset_library.content_library_paths():
                modules.append(os.path.basename(i))
        else:
            modules = [self.target_module]

        for module in modules:
            module_materials_dir = os.path.join(asset_library.path(), "content", module, "materials")
            if(os.path.isdir(module_materials_dir)):
                for i in os.listdir(module_materials_dir):
                    material_dir = os.path.join(module_materials_dir, i)
                    if(os.path.isdir(material_dir) and (i.lower().startswith(material_prefix))):
                        material_dirs.append(material_dir)

        for material_dir in material_dirs:
            material_dirname = os.path.basename(material_dir)
            for i in os.listdir(material_dir):
                if(i.startswith("M_" + material_dirname) and (i.endswith(".material"))):
                    output.append(os.path.join(material_dir, i))


        self.q_materials_list.clear()
        self.q_materials_list.paths = {}
        for i in output:
            self.q_materials_list.addItem(os.path.basename(i))
            self.q_materials_list.paths[os.path.basename(i)] = i
            self.q_materials_list.itemDoubleClicked.connect(self.select_material)


    def select_material(self, material_list_index):
        material = asset_library.material.Material.from_file(
            self.q_materials_list.paths[material_list_index.text()]
        )
        program.instance.load_sbs(material.get_source_sbs())


win = ExampleWindow()
