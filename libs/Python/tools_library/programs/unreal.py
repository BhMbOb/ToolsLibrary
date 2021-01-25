import os
import socket

import tools_library
from tools_library.utilities import json as json_utils
from tools_library.utilities import listen_server


def unreal_project_path():
    """Returns the path to the current unreal project directory"""
    return json_utils.get_property(tools_library.getConfig("client_settings.json"), "programs.unreal.project_dir")


def listen_port():
    """Returns the server port that the unreal listen server is hosted on"""
    return json_utils.get_property(tools_library.getConfig("Unreal:program.json"), "listen_port")


def unreal_uproject_path():
    """Returns the path to the current unreal project .uproject file"""
    upp = unreal_project_path()
    return os.path.join(upp, os.path.basename(upp) + ".uproject")


def launch_unreal_project():
    """Launch the current unreal project standalone"""
    print(unreal_uproject_path())
    os.system("start " + unreal_uproject_path())


def is_open():
    """Check if the program is open by testing if the listen server is hosted"""
    return not listen_server.is_free(listen_port())


def send_command(command):
    """Takes a python string command and sends it as a request to the listen server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", listen_port()))
    client.send(str(command).encode("utf-8"))
    client.close()
