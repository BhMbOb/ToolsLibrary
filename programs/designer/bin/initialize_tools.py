import os
import json
import shutil
import xml.etree.ElementTree

import tools_library

default_sbsprj_path = tools_library.getConfig("Designer:project_template.sbsprj")

all_sbsprj = {}


# loop over all designer asset libraries and create a .sbsprj file
shelves_path = tools_library.finalizeString("$(AssetLibraryPath)Shelves\\Designer")
for i in os.listdir(shelves_path):
    shelf_path = os.path.join(shelves_path, i)
    if(os.path.isdir(shelf_path)):
        shelf_name = "tl_" + i
        
        config_file_path = os.path.join(shelf_path, "config", shelf_name + ".sbsprj")

        if(not os.path.isdir(os.path.dirname(config_file_path))):
            os.makedirs(os.path.dirname(config_file_path))

        fin = open(default_sbsprj_path)
        fout = open(config_file_path, "wt")
        for line in fin:
            line = line.replace("$(SHELF_PATH)", shelf_path)
            line = line.replace("\\\\", "/")
            line = line.replace("\\", "/")
            fout.write(line)
        fin.close()
        fout.close()

        all_sbsprj[shelf_name] = shelf_path       

'''with open(tools_library.getConfig("asset_library\\shelf_libraries.json")) as j:
    json_data = json.load(j)

    for i in json_data:
        if(json_data[i]["type"] == "Designer"):
            shelf_path = tools_library.finalizeString(json_data[i]["path"])
            shelf_name = json_data[i]["name"]

            config_file_path = os.path.join(shelf_path, "config", shelf_name + ".sbsprj")

            if(not os.path.isdir(os.path.dirname(config_file_path))):
                os.makedirs(os.path.dirname(config_file_path))

            fin = open(default_sbsprj_path)
            fout = open(config_file_path, "wt")
            for line in fin:
                line = line.replace("$(SHELF_PATH)", shelf_path)
                line = line.replace("\\\\", "/")
                line = line.replace("\\", "/")
                fout.write(line)
            fin.close()
            fout.close()

            all_sbsprj[shelf_name] = shelf_path'''


# loop over all designer asset libraries and add them to the designer parent xml
config_project_path = tools_library.finalizeString("$(LocalAppdata)Allegorithmic\\Substance Designer\\default_configuration.sbscfg")


def add_project(name, path):
    """"""
    path = path + "\\" + name + ".sbsprj"

    if(os.path.exists(config_project_path)):
        already_exists = False

        xml_tree = xml.etree.ElementTree.parse(config_project_path)
        xml_root = xml_tree.getroot()

        xml_key_size = xml_root.find("./projects/projectfiles/size")
        num_projects = int(xml_key_size.text)

        xml_projects = xml_root.findall(".//*path")

        for i in xml_projects:
            if(path.replace("\\", "/") in i.text):
                already_exists = True

        if(not already_exists):
            xml_key_size.text = str(num_projects+1)
            xml_projects_root = xml_root.find("./projects/projectfiles")
            xml_project = xml.etree.ElementTree.SubElement(xml_projects_root, "_" + str(num_projects+1))
            xml_project.set("prefix", "_")
            xml_project_path = xml.etree.ElementTree.SubElement(xml_project, "path")
            xml_project_path.text = path.replace("\\", "/")

        with open(config_project_path, "w+") as f:
            f.write(xml.etree.ElementTree.tostring(xml_root, encoding="unicode", method="xml"))


for i in all_sbsprj:
    add_project(i, all_sbsprj[i])
