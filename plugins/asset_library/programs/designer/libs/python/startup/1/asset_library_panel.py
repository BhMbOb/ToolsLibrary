'''
Create and add the Asset Library dock widget to designer
'''
import sd
from PySide2 import QtWidgets
from qtpy import QtWidgets, QtCore, uic

import tools_library.utilities.qt.widgets as QToolsLibraryWidgets

from asset_library_program.tools import material_loader
from asset_library_program.tools import material_exporter


app = sd.getContext().getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

dock = uiMgr.newDockWidget(identifier="asset_library.sd_dock", title="Asset Library")
dock_layout = QToolsLibraryWidgets.QVScrollLayout()
dock.setLayout(dock_layout)


# Material Loader
p = QToolsLibraryWidgets.QCollapsibleWidget(title="<b>MATERIAL LOADER</b>")
dock_layout.addWidget(p)
p.addWidget(material_loader.QMaterialLoader())

# Material Exporter
p = QToolsLibraryWidgets.QCollapsibleWidget(title="<b>MATERIAL EXPORTER</b>")
dock_layout.addWidget(p)
p.addWidget(material_exporter.QMaterialExporter())

dock_layout.addStretch()
