import os
import sd

import tools_library.utilities.pathing as path_utils

context = sd.getContext()
application = context.getSDApplication()
package_manager = application.getPackageMgr()
ui_manager = application.getQtForPythonUIMgr()


def current():
    """Attempt to find the currently opened designer package
    :return <sdsbspackage:package> The currently opened package - None if no package is open
    """
    current_graph = ui_manager.getCurrentGraph()
    if(current_graph):
        return current_graph.getPackage()
    return None

def _ensure_package(package):
    """Ensures that we have a package to work on. If the input is None then we default to the current package
    :param <sdsbspackage:package> Target package - if None we will return the currently opened package
    :return <sdsbspackage:output> Either the input package or currently opened one
    """
    if(package is None):
        return current()
    return package

def get_path(package=None):
    """Returns the file path to an input package
    :param <sdsbspackage:package> The package to get the path for - if None we use the current package
    """
    package = _ensure_package(package)
    if(package is not None):
        return package.getFilePath()
    return None

def get_name(package=None):
    """Returns the name of a package
    :param <sdsbspackage:package> The package to get the name of - if None we use the current package
    """
    package = _ensure_package(package)
    if(package is not None):
        return path_utils.get_filename_only(get_path(package=package))
    return ""

def load(sbs_path):
    """Loads an SBS from its path
    :param <str:sbs_path> Absolute path to the SBS file
    """
    if((os.path.isfile(sbs_path)) and (sbs_path.endswith(".sbs"))):
        sd_package = package_manager.loadUserPackage(
            sbs_path.replace("\\", "/"),
            True,
            True
        )
        return sd_package
    return None

def child_graphs(package=None):
    """Gets all of the child graphs from a package
    :param <sdsbspackage:package> Target package - if None then defaults to the current graph
    :return <[sdsbsgraph]:graphs> List of all child graphs
    """
    output = []
    package = _ensure_package(package)
    if(package is not None):
        for i in list(package.getChildrenResources(isRecursive=False)):
            output.append(i)
    return output

def show_in_explorer(package=None):
    """Takes an input package and opens the export directory in explorer
    :param <sdsbspackage:package> The package to show - if None the current package is used
    """
    package = _ensure_package(package)
    if(package):
        path = get_path(package)
        if(os.path.isfile(path)):
            os.startfile(os.path.dirname(path) + "\\..\\")
