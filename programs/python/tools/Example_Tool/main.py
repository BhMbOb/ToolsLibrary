import sys
import tools_library
from PySide2 import QtWidgets
from PySide2.QtUiTools import loadUiType
from PySide2.QtWidgets import QApplication, QWidget
import libs.example
import ui.example_ui

app = QtWidgets.QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Example Window!")
window.show()

if __name__ == "__main__":
    app.exec_()