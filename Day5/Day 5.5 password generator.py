import string
import random

number_of_lettes = int(
    input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))
password = []
for i in range(number_of_lettes):
    password.append(random.choice(string.ascii_letters))
for i in range(number_of_symbols):
    password.append(random.choice(string.punctuation))
for i in range(number_of_numbers):
    password.append(random.choice(string.digits))
random.shuffle(password)
print(''.join(password))
