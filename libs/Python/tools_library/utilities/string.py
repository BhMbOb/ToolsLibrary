def snake_to_name(input):
    """Convert a snake_based string into a friendly name
    :param <str:input> The input string
    :return <str:out> Formatted string
    """
    output = ""
    for i in input.split("_"):
        output += i.capitalize() + " "
    return output