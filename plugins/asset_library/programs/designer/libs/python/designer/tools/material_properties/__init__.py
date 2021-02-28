import os
import json
from qtpy import QtWidgets, QtCore, uic, QtGui
from sd.api.sdproperty import SDPropertyCategory

import tools_library
from tools_library.types import _tool_window
import tools_library.designer.instance

import asset_library
import asset_library.framework.asset_types.material


class TMaterialProperties(_tool_window.ToolWindow):
    def __init__(self):
        super(TMaterialProperties, self).__init__()

        self.q_btn_test.clicked.connect(self.update_material)

    def update_material(self, material_name):
        current_graph = tools_library.designer.instance.get_current_graph()
        name = current_graph.getPropertyValueFromId("identifier", SDPropertyCategory.Annotation).get()


if __name__ == "__main__":
    win = TMaterialProperties()

'''
import tools_library.designer as designer
import tools_library.designer.instance as instance

from sd.api.sdproperty import SDPropertyCategory

current_graph =  instance.get_current_graph()
annotation_props = current_graph.getProperties(SDPropertyCategory.Annotation)

print(current_graph.getPropertyValueFromId("identifier", SDPropertyCategory.Annotation).get())
'''