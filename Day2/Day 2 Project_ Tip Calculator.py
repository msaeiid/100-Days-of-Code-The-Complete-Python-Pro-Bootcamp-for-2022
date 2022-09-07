from unittest import result


total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input(
    "What percentage tip would you like to give? 10,12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))
total_plus_tip = (tip_percentage/100+1)*total_bill
result = round(total_plus_tip/number_of_people, 2)
result="{:.2f}".format(result)
print(f"Each person should pay: {result}")
 