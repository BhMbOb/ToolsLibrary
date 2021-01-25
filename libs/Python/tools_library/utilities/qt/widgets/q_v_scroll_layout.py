'''
A scrollable version of QVBoxLayout
'''
from qtpy import QtWidgets, QtCore, uic, QtGui


class QVScrollLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        super(QVScrollLayout, self).__init__()
        self.setMargin(0)
        self.setSpacing(0)
        
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_widget.setLayout(self.main_layout)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(self.main_widget)
        self.scroll_area.setWidgetResizable(True)

        self.addWidget(self.scroll_area, outer_layout=True)

    def addWidget(self, wgt, outer_layout=False):
        if(outer_layout):
            super(QVScrollLayout, self).addWidget(wgt)
        else:
            self.main_layout.addWidget(wgt)

    def addStretch(self, outer_layout=False):
        if(outer_layout):
            super(QVScrollLayout, self).addStretch()
        else:
            self.main_layout.addStretch()