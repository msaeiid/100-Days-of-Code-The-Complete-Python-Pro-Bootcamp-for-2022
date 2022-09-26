MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
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


def get_item_from_menu(name: str):
    return MENU[name]


def get_price_from_menu(name: str):
    return MENU[name]['cost']


def add_to_profit(amount: int):
    resources['money'] += amount


def report_resources():
    """Report amount of resources machine has.
    """

    for resource in resources:
        if resource in ["water", "milk"]:
            print(f" {resource.capitalize()}: {resources[resource]}ml")
        elif resource == 'coffee':
            print(f"Coffee: {resources['coffee']}g")
        elif resource == 'money':
            print(f"Money: ${resources['money']}\n")


def process_coins(order: str):
    """Returns the money_received calculated from coins inserted.

    Args:
        order (str): order name

    Returns:
        int: money_received
        int: order_price
    """
    print("Please insert coins.")
    money_received = 0
    for coin in coins:
        user_input = int(input(f"How many {coin['name']}? :"))
        money_received += user_input * coin['value']
    order_price = get_price_from_menu(order)
    return money_received, order_price


def is_resource_sufficient(order: str):
    """Return True when order can be made, False if ingredients are insufficient

    Args:
        order (str): order name

    Returns:
        Bool:  sufficient resources == True else False
    """
    order_ingredients = MENU[order]['ingredients']
    not_enough_list = []
    global resources
    for item in order_ingredients:
        if resources[item] >= order_ingredients[item]:
            pass
        else:
            not_enough_list.append(item)
    if len(not_enough_list) == 0:
        return True
    print(f"Sorry there is not enough {', '.join(not_enough_list)}")
    return False


def make_coffee(order: str):
    """Deduct the required ingredients from the resources.

    Args:
        order (str): order
    """
    order_ingredients = get_item_from_menu(order)['ingredients']
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order} enjoy!")


def is_transaction_successful(order: str):
    """Return True when the payment is accepted, or False if money is insufficient.

    Args:
        order (str): order name

    Returns:
        int: change
        Bool: status transaction is successful or not
    """
    money_received, drink_cost = process_coins(order)
    change = round(money_received - drink_cost, 2)
    if change >= 0:
        add_to_profit(drink_cost)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def start_machine():
    """to start or stop the machine also to order coffee
    """
    turn_on = True
    while turn_on:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'off':
            turn_on = False
            print('Switch off!')
        elif choice == 'report':
            report_resources()
        else:
            if is_resource_sufficient(choice):
                if is_transaction_successful(choice):
                    make_coffee(choice)


start_machine()
