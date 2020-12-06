import os
import json

import tools_library

with open(tools_library.getConfig("tools_library.json")) as j:
    json_data = json.load(j)
    url = json_data["url"]
    os.system("start \"\" " + url)
