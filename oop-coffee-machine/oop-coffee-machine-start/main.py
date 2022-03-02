from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_m = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

switch = True
while switch:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == 'off':
        switch = False   
    elif choice == 'report':
        money_machine.report()
        coffee_m.report()
    else:
        drink = menu.find_drink(choice) 
        if coffee_m.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_m.make_coffee(drink)
