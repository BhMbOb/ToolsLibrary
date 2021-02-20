import os
import sys
import inspect
from qtpy import QtWidgets, QtGui, QtCore, uic

import tools_library
from tools_library.utilities import qt as qt_utils


class ToolWindow(QtWidgets.QWidget):
    def __init__(self):
        self.standalone = tools_library.program_context() == "python"
        if(self.standalone):
            self.app = qt_utils.get_application()

        super(ToolWindow, self).__init__()

        self.ui = None

        # Path to the UIC for this tool window
        try:
            tool_file_path = sys.modules[self.__class__.__module__].__file__
            self.__class__.__file__ = tool_file_path
        except:
            tool_file_path = tools_library.current_tool_path
            self.__class__.__file__ = tool_file_path
        self.uic_path = os.path.join(os.path.dirname(tool_file_path), self.__class__.__name__ + ".ui")
    
        if(os.path.isfile(self.uic_path)):
            uic.loadUi(self.uic_path, self)
        else:
            print("Tool UIC File Doesnt Exist: " + self.uic_path)

        # this is to fix the fact we can't automatically parent all windows to the main QApplication
        # results in the same behaviour as WindowStaysOnTopHint but only for the parent program
        qt_utils.get_application().focusChanged.connect(self.focus_changed_event)

    def finalize(self):
        self.show()

        if(self.standalone):
            self.app.exec_()

    def focus_changed_event(self, old, new):
        self.raise_()
