from functools import total_ordering


print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_price = 0
sentence = "You have ordered "

if size in ["s", "S"]:
    total_price += 15
    sentence += "A small pizza"
elif size in ["m", "M"]:
    total_price += 20
    sentence += "A medium pizza"
elif size in ["l", "L"]:
    total_price += 25
    sentence += "A large pizza"

if add_pepperoni in ["y", "Y"]:
    sentence += " + pepperoni"
    if size in ["s", "S"]:
        total_price += 2
    else:
        total_price += 3

if extra_cheese in ["y", "Y"]:
    total_price += 1
    sentence += " + extra cheese"

print(f"{sentence} => it costs ${total_price}")
