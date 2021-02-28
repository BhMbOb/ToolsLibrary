import os
import socket

import tools_library
from tools_library.utilities import json as json_utils
from tools_library.utilities import listen_server


def unreal_project_path():
    """Returns the path to the current unreal project .uproject\n
    :return <str:path> Path to the .uproject\n
    """
    return json_utils.get_property(tools_library.get_config("client_settings.json"), "programs.ue4.project_path").lower()

def unreal_project_dir():
    """Returns the path to the current unreal project directory\n
    :return <str:dir> Directory path to the unreal project (the directory containing the .uproject file)\n
    """
    return os.path.dirname(unreal_project_path()).lower()


def listen_port():
    """Returns the server port that the unreal listen server is hosted on\n
    :return <int:port> The port to the unreal listen server\n
    """
    return json_utils.get_property(tools_library.get_config("Ue4:program.json"), "listen_port")


def launch_unreal_project():
    """Launch the current unreal project standalone"""
    os.system("start " + unreal_project_path())


def is_open():
    """Check if the program is open by testing if the listen server is hosted
    :return <bool:open> True if the project is open, false if not
    """
    return not listen_server.is_free(listen_port())


def send_command(command):
    """Takes a python string command and sends it as a request to the listen server\n
    :param <str:command> Python command to run\n
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", listen_port()))
    client.send(str(command).encode("utf-8"))
    client.close()
