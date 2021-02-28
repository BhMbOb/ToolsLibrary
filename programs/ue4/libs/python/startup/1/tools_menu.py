import unreal

import tools_library
import tools_library.utilities.string as string_utils
from tools_library.framework.module import PluginData, ProgramData


unreal_path = os.path.join(tools_library.path(), "programs\\ue4")
unreal_tools_path = os.path.join(unreal_path, "tools\\")

#
branch_menus = {}


def add_menu_branch(parent_menu, branch_string, script_path="", section_context="Tools"):
    """Adds a new menu branch from a path string (Ie, "a\\b\\c")"""
    branch_string_split = branch_string.split("\\")
    current_branch_full = ""

    for current_branch_name in branch_string_split:
        current_branch_full = os.path.join(current_branch_full, current_branch_name)
        current_branch_upper = os.path.dirname(current_branch_full)

        if(current_branch_upper in list(branch_menus)):
            ui_menu_parent = branch_menus[current_branch_upper]
        else:
            ui_menu_parent = parent_menu

        if(current_branch_full == branch_string):
            # if we're adding the final one (the script which will be launched)
            ui_new_item = unreal.ToolMenuEntry(name=branch_string, type=unreal.MultiBlockType.MENU_ENTRY, insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST))
            ui_new_item.set_label(string_utils.snake_to_name(current_branch_name))
            ui_new_item.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "None", string=str("import tools_library; tools_library.run_tool(\"" + script_path.replace("\\", "/") + "\")"))
            ui_menu_parent.add_menu_entry(section_context, ui_new_item)
        elif(current_branch_full not in list(branch_menus)):
            # if we're just adding a submenu
            name_formatted = string_utils.snake_to_name(current_branch_name)
            ui_new_menu = ui_menu_parent.add_sub_menu(section_context, branch_string, name_formatted, name_formatted)
            branch_menus[current_branch_full] = ui_new_menu


def add_dir_as_branch(path_, parent_menu=None, section_context="Tools"):
    """Loops over all subdirectories in a path and adds them as menus or actions"""
    possible_tool_dirs = [x[0] for x in os.walk(path_)]
    tool_paths = []
    tool_menu_branches = []

    for dir_ in possible_tool_dirs:
        if(os.path.isfile(os.path.join(dir_, "main.py"))):
            tool_menu_branches.append(dir_.replace(path_, ""))
            tool_paths.append(os.path.join(dir_, "main.py"))
        for dir_child in os.listdir(dir_):
            if(dir_child.endswith(".toolptr")):
                tool_menu_branches.append(os.path.join(dir_, dir_child.split(".")[0]).replace(path_, ""))
                tool_paths.append(os.path.join(dir_, dir_child))
    for i in range(len(tool_menu_branches)):
        add_menu_branch(parent_menu, tool_menu_branches[i], script_path=tool_paths[i], section_context=section_context)


def load_script_from_path(path):
    """Loads a python script from the input path"""
    path_ = path
    globals_ = {"__file__": path_}
    exec(open(path_).read(), globals_)


def initialize_tools_library_menu():
    """Creates the tools library menu structure"""
    # create the base menu
    menus = unreal.ToolMenus.get()
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    tools_library_menu = main_menu.add_sub_menu(main_menu.get_name(), "Tools Library", "Tools Library", "Tools Library")
    tools_library_menu.searchable = True

    # loop over all base unreal tools and add them
    add_dir_as_branch(os.path.join(tools_library.path(), "programs\\ue4\\tools\\"), parent_menu=tools_library_menu, section_context="Tools")

    # loop over all separate plugins and add them to their branches
    # add separator
    for plugin_dir in tools_library.plugin_dirs():
        plugin_dir_tools_unreal_dir = os.path.join(plugin_dir, "programs\\ue4\\tools\\")
        plugin_name = os.path.basename(plugin_dir)
        if(PluginData(plugin_name).is_enabled):
            plugin_name_formatted = string_utils.snake_to_name(plugin_name)
            ui_plugin_menu_branch = tools_library_menu.add_sub_menu("Plugins", plugin_name_formatted, plugin_name_formatted, plugin_name_formatted)
            if(os.path.exists(plugin_dir_tools_unreal_dir)):
                add_dir_as_branch(plugin_dir_tools_unreal_dir, parent_menu=ui_plugin_menu_branch, section_context="Plugins")

    # helper / additional
    ui_show_in_explorer = unreal.ToolMenuEntry(name="ShowInExplorer", type=unreal.MultiBlockType.MENU_ENTRY, insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST))
    ui_show_in_explorer.set_label("Show In Explorer")
    ui_show_in_explorer.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "None", string=("import tools_library;tools_library.run_tool(\"programs\\python\\scripts\\show_in_explorer.py\")"))
    tools_library_menu.add_menu_entry("Info", ui_show_in_explorer)

    ui_open_git_repo = unreal.ToolMenuEntry(name="OpenGithubRepo", type=unreal.MultiBlockType.MENU_ENTRY, insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST))
    ui_open_git_repo.set_label("Github Repo")
    ui_open_git_repo.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "None", string=("import tools_library;tools_library.run_tool(\"programs\\python\\scripts\\open_git_repo.py\")"))
    tools_library_menu.add_menu_entry("Info", ui_open_git_repo)


    # finalize
    menus.refresh_all_widgets()


initialize_tools_library_menu()
