import os
import json
import glob
from qtpy import QtWidgets, QtCore, uic, QtGui

import tools_library
import tools_library.utilities.json as json_utils
from tools_library.utilities.qt.widgets import QCollapsibleWidget
from tools_library.types import _tool_window

import asset_library
import asset_library.framework.asset_types.shader as shader


class TMaterialPropertyEditor(_tool_window.ToolWindow):
    def __init__(self, material):
        super(TMaterialPropertyEditor, self).__init__()
        self.material = material

        #
        self.overriden_metadata = {

        }
        self.overriden_textures = {

        }
        self.overriden_parameters = {

        }

        # QT
        self.q_parameters_layout = QCollapsibleWidget(title="Parameters")
        self.q_main_layout.addWidget(self.q_parameters_layout)

        # add a new entry to the ddl for each valid shader
        self.q_ddl_shaders.clear()
        self.q_ddl_shaders.addItem("N/A")
        self.q_ddl_shaders.currentIndexChanged.connect(self.shader_updated)
        for s in shader.ShaderManager.get_shader_names():
            self.q_ddl_shaders.addItem(s)
            if(s.lower() == json_utils.get_property(self.material, "metadata.shader").lower()):
                self.q_ddl_shaders.setCurrentIndex(self.q_ddl_shaders.count() - 1)

        #
        self.q_save_cancel.clicked.connect(self.save_or_cancel)

        #
        self.finalize()

    def shader_updated(self, index):
        shader_name = self.q_ddl_shaders.itemText(index)
        if(shader_name != "N/A"):
            self.overriden_metadata["shader"] = shader_name
        else:
            self.overriden_metadata["shader"] = ""

    def save_or_cancel(self, button):
        if(button.text() == "Save"):
            with open(self.material) as json_file:
                data = json.load(json_file)
                for metadata_key in self.overriden_metadata:
                    data["metadata"][metadata_key] = self.overriden_metadata[metadata_key]
                for texture_key in self.overriden_textures:
                    data["textures"][texture_key] = self.overriden_textures[texture_key]
                for parameter_key in self.overriden_parameters:
                    data["parameters"][parameter_key] = self.overriden_parameters[paramete_key]
            with open(self.material, "w") as json_file:
                json.dump(data, json_file, sort_keys=True, indent=4)
            self.deleteLater()

        elif(button.text() == "Cancel"):
            self.deleteLater()


#a = TMaterialPropertyEditor("X:\\Content\\Core\\Materials\\Micro_Rope\\M_Micro_Rope_01.material")
