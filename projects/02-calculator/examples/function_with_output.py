def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version"""
    if f_name == "" or l_name == "":
        return  # return none if keep it empty or whatever we want
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_name = format_name("lluis", "giner")
print(formatted_name)
