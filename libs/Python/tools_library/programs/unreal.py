import os
import json

import tools_library


def unreal_project_path():
    output = ""
    active_project_config_path = os.path.join(tools_library.path(), "programs\\unreal\\config\\active_project.json")
    with open(active_project_config_path) as j:
        json_data = json.load(j)
        output = json_data["path"]
    return output


def unreal_uproject_path():
    upp = unreal_project_path()
    return os.path.join(upp, os.path.basename(upp) + ".uproject")


def launch_unreal_project():
    print(unreal_uproject_path())
    os.system("start " + unreal_uproject_path())