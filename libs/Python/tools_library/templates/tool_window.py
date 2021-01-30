import os
import sys
from qtpy import QtWidgets, QtGui, QtCore, uic

from tools_library.utilities import qt as qt_utils


class ToolWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ToolWindow, self).__init__()
        self.ui = None

        if(os.path.isfile(self.uic_path)):
            uic.loadUi(self.uic_path, self)
        else:
            print("Tool UIC File Doesnt Exist: " + self.uic_path)

        # this is to fix the fact we can't automatically parent all windows to the main QApplication
        # results in the same behaviour as WindowStaysOnTopHint but only for the parent program
        QtWidgets.QApplication.instance().focusChanged.connect(self.focus_changed_event)

    def finalize(self):
        self.show()

    def focus_changed_event(self, old, new):
        self.raise_()

    @property
    def uic_path(self):
        """Path to the UIC for this tool window"""
        tool_file_path = sys.modules[self.__class__.__module__].__file__
        return os.path.join(os.path.dirname(tool_file_path), self.__class__.__name__ + ".ui")
