import os
import sd
from sd.api.sbs import sdsbscompgraph
from sd.api import sdproperty
from sd.api.apiexception import APIException

from program import instance


def export_current_graph():
    print("TODO:")


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