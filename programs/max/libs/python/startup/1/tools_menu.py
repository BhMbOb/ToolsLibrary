import os
import sys
import pymxs
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets
import qtmax

import tools_library
import tools_library.utilities.string as string_utils

TOOLBAR = qtmax.GetQMaxMainWindow()

max_path = os.path.join(tools_library.path(), "programs\\designer")
max_tools_path = os.path.join(max_path, "tools\\")

#
branch_menus = {}


q_menu = QtWidgets.QMenu("Tools Library", None)
q_menu.setObjectName("Tools Library")
TOOLBAR.menuBar().addMenu(q_menu)

print("okj")