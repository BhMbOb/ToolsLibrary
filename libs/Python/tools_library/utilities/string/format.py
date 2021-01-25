def snake_to_name(input):
    """Converts a snake_based string to a friendly name
    Ie, "this_is_the_name" -> "This Is The Name" """
    output = ""
    for i in input.split("_"):
        output += i.capitalize() + " "
    return output