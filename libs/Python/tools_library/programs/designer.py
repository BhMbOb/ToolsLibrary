import os
import json
import socket
import xml.etree.ElementTree

import tools_library
from tools_library.utilities import json as json_utils
from tools_library.utilities import listen_server


def listen_port():
    """Returns the port the designer listen server is hosted on"""
    return json_utils.get_property(tools_library.getConfig("designer:program.json"), "listen_port")


def send_command(command):
    """Takes a python string command and sends it as a request to the listen server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", listen_port()))
    client.send(str(command).encode("utf-8"))
    client.close()


def is_open():
    """Check if the program is open by testing if the listen server is hosted"""
    return not listen_server.is_free(listen_port())


def add_sbsprj(sbsprj_path):
    """Adds a new sbsprj to the designer library"""
    if(os.path.isfile(sbsprj_path)):
        sbsprj_set = False
        designer_project_config_path = tools_library.finalizeString("$(LocalAppdata)\\Allegorithmic\\Substance Designer\\default_configuration.sbscfg")
        xml_config_tree = xml.etree.ElementTree.parse(designer_project_config_path)
        xml_config_root = xml_config_tree.getroot()
        
        xml_config_plugins_size = xml_config_root.find("./projects/projectfiles/size")
        xml_config_projects = xml_config_root.findall(".//*path")
        num_projects = int(xml_config_plugins_size.text)

        for xml_config_project in list(xml_config_projects):
            if(sbsprj_path.replace("\\", "/") in xml_config_project.text):
                sbsprj_set = True

        if(not sbsprj_set):
            xml_config_plugins_size.text = str(num_projects + 1)
            xml_config_projects_root = xml_config_root.find("./projects/projectfiles")
            xml_config_project = xml.etree.ElementTree.SubElement(xml_config_projects_root, "_" + str(num_projects + 1))
            xml_config_project.set("prefix", "_")
            xml_config_project_path = xml.etree.ElementTree.SubElement(xml_config_project, "path")
            xml_config_project_path.text = sbsprj_path.replace("\\","/")

        with open(designer_project_config_path, "w+") as f:
            f.write(xml.etree.ElementTree.tostring(xml_config_root, encoding="unicode", method="xml"))