import random
from unittest import result
names_string = input("Give me everybody's names, seprated by a comma. ")
names = names_string.split(', ')
selected_person = random.randint(0, len(names)-1)
result = f"{names[selected_person]} is going to buy the meal today!"
print(result)
