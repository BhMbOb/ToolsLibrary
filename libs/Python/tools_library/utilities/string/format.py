def snake_to_name(input):
    output = ""
    for i in input.split("_"):
        output += i.capitalize() + " "
    return output