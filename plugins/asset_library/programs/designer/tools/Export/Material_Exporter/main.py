import sys
import os
import json
import sd

import tools_library.programs.designer as program_designer
import tools_library.filemgr
import program
import program.instance


def get_graph_output_dir(graph):
    """Returns the output directory for the input graph, with respect to the asset library sbs export rules"""
    output = os.path.dirname(graph.getPackage().getFilePath())
    if(os.path.basename(output) == ".source"):
        # if in a .source dir we export intot the upper directory
        output = os.path.dirname(output)
    return output


def get_graph_name_parameter(graph, parameter_name):
    """Extracts a material name parameter from a graphs name (Ie, inst=01)"""
    output = ""
    graph_name = graph.getIdentifier()
    graph_name_split = graph_name.split("-")
    for name_split_value in graph_name_split:
        if("=" in name_split_value):
            this_parameter_name = name_split_value.split("=")[0].lower()
            this_parameter_value = name_split_value.split("=")[1]
            if(this_parameter_name == parameter_name):
                output = this_parameter_value
    return output


def get_graph_material_name(graph):
    """Returns the final asset library legal name for an input graph"""
    output = ""
    graph_name = graph.getIdentifier()
    package_name = program.instance.get_package_name(graph.getPackage())

    if(graph_name.lower().endswith("_abs")):
        # if a graph ends with "_abs" it's considered abstract and should not be exported
        pass
    elif(graph_name.lower() == "base"):
        # if a graph is named "base" then it simply takes the package name
        output = package_name
    elif(graph_name.lower() == "resources"):
        pass
    else:
        name_split = graph_name.lower().split("-")
        instance_identifier = get_graph_name_parameter(graph, "inst")
        variant_identifier = get_graph_name_parameter(graph, "var")

        output = package_name
        if(instance_identifier != ""):
            output += "_" + instance_identifier
            if(variant_identifier != ""):
                output += "_" + variant_identifier
    
    return output


def get_package_material_graphs(package):
    """Returns all of the child graphs in a package which are set up to be validly exportable materials"""
    output = []
    
    for i in list(package.getChildrenResources(isRecursive=False)):
        if(get_graph_material_name(i) != ""):
            output.append(i)

    return output


def export_graph(graph, create_material=True):
    """Export a material graphs textures to the asset library"""
    exported_textures = {}

    graph_output_dir = get_graph_output_dir(graph)
    graph_material_name = get_graph_material_name(graph)

    graph.compute()

    for node in graph.getOutputNodes():
        node_definition = node.getDefinition()
        node_output_properties = node_definition.getProperties(sd.api.sdproperty.SDPropertyCategory.Output)

        node_property_texture = None
        for node_output_property in node_output_properties:
            property_value = node.getPropertyValue(node_output_property)
            property_texture = property_value.get()
            node_identifier = node.getIdentifier()
            if(property_texture):
                node_property_texture = property_texture

        if(node_property_texture):
            texture_type = node.getAnnotationPropertyValueFromId("identifier").get()
            texture_name = str(
                "T_" +
                graph_material_name + 
                "_" +
                texture_type
            )
            node_property_texture.save(os.path.join(graph_output_dir, texture_name + ".tga"))
            exported_textures[texture_type] = texture_name

    if(len(exported_textures) > 0):
        if(create_material):
            material_path = os.path.join(graph_output_dir, "M_" + graph_material_name + ".material")
            material_data = {}

            if(os.path.isfile(material_path)):
                with open(material_path, "r") as f:
                    material_data = json.load(f)

            # add textures
            if(material_data.get("textures") is None):
                material_data["textures"] = {}

            for key in exported_textures:
                material_data["textures"][key] = exported_textures[key]

            # add metadata
            if(material_data.get("metadata") is None):
                material_data["metadata"] = {}

            material_data["metadata"]["name"] = tools_library.filemgr.filename(graph.getPackage().getFilePath())
            material_data["metadata"]["instance"] = get_graph_name_parameter(graph, "inst")
            material_data["metadata"]["variant"] = get_graph_name_parameter(graph, "var")

            with open(material_path, "w") as f:
                json.dump(material_data, f, indent=4, sort_keys=True)

    print("[Asset Library] Exported material \"" + graph_material_name + "\" to \"" + graph_output_dir + "/\"")


for i in get_package_material_graphs(program.instance.get_current_package()):
    export_graph(i)

# export the current package as a .sbsar
sbsar_exporter_instance = None
sbsar_exporter_instance = sd.api.sbs.sdsbsarexporter.SDSBSARExporter(program.instance.context, sbsar_exporter_instance)
sbsar_exporter_instance = sbsar_exporter_instance.sNew()
sbsar_exporter_instance.exportPackageToSBSAR(
    program.instance.get_current_package(),
    program.instance.get_current_package().getFilePath().replace(".sbs", ".sbsar")
)