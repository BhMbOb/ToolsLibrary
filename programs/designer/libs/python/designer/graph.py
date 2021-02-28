import os
import sd

from sd.api.sdproperty import SDPropertyCategory

context = sd.getContext()
app = context.getSDApplication()
package_manager = app.getPackageMgr()
ui_manager = app.getQtForPythonUIMgr()


def current():
    """Attempt to find the currently opened designer graph
    :return <sdsbsgraph:graph> The currently opened graph - None no graph is open 
    """
    return ui_manager.getCurrentGraph()

def _ensure_graph(graph):
    """Ensures that we have a package to work on. If the input is None then we default to the current package
    :param <sdsbsgraph:package> Target graph - if None we will return the currently opened graph
    :return <sdsbsgraph:output> Either the input graph or currently opened one
    """
    if(graph is None):
        return current()
    return graph

def graph_selection():
    """Returns the currently selected nodes in the opened graph
    :return <sdarray:nodes> Nodes if there is a valid selection, else an empty array
    """
    return ui_manager.getCurrentGraphSelection()

def graph_name(target=None):
    """Get the name of a graph
    :param <sdsbsgraph:target> Target graph, if None then will default to the currently opened graph
    :return <str:name> Name of the currently opened graph
    """
    if(target is None):
        target = current()
    if(target is not None):
        return target.getPropertyValueFromId("identifier", SDPropertyCategory.Annotation).get()
    return ""
        
