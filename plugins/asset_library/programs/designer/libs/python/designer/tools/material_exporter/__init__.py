import sys
import os
import json
import sd
from qtpy import QtWidgets, QtCore, uic, QtGui

import tools_library
import tools_library.utilities.pathing as path_utils
from tools_library.types import _tool_window
import tools_library.utilities.filemgr
import tools_library.designer.instance

import asset_library
import asset_library.designer.scene.export
from asset_library.tools import material_property_editor


class TMaterialExporter(_tool_window.ToolWindow):
    def __init__(self):
        super(TMaterialExporter, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # reference to the current instance of the material editor
        self.material_editor_tool_instance = None

        self.q_btn_export.clicked.connect(
            lambda x: asset_library.designer.scene.export.export_package()
        )

        self.q_btn_temp_update.clicked.connect(self.update_widget)
        self.q_btn_show_in_explorer.clicked.connect(
            lambda x: tools_library.designer.package.show_in_explorer()   
        )
        self.finalize()

    def update_widget(self):
        self.q_materials_list.clear()
        self.q_materials_list.materials = {}
        added_material_sbs_list = []

        if(tools_library.designer.instance.get_current_package()):
            material_dir = os.path.dirname(tools_library.designer.instance.get_current_package().getFilePath()) + "\\..\\"
            for material in os.listdir(material_dir):
                print(material)
                if(material.endswith(".material")):
                    self.q_materials_list.addItem(material)
                    self.q_materials_list.itemDoubleClicked.connect(self.set_material_parameters)

    def set_material_parameters(self, mat_path_list_wgt):
        if(self.material_editor_tool_instance != None):
            self.material_editor_tool_instance.setParent(None)
            self.material_editor_tool_instance.deleteLater()
            self.material_editor_tool_instance = None


if __name__ == "__main__":
    win = asset_library.designer.scene.export.export_package()