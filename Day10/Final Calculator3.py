#add


from tokenize import group


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
def calculator():
    num1 = int(input("What's the first number?: "))
    for operator in operators:
        print(operator)
    go_on=True
    answer=0
    while go_on:
        operator_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operators[operator_symbol]
        answer = calculation_function(num1, num2)
        print(f'{num1} {operator_symbol} {num2} = {answer}')
        user_answer=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if user_answer == 'n':
            go_on=False
            calculator()
        else:
            num1=answer
calculator()
