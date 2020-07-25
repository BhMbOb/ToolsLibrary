import QtQuick 2.2
import Painter 1.0

PainterPlugin
{
    property var painter_dir:alg.plugin_root_directory + "../../"
    
    // Manually created list of all tool names
    property var tools_list:[
        "template_tool"
    ]

    // Stored list of all alg buttons, used to call functions such as 'onTick'
    property var tools_references:[]

    tickIntervalMS: 1
    jsonServerPort: -1

    Component.onCompleted:
    {
        var i
        for(i = 0; i < tools_list.length; i++)
        {
            tools_references.push( alg.ui.addWidgetToPluginToolBar("../../tools/tools_library/" + tools_list[i] + "/main.qml") )
        }
    }

    // Call onTick for all tools
    onTick:
    {
        var i
        for(i = 0; i < tools_references.length; i++)
        {
            try { tools_references[i].onTick() } catch(err){}
        }
    }

    // Call onProjectOpened for all tools
    onProjectOpened:
    {
        var i
        for(i = 0; i < tools_references.length; i++)
        {
            try { tools_references[i].onProjectOpened() } catch(err){}
        }
    }

    // Call onProjectSaved for all tools
    onProjectSaved:
    {
        var i
        for(i = 0; i < tools_references.length; i++)
        {
            try { tools_references[i].onProjectSaved() } catch(err){}
        }
    }

}