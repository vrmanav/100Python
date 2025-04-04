# Calculator
import art
import os
import time


def add(num1, num2):
    """Adds two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Divides two numbers."""
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """Runs the calculator program."""
    os.system("clear")
    print(art.logo)
    time.sleep(1)
    while True:
        try:
            num1 = float(input("\nEnter your first number: "))
            break
        except ValueError:
            print("⚠️  You have entered an invalid input, type in a numerical value ⚠️")

    continue_calculation = True
    while continue_calculation:
        print("\nAvailable operations: ", end="")
        for symbol in symbols:
            print(symbol, end=" ")
        operation = input("\nWhat operation do you want to perform: ")
        if operation not in symbols:
            print("⚠️ Invalid input. Please enter a numerical value ⚠️")
            continue
        while True:
            try:
                num2 = float(input("\nEnter the next number: "))
                break
            except ValueError:
                print("⚠️ Invalid input. Please enter a numerical value ⚠️")
        operation_function = symbols[operation]
        result = operation_function(num1, num2)
        print(f"\n{num1} {operation} {num2} = {result}")

        choice = input(
            f"Type 'yes' to continue calculating with {result}, or type 'no' to start a new calculation: "
        ).lower()
        if choice == "yes":
            num1 = result
        elif choice == "no":
            continue_calculation = False
            calculator()


calculator()
