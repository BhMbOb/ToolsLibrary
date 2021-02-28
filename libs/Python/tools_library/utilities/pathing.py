import os


def set_path_file_type(filepath, filetype):
    """Sets the file type on a filepath\n
    :param <str:filepath> The filepath to set on\n
    :param <str:filetype> The new filetype\n
    """
    return (filepath.split(".")[0] + "." + filetype.replace(".", ""))


def remove_file_type(filepath):
    """Remove the file type from a string\n
    :param <str:filepath> The filepath to strip from\n
    :return <str:path> Filepath with type removed\n
    """
    return filepath.rsplit(".", 1)[0]

def get_filename_only(filepath):
    """Strip only the filename out of an input path\n
    :param <str:filepath> The filepath to strip from\n
    :return <str:name> The filename\n
    """
    return os.path.splitext(os.path.basename(filepath))[0]