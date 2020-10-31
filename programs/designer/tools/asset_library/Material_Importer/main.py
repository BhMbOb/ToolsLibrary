'''
 Material Importer

    - Import from .sbsar, .sbs, .material, texture
    Looks for a matching .sbs from the filename / path

    - Import from textures
    Generate a .sbs source file

    - Import from .material
    Generate a .sbs source file
'''

#TODO: UPDATE ME

from PySide2 import QtWidgets
import sys, os

import sd

#
from tools_library import materials




sd_context = sd.getContext()
sd_app = sd_context.getSDApplication()
sd_packagemgr = sd_app.getPackageMgr()


# Load an SBS from a filepath
def LoadSBS(path):
    if( (os.path.isfile(path)) and (path.endswith(".sbs")) ):
        sd_packagemgr.loadUserPackage(path)


# Pick either a .material, .sbs, .sbsar .tga file to attempt to load
def GetOpenFileName_Material():
    file_dialog = QtWidgets.QFileDialog()

    open_file = file_dialog.getOpenFileName(
        None,
        "Import Material",
        "X:/Assets",
        "Material Files(*.material *.sbsar *.sbs *.tga)"
    )[0]

    return open_file

# removes the "_TYPE" identifier from the end of a texture string
def RemoveTextureType(texture_path):
    output = texture_path

    #TODO: Add this to a common known textures.types table
    known_types = ["D", "DA", "S", "N", "M", "T"]
    
    for suffix in known_types:
        output = output.replace( "_" + suffix + ".", "." )

    return output

# removes the "_index" identifier from the end of a texture string
def RemoveTextureIndex(texture_path):
    output = texture_path

    for i in range(0, 99):
        index = str(i) if (i >= 10) else ( "0" + str(i) )

        output = output.replace( "_" + index, "")

    return output
        


# Attempt to find an SBS file from another path
def GetSBSFilePathFromFile(path):
    output = None
    path = RemoveTextureType(path)
    path = RemoveTextureIndex(path)

    # If path is .sbs and exists then output is found
    if( (path.endswith(".sbs")) and (os.path.isfile(path)) ):
        return path

    # Try - guess sbs from a texture
    elif(path.endswith(".tga")):
        pass

    # Try - guess sbs from .material
    elif(path.endswith(".material")):
        pass

    # Try - guess sbs from sbsar
    elif(path.endswith(".sbsar")):
        sbs_from_sbsar = path.replace(".sbsar", ".sbs")
        if(os.path.isfile(sbs_from_sbsar)):
            output = sbs_from_sbsar

    # Secondary checks
    if(output == None):

        # Force replace file extension with ".sbs"
        replace_sbs = path.rsplit(".", 1)[0]
        if(os.path.isfile(replace_sbs)):
            output = replace_sbs

        # Remove texture extensions and go into _source folder
        #...

    return output

# Returns a list of textures used in a material from an input texture path
def GetTexturesFromFile(path):
    pass

# 
def LoadAsset_Material():
    material_file_context = GetOpenFileName_Material()

    if(os.path.isfile(material_file_context)):

        sbs_source_filepath = GetSBSFilePathFromFile(material_file_context)

        if(sbs_source_filepath != None):
            LoadSBS(sbs_source_filepath)

LoadAsset_Material()