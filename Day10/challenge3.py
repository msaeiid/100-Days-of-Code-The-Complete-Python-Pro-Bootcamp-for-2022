def format_name(f_name:str,l_name:str):
    """doc string

    Args:
        f_name (str): First name
        l_name (str): Last name

    Returns:
        _type_: integere with valid input
    """
    if f_name =="" or l_name =="":
        return "You didn't provide valid argument."
    l_name=l_name.title()
    f_name=f_name.title()
    return f"{f_name} {l_name}"

print(format_name(input("enter your first name: "),input("enter your last name: ")))