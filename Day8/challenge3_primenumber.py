
from itertools import count


def prime_number(number):
    is_prime=True
    for i in range(2, number):
        if number % i == 0:
            is_prime=False
    return is_prime


n = int(input("Check this number: "))
result = prime_number(number=n)
if result:
    print("It's a prime number.")
else:
    print("It's not a prime number.")