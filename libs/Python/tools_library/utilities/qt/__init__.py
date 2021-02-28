import sys
from qtpy import QtWidgets

import tools_library


def get_application():
    """Returns the QApplication instance - creates it if it has not been initialized
    :return <QApplication:out> The QApplication instance"""
    output = QtWidgets.QApplication.instance()
    if(not output):
        output = QtWidgets.QApplication(sys.argv)
        output.setStyleSheet(open(tools_library.get_config("styles/standalone.css")).read())
    return output