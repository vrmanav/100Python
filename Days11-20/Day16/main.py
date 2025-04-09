from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def greet():
    """Greet the user & show the menu-card"""
    os.system("clear")
    print("WELCOME TO MANAV'S CAFE")
    print(f"\nAvailable drinks are")
    print(menu.get_items())


def coffee_machine():
    greet()
    order = input("What would you like to have: ").lower()
    if order == "off":
        print("\n⚠️ Turning OFF the machine.. ⚠️")
        print("Machine turned OFF 😴")
    elif order == "report":
        print("\nRemaining resource are ..")
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


coffee_machine()
