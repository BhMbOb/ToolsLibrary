import os
import sys

import tools_library
from tools_library.templates import tool_window


class TAssetLibraryImporter(tool_window.ToolWindow):
    def __init__(self):
        super(TAssetLibraryImporter, self).__init__()
        self.finalize()


tool = TAssetLibraryImporter()

import os
import sys
import json
import datetime
import glob
import unreal

from qtpy import QtWidgets, QtCore, uic

import asset_library
from asset_library.asset_types import texture, material

from importlib import reload
reload(texture)
reload(material)


class Tool(QtWidgets.QWidget):
    def __init__(self):
        super(Tool, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "main.ui"), self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()

        # add all modules to the dropdown
        self.q_ddl_targetModule.addItem("All Modules")
        self.q_ddl_targetModule.currentIndex = 0
        self.target_module_name = self.q_ddl_targetModule.itemText(0).lower()
        for i in asset_library.paths.get_content_modules():
            module_name = os.path.basename(i)
            self.q_ddl_targetModule.addItem(module_name)

        self.q_ddl_targetModule.currentIndexChanged.connect(self.module_changed)

        self.q_btnImport.clicked.connect(self.run_import)

    def module_changed(self, value):
        self.target_module_name = self.q_ddl_targetModule.itemText(value).lower()
        self.q_ddl_targetModule.currentIndex = value

    def run_import(self):
        target_module_dirs = []

        if(self.q_ddl_targetModule.currentIndex == 0):
            # 0 = All Modules
            target_module_dirs = asset_library.paths.get_content_modules()
        else:
            target_module_dirs = [asset_library.paths.get_content_module(self.target_module_name)]


        # Textures Import
        for target_module_dir in target_module_dirs:
            break
            target_module_textures_dir = os.path.join(target_module_dir, "textures")
            module_textures = glob.glob(target_module_textures_dir + "/**/*.tga", recursive=True)
            for i in module_textures:
                is_importable = "." not in os.path.dirname(i)
                if("." not in os.path.dirname(i)):
                    tex = texture.Texture(i)
                    tex.import_to_unreal()

        # Geometry Import
        # 1) Import geomtry
        # 2) Create .meta file
        # 3) Generate materials
        # 4) Set imported .uasset to read only

        # Materials Import
        for target_module_dir in target_module_dirs:
            target_module_materials_dir = os.path.join(target_module_dir, "materials")
            module_materials = glob.glob(target_module_materials_dir + "/**/*.material", recursive=True)
            for i in module_materials:
                is_importable = "." not in os.path.dirname(i)
                mat = material.Material(i)
                mat.import_to_unreal()
                for i in mat.get_textures():
                    print(i.real_path)

                    default_material_upath = "/AssetLibrary/Common/Manual/Shaders/Colour/SHD_Colour"

                    u_material_path = mat.unreal_path

                    if(unreal.EditorAssetLibrary.does_asset_exist(mat.unreal_path)):
                        u_mat_inst = unreal.EditorAssetLibrary.find_asset_data(mat.unreal_path).get_asset()
                    else:
                        u_mat_inst = unreal.AssetToolHelpers.get_asset_tools().create_asset(mat.name, mat.unreal_dir, unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())

                    #mat_parent = unreal.EditorAssetLibrary.find_asset_data("/AssetLibrary/common/manual/shaders/object/shd_abs_object")
                    #unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(mat_inst, "uvscale", 322.0)
                    """
                    # TEMP: Test material instancing
                    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

                    mat_inst_name = "TestMaterial"
                    mat_inst_dir = "/Game/_Temp"
                    mat_inst_path = mat_inst_dir + "/" + mat_inst_name

                    if(unreal.EditorAssetLibrary.does_asset_exist(mat_inst_path)):
                        mat_inst = unreal.EditorAssetLibrary.find_asset_data(mat_inst_path).get_asset()
                    else:
                        mat_inst = asset_tools.create_asset("TestMaterial", "/Game/_Temp", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())

                    unreal.MaterialEditingLibrary.set_material_instance_parent(mat_inst, mat_parent.get_asset())

                    return
                    """

        # 1) Import all textures
        # 2) Geenrate Unreal Material
        # 3) Create .meta file
        # 4) Set imported .uasset to read only


if(__name__ == "__main__"):
    if(not QtWidgets.QApplication.instance()):
        app = QtWidgets.QApplication(sys.argv)

    win = Tool()
    print("Module Importer")