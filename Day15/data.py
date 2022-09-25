# in 15 day I learned how  to install python, pycharm and so on ...
from unicodedata import decimal
from unittest import result


hot_flavours = [
    {
        'name': 'espresso',
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'price': 1.50,
    },
    {
        'name': 'latte',
        'water': 200,
        'coffee': 24,
        'milk': 150,
        'price': 2.50,
    },
    {
        'name': 'cappuccino',
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'price': 3.00,
    },
]
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}
coins = [
    {
        'name': 'quarters',
        'value': 0.25
    },
    {
        'name': 'dimes',
        'value': 0.10
    },
    {
        'name': 'nickles',
        'value': 0.05
    },
    {
        'name': 'pennies',
        'value': 0.01
    },
]


def get_flavour(name: str):
    return [flavour for flavour in hot_flavours if flavour['name'] == name][0]

def increase_money(amount:decimal):
    resources['money']+=amount