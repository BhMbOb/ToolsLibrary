import sys
from qtpy import QtWidgets


def get_application():
    """Get or create the qapplication instance"""
    output = QtWidgets.QApplication.instance()
    if(not output):
        output = QtWidgets.QApplication(sys.argv)
    return output