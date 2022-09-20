def format_name(f_name:str,l_name:str):
    if f_name =="" or l_name =="":
        return "You didn't provide valid inputs."
    l_name=l_name.title()
    f_name=f_name.title()
    return f"{f_name} {l_name}"

print(format_name(input("enter your first name: "),input("enter your last name: ")))