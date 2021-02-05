import sys
from qtpy import QtWidgets

import tools_library


def get_application():
    """Get or create the qapplication instance"""
    output = QtWidgets.QApplication.instance()
    if(not output):
        output = QtWidgets.QApplication(sys.argv)
        output.setStyleSheet(open(tools_library.getConfig("styles/standalone.css")).read())
    return output