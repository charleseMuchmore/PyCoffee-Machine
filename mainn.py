from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
exit_condition = False
while exit_condition == False:
    user_input = input(f"What drink would you like? {Menu.get_items()}: ")
    if user_input == 'off':
        exit()
    if user_input == 'report':
        CoffeeMaker.report()
    if user_input != 'report' and user_input != 'exit':
        name_of_drink = user_input
        drink = Menu.find_drink(name_of_drink)
        is_resources_sufficient = CoffeeMaker.is_resource_sufficient(drink)
        if is_resources_sufficient == True:
            payment = MoneyMachine.make_payment(drink.cost)
            if payment == True:
                CoffeeMaker.make_coffee(drink)