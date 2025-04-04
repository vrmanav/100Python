# Calculator
import art
import os
import time


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    time.sleep(1.5)
    os.system("clear")

    while True:
        try:
            num1 = float(input("\nEnter your first number: "))
            break
        except ValueError:
            print("⚠️  You have entered an invalid input, type in a numerical value ⚠️")
    print()
    for symbol in symbols:
        print(symbol, end=" ")
    operation = input("\nWhat operation do you want to perform: ")
    while True:
        try:
            num2 = float(input("\nEnter your second number: "))
            break
        except ValueError:
            print("⚠️  You have entered an invalid input, type in a numerical value ⚠️")

    operation_function = symbols[operation]
    result = operation_function(num1, num2)
    print(f"\n{num1} {operation} {num2} = {result}")


calculator()
