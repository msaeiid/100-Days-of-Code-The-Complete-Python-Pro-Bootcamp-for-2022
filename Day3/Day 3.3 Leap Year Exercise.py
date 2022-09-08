from unittest import result


year = int(input("which year do you want to check ?"))
result = "Not Leap year!"
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = "Leap year!"
    else:
        result = "Leap year!"
print(result)
