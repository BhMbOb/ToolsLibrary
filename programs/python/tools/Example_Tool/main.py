import sys
import os
import tools_library

from qtpy import QtWidgets, uic
from qtpy.QtWidgets import QApplication, QWidget
from qtpy.QtCore import QTimer
import libs.example
import ui.example_ui

app = QtWidgets.QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Example Window!")
window.show()


def example():
    print("oklokok")

t = QTimer()
t.timeout.connect(example)
t.start(100)

uic.loadUi(os.path.dirname(__file__) + "\\example_ui.ui")

if __name__ == "__main__":
    app.exec_()