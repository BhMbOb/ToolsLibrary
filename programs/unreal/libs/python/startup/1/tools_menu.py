global unreal
import unreal

if __name__ == "__main__":
    
    example_tool_list = [
        "a" ,
        "b",
        "c"  
    ]

    menus = unreal.ToolMenus.get()
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    tools_library_menu = main_menu.add_sub_menu(main_menu.get_name(), "ToolsLibrary", "ToolsLibrary", "ToolsLibrary")


    def add_menu_entry(name, script_path, parent):
        new_entry = unreal.ToolMenuEntry(
            name=name,
            type=unreal.MultiBlockType.MENU_ENTRY,
            insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
        )
        new_entry.set_label(name)
        new_entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "None", string=("print(\"" + script_path + "\")"))
        parent.add_menu_entry("Scripts", new_entry)

    for i in example_tool_list:
        add_menu_entry(i, i, tools_library_menu)

    menus.refresh_all_widgets()

# https://docs.unrealengine.com/en-US/PythonAPI/class/ToolMenus.html?highlight=find_menu#unreal.ToolMenus.find_menu
# Registers a menu by name
# unreal.ToolMenus.get().register_menu(name, parent="None", type=MultiBoxType.MENU, warn_if_already_registered=True)