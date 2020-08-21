import json

from tools_library import asset_library


class Asset(object):
    """"""
    def __init__(self, asset_path):

        # if the asset_path is formatted "content_library:path/to/the/asset.asset" then extract, else use "Common" by default
        self.content_library = asset_path.split(":")[0] if (len(asset_path.split(":")) > 1) else "Common"

        # if the asset_path is formatted "asset_library:path/to/the/asset.asset" then extract, else use asset_path
        self.base_path = asset_path.split(":")[1] if (len(asset_path.split(":")) > 1) else asset_path

    def path(self, relative=True):
        """"""
        output = self.content_library + ":" + self.base_path

        if(not relative):
            output = asset_library.actualPath(output)

        return output
        
    def get_property(self, property_name):
        output = None

        property_hierachy = property_name.split(".")

        print(property_hierachy)

        with open(self.path(relative=False)) as j:
            json_data = json.load(j)

            key_string = ""
            for i in property_hierachy:
                key_string += "[\"" + i + "\"]"

            try:
                output = eval("json_data" + key_string)
            except:
                print("Key Not Found: " + key_string)

        return output
