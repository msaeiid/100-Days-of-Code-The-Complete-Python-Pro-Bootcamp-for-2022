from data import coins, hot_flavours, resources, get_flavour, increase_money


def report_resources():
    """print report.
    """

    for resource in resources:
        if resource in ["water", "milk"]:
            print(f" {resource.capitalize()}: {resources[resource]}ml")
        elif resource == 'coffee':
            print(f"Coffee: {resources['coffee']}g")
        elif resource == 'money':
          print(f"Money: ${resources['money']}\n")


def process_coins(order: str):
    """process coins

    Args:
        order (str): order name

    Returns:
        int: total
        int: order_price
    """
    print("Please insert coins.")
    total = 0
    for coin in coins:
        user_input = int(input(f"How many {coin['name']}? :"))
        total += user_input*coin['value']
    order_price = get_flavour(order)['price']
    return total, order_price


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

    Returns:
        int: difference
        Bool: status transaction is successful or not
    """
    total, order_price = process_coins(order)
    difference = total-order_price
    if difference >= 0:
        increase_money(order_price)
        print(f"Here is ${round(difference,2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


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
            if check_resources(user_order):
                status = check_transaction(user_order)
                if status:
                    make_coffee(user_order)


start_machine()
