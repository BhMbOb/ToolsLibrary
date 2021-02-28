"""
Library containing filesystem based functions
"""
import os

from qtpy import QtWidgets


def makedir(path):
    """Creates a folder if it doesn't already exist\n
    :param <str:path> The path of the directory to make\n
    """
    if(not os.path.isdir(path)):
        os.makedirs(path)


def makesubdirs(folder_dir, *subdirs):
    """Makes a list of subdirectories inside an input directory\n
    :param <str:folder_dir> The parent directory\n
    :param <[str]:subdirs> Names of the child subdirectories to create\n
    """
    if(not subdirs):
        makedir(folder_dir)
    if(len(subdirs) == 1):
        if(type(subdirs[0]) == list):
            subdirs = subdirs[0]
    makedir(folder_dir)
    for i in subdirs:
        makedir(os.path.join(folder_dir, i))


def pick_file(title="Pick File..", start="C:\\", file_types=""):
    """Open a basic Qt based file picker dialog\n
    :param <str:title> Title of the file picker window\n
    :param <str:start> Starting directory of the file picker\n
    :param <str:file_types> Standard windows file type constructor (Ie, "Text Files (*.txt), *.txt"\n
    :return <str:path> The path to the picked file\n
    """
    file_dialog = QtWidgets.QFileDialog()
    open_file = file_dialog.getOpenFileName(
        None,
        title,
        start,
        file_types
    )[0]
    return open_file


def symlink(src, dest):
    """Create a symlink between 2 paths\n
    :param <str:src> Source file path\n
    :param <str:dest> Destination file path\n
    """
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
