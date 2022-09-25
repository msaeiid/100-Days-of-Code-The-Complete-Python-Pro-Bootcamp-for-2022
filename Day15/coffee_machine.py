from data import coins, hot_flavours, resources, get_flavour, increase_money


def report_resources():
    """print report.
    """
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")


def process_coins(order: str):
    """process coins

    Args:
        order (str): order name

    Returns:
        int: total-order_price
        int: order_price
    """
    print("Please insert coins.")
    total = 0
    for coin in coins:
        user_input = int(input(f"How many {coin['name']}? :"))
        total += user_input*coin['value']
    order_price = get_flavour(order)['price']
    if total - order_price >= 0:
        return total - order_price, order_price
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0, order_price


def check_resources(order: str):
    """check resources sufficient

    Args:
        order (str): order name

    Returns:
        Bool:  sufficient resources == True else False
    """
    for flavour in hot_flavours:
        if flavour['name'] == order:
            check_resources = {
                'water': resources['water']-flavour['water'],
                'coffee': resources['coffee']-flavour['coffee'],
                'milk': resources['milk']-flavour['milk']
            }
            not_enough_list = [
                item for item in check_resources if check_resources[item] < 0]
            if len(not_enough_list) == 0:
                resources['water'] -= flavour['water']
                resources['coffee'] -= flavour['coffee']
                resources['milk'] -= flavour['milk']
                return True
            else:
                print(
                    f"Sorry there is not enough {', '.join(not_enough_list)}")
                return False


def make_coffee(order: str):
    """make coffee

    Args:
        order (str): order
    """
    print(f"Here is your {order} enjoy!")


def check_transaction(order: str):
    """check transaction successful

    Args:
        order (str): order name
    """
    # positive, 0 or negative
    if check_resources(order):
        difference, order_price = process_coins(order)
        if difference > 0:
            print(f"Here is ${round(difference,2)} in change.")
            increase_money(order_price)
            make_coffee(order)


def start_machine():
    """to start or stop the machine also to order coffee
    """
    turn_on = True
    while turn_on:
        user_order = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if user_order == 'off':
            turn_on = False
            print('Switch off!')
        elif user_order == 'report':
            report_resources()
        else:
            check_transaction(user_order)


start_machine()
