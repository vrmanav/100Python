# Coffee Maker
import os
from prettytable import PrettyTable


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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def greet():
    """Greets the user & displays menu card in tabular format"""
    os.system("clear")
    print("\t⭐️ WELCOME TO MANAV'S CAFE ⭐️\n")
    table = PrettyTable()
    table.field_names = ["Drink", "Cost"]
    for drink in MENU:
        drink_cost = MENU[drink]["cost"]
        table.add_row([drink.capitalize(), drink_cost])
    print(table)


def show_report():
    """Displays the ingredients remaining in the machine"""
    os.system("clear")
    print(f"* Water: {resources["water"]} ml")
    print(f"* Milk: {resources["milk"]} ml")
    print(f"* Coffee: {resources["coffee"]} g")
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    """Returns whether the resources are sufficient for the order placed or not"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"\n⚠️  Sorry there is not enough {item} ")
            return False
    return True


def process_coins():
    "Collects & returns the sum of coins given"
    print("\nPlease make your payment...")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(drink_cost, money_received):
    "Compares money received by user with that of drink's cost& return change if any"
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is your ${change} in change, ", end="")
        global profit
        profit += change
        return True
    else:
        print("\nSorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from resources"""
    for item in resources:
        resources[item] -= ingredients[item]
    print(f"and your {drink_name}. Enjoy ☕️")


def coffee_machine():
    "Starts the coffee machine"
    greet()
    order = input("\nWhat would you like to have: ").lower()
    if order == "off":
        print("\n\t⚠️ Turning OFF the machine ⚠️")
    elif order == "report":
        show_report()
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(drink["cost"], payment):
                make_coffee(order, drink["ingredients"])


coffee_machine()
