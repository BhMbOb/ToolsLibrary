import os
from qtpy import QtWidgets, QtCore, uic, QtGui

import tools_library
from tools_library.templates import tool_window

import asset_library


class TMaterialPropertyEditor(tool_window.ToolWindow):
    def __init__(self):
        super(TMaterialPropertyEditor, self).__init__()
        self.finalize()


if __name__ == "__main__":
    app = tools_library.utilities.qt.get_application()
    a = TMaterialPropertyEditor()
    app.exec_()