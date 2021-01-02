"""
Listen server bound to a Qt timer used to recieve commands from external python instances
"""

import socket
import select
import sys

from qtpy import QtWidgets, QtCore

import tools_library.programs.designer
import tools_library.utilities.listen_server


if(QtWidgets.QApplication.instance()):
	listen_port = tools_library.programs.designer.listen_port()
	listen_server = tools_library.utilities.listen_server.ListenServer(listen_port)

	timer_ = QtCore.QTimer()
	timer_.timeout.connect(listen_server.tick)
	timer_.start(20)