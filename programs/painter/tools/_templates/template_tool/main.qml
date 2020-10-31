import QtQml 2.1
import QtQuick 2.3
import QtQuick.Window 2.2
import QtWebSockets 1.0
import QtQuick.Layouts 1.2

import AlgWidgets 2.0
import Painter 1.0

AlgToolBarButton
{
    property var tool_name:"template_tool"
    property var painter_dir:alg.plugin_root_directory + "../../"
    
    iconName:("file:///" + painter_dir + "tools/tools_library/" + tool_name + "/icon.png")
    tooltip:"Template Plugin"

    id:id_button_main
    enabled:false

    onClicked:
    {

    }

    function onTick()
    {
        //alg.log.info("Terrain tool tick!")
    }

    function onProjectOpened()
    {
        id_button_main.enabled = true
    }

    function onProjectSaved()
    {
        id_button_main.onProjectOpened()
    }

}