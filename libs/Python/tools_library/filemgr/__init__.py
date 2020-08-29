import os


def makedir(path):
    """Creates a folder if it doesn't already exist"""
    if(not os.path.isdir(path)):
        os.makedirs(path)


def makesubdirs(folder_dir, *subdirs):
    """Makes a list of subdirectories within an input directory

    folder_dir - parent folder
    subdirs - names of all subfolders to create
    """
    if(not subdirs):
        makedir(folder_dir)
    if(len(subdirs) == 1):
        if(type(subdirs[0]) == list):
            subdirs = subdirs[0]
    makedir(folder_dir)
    for i in subdirs:
        makedir(os.path.join(folder_dir, i))
