from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine_my = MoneyMachine()
coffee_maker_my = CoffeeMaker()
is_on = True
menu_my = Menu()




while is_on:
    option = menu_my.get_items()
    choice = input("What would you like? " + option +" ")
    if choice == 'off':
        machine_on = False
    elif choice == "report":
        coffee_maker_my.report()
        money_machine_my.report()
    else:
        drink = menu_my.find_drink(choice)
        if coffee_maker_my.is_resource_sufficient(drink):
            if money_machine_my.make_payment(drink.cost):
                coffee_maker_my.make_coffee(drink)