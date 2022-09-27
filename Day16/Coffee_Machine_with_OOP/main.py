# 1.print report.
# 2. Check resources sufficient
# 3. Process coins
# 4. Check transaction successful
# 5. Make Coffee

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == 'off':
        is_on = False
        print('Switch off!')
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
