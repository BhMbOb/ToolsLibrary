import sys
import qtpy
from qtpy import QtWidgets


#app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.show()
combo = QtWidgets.QComboBox()
combo.addItem("a")

layout = QtWidgets.QHBoxLayout()
window.setLayout(layout)
layout.addWidget(combo)

#app.exec()
#print("done")