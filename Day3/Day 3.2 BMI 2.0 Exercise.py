# BMI calculator version 2.0
from doctest import REPORTING_FLAGS


height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg :"))
bmi =round(weight/height**2,2)
result=f"Your bmi is {bmi}, you are "
if bmi < 18.5:
    print(f"{result} underweight")
elif bmi < 25:
    print(f"{result} normal weight")
elif bmi < 30:
    print(f"{result} overweight")
elif bmi < 35:
    print(f"{result} obese")
else:
    print(f"{result} clinical obese.")
