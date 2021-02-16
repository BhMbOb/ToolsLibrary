"""
Library containing filesystem based functions
"""
import os

from qtpy import QtWidgets


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


def filename(path):
    """Returns the filename part of an input path - also removes the filetype"""
    return os.path.basename(path).split(".")[0]


def filetype(path):
    """Returns the filetype part of an input path"""
    filename = os.path.basename(path)
    if("." in filename):
        return filename.split(".")[1]
    return ""


def pick_file(title="Pick File..", start="C:\\", file_types=""):
    """Pick a file from a dialog"""
    file_dialog = QtWidgets.QFileDialog()
    open_file = file_dialog.getOpenFileName(
        None,
        title,
        start,
        file_types
    )[0]
    return open_file


def symlink(src, dest):
    """Create a symlink"""
    try:
        makedir(os.path.dirname(dest))

        if(os.path.isdir(src)):
            if(os.path.islink(dest)):
                os.unlink(dest)
            os.symlink(
                os.path.realpath(src),
                os.path.realpath(dest),
                target_is_directory=True
            )
    except OSError as error:
        if(os.path.isdir(dest)):
            print("[Tools Library][Symlink] Warning: Destination directory already exists!")
        elif(not os.path.isdir(src)):
            print("[Tools Library][Symlink] Warning: Source directory does not exist!")
        else:
            print("[Tools Library][Symlink] Error: Symlink failed!")
            print(error)
    else:
        print("[Tools Library][Symlink] Success: " + dest)
