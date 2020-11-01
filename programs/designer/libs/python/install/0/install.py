import os
import json
import shutil
import xml.etree.ElementTree

import tools_library


config_project_path = tools_library.finalizeString("$(LocalAppdata)Allegorithmic\\Substance Designer\\default_configuration.sbscfg")


def add_tools_library_sbsprj():
    """Adds the tools library sbsprj to the designer config"""
    tools_library_sbsprj = tools_library.getConfig("Designer:tools_library.sbsprj")

    sbsprj_set = False

    xml_config_tree = xml.etree.ElementTree.parse(config_project_path)
    xml_config_root = xml_config_tree.getroot()

    xml_config_plugins_size = xml_config_root.find("./projects/projectfiles/size")
    xml_config_projects = xml_config_root.findall(".//*path")
    num_projects = int(xml_config_plugins_size.text)

    for xml_config_project in list(xml_config_projects):
        if(tools_library_sbsprj.replace("\\", "/") in xml_config_project.text):
            sbsprj_set = True

    if(not sbsprj_set):
        xml_config_plugins_size.text = str(num_projects + 1)
        xml_config_projects_root = xml_config_root.find("./projects/projectfiles")
        xml_config_project = xml.etree.ElementTree.SubElement(xml_config_projects_root, "_" + str(num_projects + 1))
        xml_config_project.set("prefix", "_")
        xml_config_project_path = xml.etree.ElementTree.SubElement(xml_config_project, "path")
        xml_config_project_path.text = tools_library_sbsprj.replace("\\", "/")

    with open(config_project_path, "w+") as f:
        f.write(xml.etree.ElementTree.tostring(xml_config_root, encoding="unicode", method="xml"))


add_tools_library_sbsprj()
