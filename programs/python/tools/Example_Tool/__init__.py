import os
import json
from qtpy import QtWidgets, QtCore, uic, QtGui

import tools_library
from tools_library.templates import tool_window
import tools_library.utilities.qt


class TExampleTool(tool_window.ToolWindow):
    def __init__(self):
        super(TExampleTool, self).__init__()
        self.finalize()


if __name__ == "__main__":
    TExampleTool()
    #tool_window.run_standalone(TExampleTool)