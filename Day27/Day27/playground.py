## Arguments whit default Values
# def my_function(a=1, b=2, c=3)

## Unlimited Positional Arguments *args
# def add(*args):
#     return sum(args)

## **kwargs: Many Keywordrd Arguments
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)

# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')

    def __str__(self):
        return f'{self.make} {self.model} {self.colour} {self.seats}'


car = Car(make='Toyota', model='GTI-R', seats=5)
print(car)
