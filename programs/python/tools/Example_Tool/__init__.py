import os
import json
from qtpy import QtWidgets, QtCore, uic, QtGui

import tools_library
from tools_library.types import _tool_window
import tools_library.utilities.qt


class TExampleTool(_tool_window.ToolWindow):
    def __init__(self):
        super(TExampleTool, self).__init__()
        self.finalize()


if __name__ == "__main__":
    TExampleTool()