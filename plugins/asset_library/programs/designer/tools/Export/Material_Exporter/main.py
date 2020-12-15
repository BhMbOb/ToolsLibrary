import sys
import os
import sd

import tools_library.programs.designer as program_designer
import program
import program.instance
import program.export


def get_graph_output_dir(graph):
    """Returns the output directory for the input graph, with respect to the asset library sbs export rules"""
    output = os.path.dirname(graph.getPackage().getFilePath())
    if(os.path.basename(output) == ".source"):
        # if in a .source dir we export intot the upper directory
        output = os.path.dirname(output)
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
    elif(graph_name.lower().startswith("inst_")):
        # "inst_" signifies an instance of another graph
        output = package_name + "_" + graph_name.replace("inst_", "")
    
    return output


def get_package_material_graphs(package):
    output = []
    
    for i in list(package.getChildrenResources(isRecursive=False)):
        if(get_graph_material_name(i) != ""):
            output.append(i)

    return output


def export_graph(graph):
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
                texture_type +
                ".tga"
            )
            node_property_texture.save(os.path.join(graph_output_dir, texture_name))

    print("[Asset Library] Exported material \"" + graph_material_name + "\" to \"" + graph_output_dir + "/\"")


for i in get_package_material_graphs(program.instance.get_current_package()):
    export_graph(i)