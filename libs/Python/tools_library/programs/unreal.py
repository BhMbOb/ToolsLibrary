import os
import socket

import tools_library
from tools_library.utilities import json as json_utils
from tools_library.utilities import listen_server


def unreal_project_path():
    """Returns the path to the current unreal project .uproject"""
    return json_utils.get_property(tools_library.getConfig("client_settings.json"), "programs.unreal.project_path")

def unreal_project_dir():
    """Returns the path to the current unreal project directory"""
    return os.path.dirname(unreal_project_path())


def listen_port():
    """Returns the server port that the unreal listen server is hosted on"""
    return json_utils.get_property(tools_library.getConfig("Unreal:program.json"), "listen_port")


def launch_unreal_project():
    """Launch the current unreal project standalone"""
    os.system("start " + unreal_project_path())


def is_open():
    """Check if the program is open by testing if the listen server is hosted"""
    return not listen_server.is_free(listen_port())


def send_command(command):
    """Takes a python string command and sends it as a request to the listen server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", listen_port()))
    client.send(str(command).encode("utf-8"))
    client.close()
