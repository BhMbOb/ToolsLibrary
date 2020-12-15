import sys
import os
import sd
from sd.tools import export

import tools_library.programs.designer as program_designer
import program
import program.instance
import program.export



def export_graph(
        graph,
        output_dir = '',
        file_ext = 'tga'):
    """
    Export the textures of the output node of the specified sSDGraph
    :param graph: The graph that contains the outputs to export
    :param output_dir: The output directory used to save the output's images
    :return: True if succeed else False
    """
    if not graph :
        return False

    if not issubclass(type(graph), sdsbscompgraph.SDSBSCompGraph):
        return False

    # Compute the SDSBSCompGraph so that all node's textures are computed
    graph.compute()

    # Get some information on the graph
    packageName = os.path.basename(graph.getPackage().getFilePath()).split(".")[0]
    graphIdentifier = graph.getIdentifier()

    # Iterate on nodes
    nodeIndex = -1
    for sdNode in graph.getOutputNodes():
        nodeIndex = nodeIndex + 1

        nodeDefinition = sdNode.getDefinition()
        outputProperties = nodeDefinition.getProperties(sdproperty.SDPropertyCategory.Output)
        for outputProperty in outputProperties:
            # Get the property value
            propertyValue = sdNode.getPropertyValue(outputProperty)
            identifier = sdNode.getIdentifier()

            # Get the property value as texture
            propertyTexture = propertyValue.get()
            if not propertyTexture:
                continue

            # Save the texture on disk
            fileExt = file_ext
            fileName = str(
                packageName +
                "_" +
                graphIdentifier +
                "_" +
                identifier +
                '.'+
                fileExt
            )
            textureFileName = os.path.abspath(os.path.join(output_dir, fileName))

            try:
                propertyTexture.save(textureFileName)
            except APIException:
                print('Fail to save texture %s' % textureFileName)
    return True


def get_material_path():
	output = ""
	current_graph = program.instance.get_current_graph()
	if(current_graph):
		output = current_graph.getPackage().getFilePath()
	return output


def get_material_name(graph_instance):
 output = ""
 current_graph_name = graph_instance.getIdentifier()
 package_name = program.instance.get_package_name(graph_instance.getPackage())
 if(current_graph_name.lower() == "base"):
  output = package_name
 elif(current_graph_name.lower().startswith("inst_")):
  output = package_name + "_" + current_graph_name.replace("inst_", "")
 return output


def get_all_materials():
 output = []
 current_package = program.instance.get_current_package()
 if(current_package):
  for i in list(current_package.getChildrenResources(isRecursive=False)):
   if(get_material_name(i) != ""):
    output.append(i)
 return output


for i in get_all_materials():
 exportSDGraphOutputs(
  i,
  output_dir=os.path.dirname(i.getPackage().getFilePath()),
  file_ext="tga"
 )
 print(get_material_name(i))
