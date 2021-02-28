import os
import sys
import json
import sd


import tools_library.designer.graph
import tools_library.designer.package
import tools_library.utilities.pathing as path_utils


def graph_output_dir(graph=None):
    """Attempts to find the Asset Library output directory for a graph\n
    :param <sdsbsgraph:graph> The graph to work with - if None then the currently opened graph\n
    :return <str:dir> The output directory for all material data\n
    """
    graph = tools_library.designer.graph._ensure_graph(graph)
    possible_output_dir = os.path.dirname(graph.getPackage().getFilePath())
    if(os.path.basename(possible_output_dir) == ".source"):
        return os.path.dirname(possible_output_dir)
    return ""

def _get_graph_name_param(graph, param):
    """Extracts a material parameter from a graph name
    :param <sdsbsgraph:graph> The target graph
    :param <str:param> Name of the parameter to get (Ie, inst=01)
    :return <str:name> The parameter value if found, "" if not
    """
    graph_name_split = graph.getIdentifier().split("-")
    for i in graph_name_split:
        if("=" in i):
            this_name = i.split("=")[0].lower()
            this_value = i.split("=")[1]
            if(this_name == param):
                return this_value
    return ""


def get_graph_instance(graph=None):
    """Returns the instance name of an input graph
    :param <sdsbsgraph:graph> The graph to work on - defaults to the current graph
    :return <str:instance> The instance identifier - "" if unsupplied
    """
    graph = tools_library.designer.graph._ensure_graph(graph)
    return _get_graph_name_param(graph, "inst")

def get_graph_variant(graph=None):
    """Returns the variant name of an input graph
    :param <sdsbsgraph:graph> The graph to work on - defaults to the current graph
    :return <str:variant> The variant identifier - "" if unsupplied
    """
    graph = tools_library.designer.graph._ensure_graph(graph)
    return _get_graph_name_param(graph, "var")

def graph_material_name(graph=None):
    """Returns the material name of an Asset Library compliant graph
    :param <sdsbsgraph:graph> Target graph to work on - defaults to the current graph
    :return <str:material_name> The material name
    """
    output = ""
    graph = tools_library.designer.graph._ensure_graph(graph)
    graph_name = graph.getIdentifier().lower()
    package_name = tools_library.designer.package.get_name(package=graph.getPackage())

    if(graph_name.endswith("_abs")):
        # "_abs" = abstract, and should not be exported
        pass
    elif(graph_name == "base"):
        # "base" is the default material and takes only the package name
        output = package_name
    elif(graph_name == "resources"):
        pass
    else:
        name_split = graph_name.split("-")
        inst = get_graph_instance(graph=graph)
        var = get_graph_variant(graph=graph)
        output = package_name
        if(inst != ""):
            output += "_" + inst
            if(var != ""):
                output += "_" + var
    return output

def get_all_material_graphs(package=None):
    """Get a list of all child graphs within a package which are Asset Library compliant\n
    :param <sdsbspackage:package> Target package to work on - if None uses the current package\n
    :return <[sdsbsgraph]:graphs> A graph list containing all Asset Library compliant graphs\n
    """
    output = []
    package = tools_library.designer.package._ensure_package(package)
    all_graphs = tools_library.designer.package.child_graphs(package=package)
    for i in all_graphs:
        if(graph_material_name(i) != ""):
            output.append(i)
    return output

def export_graph(graph):
    """Exports a graph to the Asset Library
    :param <sdsbsgraph:graph> Target graph to export
    """
    exported_textures = {}
    output_dir = graph_output_dir(graph=graph)
    material_name = graph_material_name(graph=graph)
    graph.compute()

    for node in graph.getOutputNodes():
        node_definition = node.getDefinition()
        node_outputs = node_definition.getProperties(
            sd.api.sdproperty.SDPropertyCategory.Output
        )
        node_texture = None
        for node_output in node_outputs:
            prop_value = node.getPropertyValue(node_output)
            prop_texture = prop_value.get()
            node_identifier = node.getIdentifier()
            if(prop_texture):
                node_texture = prop_texture

        if(node_texture):
            texture_type = node.getAnnotationPropertyValueFromId("identifier").get()
            texture_name = "T_{}_{}".format(material_name, texture_type)
            node_texture.save(
                os.path.join(output_dir, texture_name + ".tga")
            )
            exported_textures[texture_type] = texture_name

    if(len(exported_textures) > 0):
        material_path = os.path.join(
            output_dir,
            "M_{}.material".format(material_name)
        )
        if(os.path.isfile(material_path)):
            with open(material_path, "r") as f:
                material_data = json.load(f)
        else:
            material_data = {}
        if("textures" not in material_data):
            material_data["textures"] = {}
        for key in exported_textures:
            material_data["textures"][key] = exported_textures[key]
        if("metadata" not in material_data):
            material_data["metadata"] = {}
        material_data["metadata"]["name"] = path_utils.get_filename_only(
            graph.getPackage().getFilePath()
            )
        material_data["metadata"]["instance"] = get_graph_instance(graph=graph)
        material_data["metadata"]["variant"] = get_graph_variant(graph=graph)
        with open(material_path, "w") as f:
            json.dump(material_data, f, indent=4, sort_keys=True)
    print("[Asset Library] Exportet Material {} to {}".format(
        material_name, output_dir
    ))

def export_package(package=None, export_sbsar=True):
    """Exports all valid Asset Library materials within a package
    :param <sdsbspackage:package> Target package to export - defaults to the current package
    :param <bool:export_sbsar> Should we export the package as an SBSAR too?
    """
    package = tools_library.designer.package._ensure_package(package)
    for i in tools_library.designer.package.child_graphs(package=package):
        if(graph_material_name(i) != ""):
            export_graph(i)

    if(export_sbsar):
        sbsar_exporter_instance = None
        sbsar_exporter_instance = sd.api.sbs.sdsbsarexporter.SDSBSARExporter(
            tools_library.designer.instance.context, sbsar_exporter_instance
        )
        sbsar_exporter_instance = sbsar_exporter_instance.sNew()
        sbsar_exporter_instance.exportPackageToSBSAR(
            package,
            package.getFilePath().replace(".sbs", ".sbsar")
        )
    


