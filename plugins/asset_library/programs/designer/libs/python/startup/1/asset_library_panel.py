'''
Create and add the Asset Library dock widget to designer
'''
import sd
from PySide2 import QtWidgets
from qtpy import QtWidgets, QtCore, uic

import tools_library.utilities.qt.widgets as QToolsLibraryWidgets

from asset_library.designer.tools import material_loader
from asset_library.designer.tools import material_exporter
from asset_library.designer.tools import material_properties
from asset_library.tools import material_property_editor


app = sd.getContext().getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

dock = uiMgr.newDockWidget(identifier="asset_library.sd_dock", title="Asset Library")
dock_layout = QToolsLibraryWidgets.QVScrollLayout()
dock.setLayout(dock_layout)


target_dock_tool_classes = {
    "Material Loader": material_loader.TMaterialLoader,
    "Material Exporter": material_exporter.TMaterialExporter,
    "Material Properties": material_properties.TMaterialProperties
}

for i in target_dock_tool_classes:
    p = QToolsLibraryWidgets.QCollapsibleWidget(title=("<b>" + i.upper() + "</b>"))
    dock_layout.addWidget(p)
    p.addWidget(target_dock_tool_classes[i]())

dock_layout.addStretch()
