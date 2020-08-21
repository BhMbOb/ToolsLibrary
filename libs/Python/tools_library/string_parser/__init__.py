import tools_library


def _parse__toolslibrarypath(input_):
    return input_.replace("$(ToolsLibraryPath)", tools_library.path())


def parse(input_):
    output = input_
    output = _parse__toolslibrarypath(output)

    return output
