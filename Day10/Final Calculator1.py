#add


def add(n1: int, n2: int):
    return n1+n2
#subtract


def subtract(n1: int, n2: int):
    return n1-n2

#multiply


def multiply(n1: int, n2: int):
    return n1*n2
#divive


def divide(n1: int, n2: int):
    if n2 != 0:
        return n1/n2


operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num1 = int(input("What's the first number?: "))
for operator in operators:
    print(operator)
operator_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operators[operator_symbol]
answer = calculation_function(num1, num2)
print(f'{num1} {operator_symbol} {num2} = {answer}')
