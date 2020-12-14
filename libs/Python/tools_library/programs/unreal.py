import os
import json
import socket

import tools_library
from tools_library.utilities import json as json_utils


def unreal_project_path():
    return json_utils.getProperty(tools_library.getConfig("unreal:active_project.json"), "path")


def listen_port():
    return json_utils.getProperty(tools_library.getConfig("unreal:active_project.json"), "listen_port")


def unreal_uproject_path():
    upp = unreal_project_path()
    return os.path.join(upp, os.path.basename(upp) + ".uproject")


def launch_unreal_project():
    print(unreal_uproject_path())
    os.system("start " + unreal_uproject_path())


def send_command(command):
    """Takes a python string command and sends it as a request to the listen server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", listen_port()))
    client.send(str(command).encode("utf-8"))
    client.close()