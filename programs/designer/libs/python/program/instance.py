import os
import sd


context = sd.getContext()
application = context.getSDApplication()
package_manager = application.getPackageMgr()
ui_manager = application.getQtForPythonUIMgr()


def get_current_graph():
    return ui_manager.getCurrentGraph()


def get_current_graph_selection():
    return ui_manager.getCurrentGraphSelection()


def get_current_package():
    if(get_current_graph()):
        return get_current_graph().getPackage()
    None


def get_current_package_path():
    if(get_current_package()):
        return get_current_package().getFilePath()
    return None


def get_package_name(package):
    if(package):
        return os.path.basename(package.getFilePath()).split(".")[0]
    return ""


def get_current_package_name():
    if(get_current_package_path()):
        return os.path.basename(get_current_package_path()).split(".")[0]
    return ""
