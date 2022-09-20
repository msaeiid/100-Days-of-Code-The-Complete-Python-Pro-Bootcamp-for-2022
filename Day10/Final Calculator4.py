#add


from art import logo
import imp
from tokenize import group


def add(n1: float, n2: float):
    return n1+n2
#subtract


def subtract(n1: float, n2: float):
    return n1-n2

#multiply


def multiply(n1: float, n2: float):
    return n1*n2
#divive


def divide(n1: float, n2: float):
    if n2 != 0:
        return n1/n2


operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operators:
        print(operator)
    go_on = True
    answer = 0
    while go_on:
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operator_symbol]
        answer = calculation_function(num1, num2)
        print(f'{num1} {operator_symbol} {num2} = {answer}')
        user_answer = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if user_answer == 'n':
            go_on = False
            calculator()
        else:
            num1 = answer


calculator()
