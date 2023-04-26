from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    order = menu.get_items()
    choice = input(f'What would you like ({order}) : ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




