def set_path_file_type(filepath, filetype):
    """Replace the file type of an input filepath"""
    return (filepath.split(".")[0] + "." + filetype.replace(".", ""))


def remove_file_type(filepath):
    return filepath.rsplit(".", 1)[0]