import os
import json
import socket

import tools_library
from tools_library.utilities import json as json_utils


def listen_port():
    return json_utils.getProperty(tools_library.getConfig("designer:program.json"), "listen_port")


def send_command(command):
    """Takes a python string command and sends it as a request to the listen server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", listen_port()))
    client.send(str(command).encode("utf-8"))
    client.close()
